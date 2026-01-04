import { useState, useEffect } from 'react'
import { useMutation, useQuery } from '@tanstack/react-query'
import { generationApi } from '@/lib/api'
import { useAuthStore } from '@/stores/authStore'
import toast from 'react-hot-toast'
import { BookOpen, Upload, Loader2, Plus, CheckCircle2, XCircle, FileText, Eye, Database } from 'lucide-react'

interface MCQQuestion {
  question: string
  answer: string
  distractors: string[]
  explanation?: string
  topic_name?: string
  difficulty_level?: string
}

interface LectureFile {
  file_name: string
  file_path: string
  bucket: string
}

interface WeekData {
  week_number: number
  files: LectureFile[]
}

interface CourseData {
  course_code: string
  bucket_name: string
  weeks: WeekData[]
}

export default function Dashboard() {
  const user = useAuthStore((state) => state.user)
  const [courseCode, setCourseCode] = useState('')
  const [selectedWeek, setSelectedWeek] = useState<number | null>(null)
  const [showUpload, setShowUpload] = useState(false)
  const [uploadFile, setUploadFile] = useState<File | null>(null)
  const [generatedMCQs, setGeneratedMCQs] = useState<MCQQuestion[]>([])
  const [showTopicSelector, setShowTopicSelector] = useState(false)
  const [numberOfTopics, setNumberOfTopics] = useState(5)
  const [selectedPdf, setSelectedPdf] = useState<string | null>(null)
  const [showMCQUpload, setShowMCQUpload] = useState(false)
  const [mcqFile, setMcqFile] = useState<File | null>(null)
  const [showIndexModal, setShowIndexModal] = useState(false)
  const [uploadedMCQs, setUploadedMCQs] = useState<any[]>([])
  const [showBookUpload, setShowBookUpload] = useState(false)
  const [bookFile, setBookFile] = useState<File | null>(null)
  const [showGraphIndexModal, setShowGraphIndexModal] = useState(false)
  const [showNewWeekUpload, setShowNewWeekUpload] = useState(false)
  const [newWeekNumber, setNewWeekNumber] = useState<number>(1)


  // Fetch lectures when course code is selected
  const { data: lecturesData, refetch: refetchLectures } = useQuery({
    queryKey: ['lectures', courseCode],
    queryFn: async () => {
      if (!courseCode) {
        return { courses: [] }
      }
      const response = await generationApi.listLectures(courseCode)
      return response.data
    },
    enabled: !!courseCode,
  })

  // Set initial course code if user has teaching courses
  useEffect(() => {
    if (user?.teaching_courses && user.teaching_courses.length > 0 && !courseCode) {
      setCourseCode(user.teaching_courses[0])
    }
  }, [user, courseCode])

  const uploadMutation = useMutation({
    mutationFn: async (data: { file: File; course_code: string; week_number: number }) => {
      const response = await generationApi.uploadFile(data.file, data.course_code, data.week_number)
      return response.data
    },
    onSuccess: () => {
      toast.success('Lecture uploaded successfully!')
      setUploadFile(null)
      setShowUpload(false)
      setShowNewWeekUpload(false)
      refetchLectures() // Refresh lectures list
    },
    onError: (error: any) => {
      toast.error(error.message || 'Failed to upload lecture')
    },
  })

  const generateMutation = useMutation({
    mutationFn: async (data: { course_code: string; week_number: number; number_of_topics: number }) => {
      const response = await generationApi.generateQuiz({
        course_code: data.course_code,
        week_number: data.week_number,
        number_of_topics: data.number_of_topics,
      })
      return response.data
    },
    onSuccess: (data: any) => {
      setGeneratedMCQs(data.questions || [])
      setShowTopicSelector(false)
      toast.success(`Successfully generated ${data.questions?.length || 0} MCQs!`)
    },
    onError: (error: any) => {
      toast.error(error.response?.data?.detail || error.message || 'Generation failed')
    },
  })

  const handleUpload = (weekNumber: number) => {
    setSelectedWeek(weekNumber)
    setShowUpload(true)
    setShowTopicSelector(false)
    setGeneratedMCQs([])
  }

  const handleGenerate = (weekNumber: number) => {
    if (!courseCode) {
      toast.error('Please enter a course code first')
      return
    }
    setSelectedWeek(weekNumber)
    setShowTopicSelector(true)
    setShowUpload(false)
    setGeneratedMCQs([])
  }

  const handleConfirmGenerate = () => {
    if (!selectedWeek) return
    setShowTopicSelector(false)
    generateMutation.mutate({ 
      course_code: courseCode, 
      week_number: selectedWeek,
      number_of_topics: numberOfTopics
    })
  }

  const handleFileUpload = () => {
    if (!uploadFile || !courseCode || !selectedWeek) {
      toast.error('Please select a file and ensure course code and week are set')
      return
    }
    uploadMutation.mutate({ file: uploadFile, course_code: courseCode, week_number: selectedWeek })
  }

  const handleNewWeekFileUpload = () => {
    if (!uploadFile || !courseCode) {
      toast.error('Please select a file and ensure course code is set')
      return
    }
    uploadMutation.mutate({ file: uploadFile, course_code: courseCode, week_number: newWeekNumber })
  }

  const addWeek = () => {
    if (!courseCode) {
      toast.error('Please select a course code first')
      return
    }
    const existingWeeks = lecturesData?.courses
      ?.find((course: CourseData) => course.course_code.toLowerCase() === courseCode.toLowerCase())
      ?.weeks.map((w: WeekData) => w.week_number) || []
    
    const nextWeek = existingWeeks.length > 0 ? Math.max(...existingWeeks) + 1 : 1
    setNewWeekNumber(nextWeek)
    setShowNewWeekUpload(true)
  }

  const getDifficultyColor = (difficulty?: string) => {
    switch (difficulty?.toLowerCase()) {
      case 'easy':
        return 'bg-gray-100 text-gray-800 border-gray-300'
      case 'medium':
        return 'bg-gray-200 text-gray-800 border-gray-300'
      case 'hard':
        return 'bg-gray-300 text-gray-900 border-gray-400'
      default:
        return 'bg-gray-100 text-gray-800 border-gray-200'
    }
  }

  const handleMCQFileChange = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0]
    if (!file) return

    setMcqFile(file)

    // Read and parse the JSON file
    try {
      const text = await file.text()
      const mcqs = JSON.parse(text)
      setUploadedMCQs(mcqs)
    } catch (error) {
      toast.error('Invalid JSON file format')
      setMcqFile(null)
      setUploadedMCQs([])
    }
  }

  const handleMCQUpload = () => {
    if (!mcqFile || uploadedMCQs.length === 0) {
      toast.error('Please select a valid MCQ JSON file')
      return
    }
    setShowIndexModal(true)
  }

  const indexMutation = useMutation({
    mutationFn: async (data: { mcqs: any[], course_code: string }) => {
      const response = await generationApi.indexMCQs({
        mcqs: data.mcqs,
        course_code: data.course_code,
      })
      return response.data
    },
    onSuccess: () => {
      toast.success('MCQs indexed to vector database successfully!')
      setShowIndexModal(false)
      setShowMCQUpload(false)
      setMcqFile(null)
      setUploadedMCQs([])
    },
    onError: (error: any) => {
      toast.error(error.response?.data?.detail || error.message || 'Failed to index MCQs')
    },
  })

  const handleConfirmIndex = () => {
    if (!courseCode) {
      toast.error('Course code is required')
      return
    }
    indexMutation.mutate({
      mcqs: uploadedMCQs,
      course_code: courseCode,
    })
  }

  const handleBookFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0]
    if (!file) return
    setBookFile(file)
  }

  const handleBookUpload = () => {
    if (!bookFile) {
      toast.error('Please select a book file')
      return
    }
    setShowGraphIndexModal(true)
  }

  const graphIndexMutation = useMutation({
    mutationFn: async (data: { file: File; course_code: string }) => {
      // Upload file to MinIO (without week_number)
      const uploadResult = await generationApi.uploadBook(data.file, data.course_code)

      // Index to graph database
      const indexResponse = await fetch('http://localhost:3006/v1/indexing', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          course_code: data.course_code,
          file_path: uploadResult.data.file_path || uploadResult.data.path,
        }),
      })

      if (!indexResponse.ok) {
        throw new Error('Failed to index book to graph database')
      }

      return indexResponse.json()
    },
    onSuccess: () => {
      toast.success('Book indexed to graph database successfully!')
      setShowGraphIndexModal(false)
      setShowBookUpload(false)
      setBookFile(null)
    },
    onError: (error: any) => {
      toast.error(error.message || 'Failed to index book to graph database')
    },
  })

  const handleConfirmGraphIndex = () => {
    if (!courseCode) {
      toast.error('Course code is required')
      return
    }
    if (!bookFile) {
      toast.error('Book file is required')
      return
    }
    graphIndexMutation.mutate({
      file: bookFile,
      course_code: courseCode,
    })
  }

  return (
    <div className="min-h-screen bg-gray-50 p-6">
      <div className="max-w-7xl mx-auto">
        {/* Header */}
        <div className="mb-8 text-center">
          <div className="flex items-center justify-center gap-3 mb-3">
            <h1 className="text-4xl font-bold text-gray-900">
              Teacher Dashboard
            </h1>
          </div>
          <p className="text-gray-600 text-lg">Upload lectures and generate intelligent MCQs for your courses</p>
        </div>

        {/* Course Selector */}
        <div className="bg-white rounded-xl shadow-md p-8 mb-8 border border-gray-200">
          <label className="block text-sm font-semibold text-gray-700 mb-3 uppercase tracking-wide">
            Select Course
          </label>
          {user?.teaching_courses && user.teaching_courses.length > 0 ? (
            <div className="flex flex-wrap gap-3">
              {user.teaching_courses.map((course) => (
                <button
                  key={course}
                  onClick={() => setCourseCode(course)}
                  className={`px-6 py-3 rounded-lg font-semibold transition-all duration-200 ${
                    courseCode === course
                      ? 'bg-blue-600 text-white shadow-md'
                      : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                  }`}
                >
                  {course.toUpperCase()}
                </button>
              ))}
            </div>
          ) : (
            <div className="flex items-center gap-3">
              <input
                type="text"
                placeholder="e.g., INT3405, DSA2025"
                className="flex-1 md:w-96 px-5 py-3 bg-gray-50 border-2 border-gray-200 rounded-xl focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition-all duration-200 text-gray-900 placeholder-gray-400 font-medium"
                value={courseCode}
                onChange={(e) => setCourseCode(e.target.value.toLowerCase())}
              />
            </div>
          )}
        </div>

        {/* My Lectures Section */}
        {courseCode && (
          <div className="bg-white rounded-xl shadow-md p-8 mb-8 border border-gray-200">
            <div className="flex items-center justify-between mb-6">
              <h2 className="text-2xl font-bold text-gray-900 flex items-center gap-3">
                <FileText className="w-7 h-7 text-gray-700" />
                My Lectures - {courseCode.toUpperCase()}
              </h2>
              <div className="flex items-center gap-3">
                <button
                  onClick={() => setShowBookUpload(true)}
                  className="flex items-center gap-2 px-5 py-2.5 bg-blue-600 text-white font-semibold rounded-lg hover:bg-blue-700 shadow-md transition-all duration-200"
                >
                  <BookOpen className="w-5 h-5" />
                  Add Book
                </button>
                <button
                  onClick={addWeek}
                  className="flex items-center gap-2 px-5 py-2.5 bg-blue-600 text-white font-semibold rounded-lg hover:bg-blue-700 shadow-md transition-all duration-200"
                >
                  <Plus className="w-5 h-5" />
                  Add New Week
                </button>
              </div>
            </div>
            
            <div className="space-y-4">
              {(() => {
                // Get all existing weeks from lectures
                const existingWeeks = lecturesData?.courses
                  ?.find((course: CourseData) => course.course_code.toLowerCase() === courseCode.toLowerCase())
                  ?.weeks.map((w: WeekData) => w.week_number) || []
                
                // Only show weeks that have lectures
                const allWeeks = existingWeeks.sort((a: number, b: number) => a - b)
                
                return allWeeks.length > 0 ? (
                  <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                    {allWeeks.map((week: number) => {
                      // Find lectures for this week
                      const weekLectures = lecturesData?.courses
                        ?.find((course: CourseData) => course.course_code.toLowerCase() === courseCode.toLowerCase())
                        ?.weeks.find((w: WeekData) => w.week_number === week)?.files || []

                      const hasLectures = weekLectures.length > 0

                      return (
                        <div
                          key={week}
                          className="relative border border-gray-200 rounded-lg p-6 hover:shadow-md hover:border-gray-300 transition-all duration-200 bg-white"
                        >
                          {/* Delete Week Button - removed since weeks are managed by lectures */}

                          <div className="flex items-center justify-between mb-4">
                            <h3 className="text-xl font-bold text-gray-900">Week {week}</h3>
                            <div className={`p-2 rounded-lg ${hasLectures ? 'bg-gray-100' : 'bg-gray-100'}`}>
                              <BookOpen className={`w-6 h-6 ${hasLectures ? 'text-gray-700' : 'text-gray-500'}`} />
                            </div>
                          </div>

                          {/* Lecture Files */}
                          {hasLectures && (
                            <div className="mb-4 space-y-2">
                              <p className="text-xs font-semibold text-gray-500 uppercase tracking-wide mb-2">
                                📚 {weekLectures.length} {weekLectures.length === 1 ? 'Lecture' : 'Lectures'}
                              </p>
                              {weekLectures.map((file: LectureFile, idx: number) => (
                                <button
                                  key={idx}
                                  onClick={() => {
                                    const url = generationApi.getLectureDownloadUrl(file.bucket, file.file_path)
                                    setSelectedPdf(url)
                                  }}
                                  className="w-full flex items-center gap-2 p-3 bg-gray-50 hover:bg-gray-100 border border-gray-200 rounded-lg transition-all text-left group/file"
                                >
                                  <FileText className="w-4 h-4 text-gray-600 flex-shrink-0" />
                                  <span className="flex-1 text-sm text-gray-800 font-medium truncate">
                                    {file.file_name}
                                  </span>
                                  <Eye className="w-4 h-4 text-gray-600 flex-shrink-0" />
                                </button>
                              ))}
                            </div>
                          )}
                          
                          {/* Action Buttons */}
                          <div className="space-y-3">
                            {/* Show Upload button only for weeks without lectures */}
                            {!hasLectures && (
                              <button
                                onClick={() => handleUpload(week)}
                                disabled={!courseCode || uploadMutation.isPending}
                                className="w-full py-3 px-4 bg-blue-600 text-white font-semibold rounded-lg hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed shadow-sm transition-all duration-200 flex items-center justify-center gap-2"
                              >
                                <Upload className="w-4 h-4" />
                                Upload Lecture
                              </button>
                            )}
                            
                            {/* Show Create MCQs button only for weeks with lectures */}
                            {hasLectures && (
                              <button
                                onClick={() => handleGenerate(week)}
                                disabled={!courseCode || generateMutation.isPending}
                                className="w-full py-3 px-4 bg-blue-600 text-white font-semibold rounded-lg hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed shadow-sm transition-all duration-200 flex items-center justify-center gap-2"
                              >
                                {generateMutation.isPending && selectedWeek === week ? (
                                  <>
                                    <Loader2 className="w-4 h-4 animate-spin" />
                                    Generating...
                                  </>
                                ) : (
                                  <>
                                    Create MCQs
                                  </>
                                )}
                              </button>
                            )}
                          </div>
                        </div>
                      )
                    })}
                  </div>
                ) : (
                  <div className="text-center py-12">
                    <BookOpen className="w-16 h-16 text-gray-300 mx-auto mb-4" />
                    <p className="text-gray-500 text-lg mb-2">No lectures yet</p>
                    <p className="text-gray-400 text-sm">Click "Add New Week" to start uploading lectures</p>
                  </div>
                )
              })()}
            </div>
          </div>
        )}

        {/* PDF Viewer Modal */}
        {selectedPdf && (
          <div className="fixed inset-0 bg-black bg-opacity-50 z-50 flex items-center justify-center p-4">
            <div className="bg-white rounded-2xl shadow-2xl w-full max-w-6xl h-[90vh] flex flex-col">
              <div className="flex items-center justify-between p-4 border-b border-gray-200">
                <h3 className="text-xl font-bold text-gray-900">Lecture Viewer</h3>
                <button
                  onClick={() => setSelectedPdf(null)}
                  className="p-2 hover:bg-gray-100 rounded-lg transition-all"
                >
                  <XCircle className="w-6 h-6 text-gray-600" />
                </button>
              </div>
              <div className="flex-1 overflow-hidden">
                <iframe
                  src={selectedPdf}
                  className="w-full h-full"
                  title="Lecture PDF"
                />
              </div>
            </div>
          </div>
        )}

        {/* Topic Selector Section */}
        {showTopicSelector && selectedWeek && (
          <div className="bg-white rounded-xl shadow-md p-8 mb-8 border border-gray-200 animate-in slide-in-from-top duration-300">
            <div className="flex items-center justify-between mb-6">
              <div className="flex items-center gap-3">
                <h2 className="text-2xl font-bold text-gray-900">
                  Generate MCQs - Week {selectedWeek}
                </h2>
              </div>
              <button
                onClick={() => setShowTopicSelector(false)}
                className="text-gray-400 hover:text-gray-600 hover:bg-gray-100 p-2 rounded-lg transition-all"
              >
                <XCircle className="w-6 h-6" />
              </button>
            </div>

            <div className="space-y-6">
              <div>
                <label className="block text-sm font-semibold text-gray-700 mb-3 uppercase tracking-wide">
                  Number of Topics
                </label>
                <p className="text-sm text-gray-600 mb-4">
                  Select how many topics you want to generate MCQs for. More topics = more questions.
                </p>
                <div className="flex items-center gap-4">
                  <input
                    type="range"
                    min="1"
                    max="10"
                    value={numberOfTopics}
                    onChange={(e) => setNumberOfTopics(parseInt(e.target.value))}
                    className="flex-1 h-3 bg-gray-200 rounded-lg appearance-none cursor-pointer
                      [&::-webkit-slider-thumb]:appearance-none [&::-webkit-slider-thumb]:w-6 [&::-webkit-slider-thumb]:h-6 
                      [&::-webkit-slider-thumb]:rounded-full [&::-webkit-slider-thumb]:bg-blue-600 
                      [&::-webkit-slider-thumb]:cursor-pointer [&::-webkit-slider-thumb]:shadow-md
                      [&::-moz-range-thumb]:w-6 [&::-moz-range-thumb]:h-6 [&::-moz-range-thumb]:rounded-full 
                      [&::-moz-range-thumb]:bg-blue-600 
                      [&::-moz-range-thumb]:cursor-pointer 
                      [&::-moz-range-thumb]:border-0 [&::-moz-range-thumb]:shadow-md"
                  />
                  <div className="flex items-center justify-center w-16 h-16 bg-blue-600 text-white text-2xl font-bold rounded-lg shadow-md">
                    {numberOfTopics}
                  </div>
                </div>
                <div className="flex justify-between text-xs text-gray-500 mt-2">
                  <span>1 topic</span>
                  <span>10 topics</span>
                </div>
              </div>

              <button
                onClick={handleConfirmGenerate}
                disabled={generateMutation.isPending}
                className="w-full flex items-center justify-center gap-3 py-4 px-6 bg-blue-600 text-white font-semibold rounded-lg hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed shadow-md transition-all duration-200"
              >
                {generateMutation.isPending ? (
                  <>
                    <Loader2 className="w-5 h-5 animate-spin" />
                    Generating MCQs...
                  </>
                ) : (
                  <>
                    Generate {numberOfTopics} {numberOfTopics === 1 ? 'Topic' : 'Topics'}
                  </>
                )}
              </button>
            </div>
          </div>
        )}

        {/* Upload Section */}
        {showUpload && selectedWeek && (
          <div className="bg-white rounded-xl shadow-md p-8 mb-8 border border-gray-200 animate-in slide-in-from-top duration-300">
            <div className="flex items-center justify-between mb-6">
              <div className="flex items-center gap-3">
                <h2 className="text-2xl font-bold text-gray-900">
                  Upload Lecture - Week {selectedWeek}
                </h2>
              </div>
              <button
                onClick={() => {
                  setShowUpload(false)
                  setUploadFile(null)
                }}
                className="text-gray-400 hover:text-gray-600 hover:bg-gray-100 p-2 rounded-lg transition-all"
              >
                <XCircle className="w-6 h-6" />
              </button>
            </div>

            <div className="space-y-5">
              <div>
                <label className="block text-sm font-semibold text-gray-700 mb-3 uppercase tracking-wide">
                  Select File
                </label>
                <div className="relative">
                  <input
                    type="file"
                    accept=".pdf,.doc,.docx,.txt,.ppt,.pptx"
                    className="w-full px-5 py-4 border-2 border-dashed border-gray-300 rounded-xl hover:border-gray-400 transition-all cursor-pointer file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-gray-100 file:text-gray-700 hover:file:bg-gray-200"
                    onChange={(e) => setUploadFile(e.target.files?.[0] || null)}
                  />
                </div>
                {uploadFile && (
                  <div className="mt-3 flex items-center gap-2 p-3 bg-gray-50 border border-gray-200 rounded-lg">
                    <CheckCircle2 className="w-5 h-5 text-gray-700" />
                    <p className="text-sm text-gray-700 font-medium">
                      {uploadFile.name} <span className="text-gray-500">({(uploadFile.size / 1024 / 1024).toFixed(2)} MB)</span>
                    </p>
                  </div>
                )}
              </div>

              <button
                onClick={handleFileUpload}
                disabled={!uploadFile || uploadMutation.isPending}
                className="w-full flex items-center justify-center gap-3 py-4 px-6 bg-blue-600 text-white font-semibold rounded-lg hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed shadow-md transition-all duration-200"
              >
                {uploadMutation.isPending ? (
                  <>
                    <Loader2 className="w-5 h-5 animate-spin" />
                    Uploading...
                  </>
                ) : (
                  <>
                    <Upload className="w-5 h-5" />
                    Upload File
                  </>
                )}
              </button>
            </div>
          </div>
        )}

        {/* Generated MCQs Section */}
        {generatedMCQs.length > 0 && (
          <div className="bg-white rounded-xl shadow-md p-8 mb-8 border border-gray-200">
            <div className="flex items-center gap-3 mb-6">
              <h2 className="text-2xl font-bold text-gray-900">
                Generated MCQs - Week {selectedWeek}
              </h2>
              <span className="ml-auto bg-gray-100 text-gray-700 px-4 py-2 rounded-full font-semibold text-sm">
                {generatedMCQs.length} Questions
              </span>
            </div>
            
            <div className="space-y-6">
              {generatedMCQs.map((mcq, index) => (
                <div 
                  key={index} 
                  className="bg-gray-50 border-l-4 border-gray-700 rounded-lg p-6 shadow-sm hover:shadow-md transition-all duration-200"
                >
                  {/* Question Header */}
                  <div className="flex items-start justify-between mb-4">
                    <div className="flex-1">
                      <div className="flex items-center gap-2 mb-2">
                        <span className="flex items-center justify-center w-8 h-8 bg-blue-600 text-white font-bold rounded-full text-sm">
                          {index + 1}
                        </span>
                        {mcq.topic_name && (
                          <span className="px-3 py-1 bg-gray-200 text-gray-700 rounded-full text-xs font-semibold">
                            {mcq.topic_name}
                          </span>
                        )}
                        {mcq.difficulty_level && (
                          <span className={`px-3 py-1 rounded-full text-xs font-semibold border ${getDifficultyColor(mcq.difficulty_level)}`}>
                            {mcq.difficulty_level}
                          </span>
                        )}
                      </div>
                      <p className="text-lg font-semibold text-gray-900 leading-relaxed">
                        {mcq.question}
                      </p>
                    </div>
                  </div>

                  {/* Answer Options */}
                  <div className="space-y-3 ml-2">
                    {/* Correct Answer */}
                    <div className="flex items-start gap-3 p-4 bg-white border border-gray-300 rounded-lg">
                      <CheckCircle2 className="w-5 h-5 text-gray-700 flex-shrink-0 mt-0.5" />
                      <p className="text-gray-900 font-medium">{mcq.answer}</p>
                    </div>
                    
                    {/* Distractors */}
                    {mcq.distractors.map((distractor, idx) => (
                      <div key={idx} className="flex items-start gap-3 p-4 bg-white border border-gray-200 rounded-lg">
                        <XCircle className="w-5 h-5 text-gray-400 flex-shrink-0 mt-0.5" />
                        <p className="text-gray-700">{distractor}</p>
                      </div>
                    ))}
                  </div>

                  {/* Explanation */}
                  {mcq.explanation && (
                    <div className="mt-4 p-4 bg-gray-100 border-l-4 border-gray-400 rounded-lg">
                      <p className="text-sm text-gray-700">
                        <span className="font-semibold text-gray-900">💡 Explanation: </span>
                        {mcq.explanation}
                      </p>
                    </div>
                  )}
                </div>
              ))}
            </div>
          </div>
        )}

        {/* MCQ Upload Modal */}
        {showMCQUpload && (
          <div className="fixed inset-0 bg-black bg-opacity-50 z-50 flex items-center justify-center p-4">
            <div className="bg-white rounded-2xl shadow-2xl w-full max-w-2xl animate-in zoom-in-95 duration-200">
              <div className="flex items-center justify-between p-6 border-b border-gray-200">
                <h3 className="text-2xl font-bold text-gray-900">Add Collected MCQs</h3>
                <button
                  onClick={() => {
                    setShowMCQUpload(false)
                    setMcqFile(null)
                    setUploadedMCQs([])
                  }}
                  className="p-2 hover:bg-gray-100 rounded-lg transition-all"
                >
                  <XCircle className="w-6 h-6 text-gray-600" />
                </button>
              </div>
              
              <div className="p-6 space-y-6">
                <div>
                  <label className="block text-sm font-semibold text-gray-700 mb-3 uppercase tracking-wide">
                    Upload MCQs JSON File
                  </label>
                  <div className="relative">
                    <input
                      type="file"
                      accept=".json"
                      className="w-full px-5 py-4 border-2 border-dashed border-gray-300 rounded-xl hover:border-gray-400 transition-all cursor-pointer file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-gray-100 file:text-gray-700 hover:file:bg-gray-200"
                      onChange={handleMCQFileChange}
                    />
                  </div>
                  {mcqFile && uploadedMCQs.length > 0 && (
                    <div className="mt-3 flex items-center gap-2 p-4 bg-gray-50 border border-gray-200 rounded-lg">
                      <CheckCircle2 className="w-5 h-5 text-gray-700" />
                      <div className="flex-1">
                        <p className="text-sm text-gray-700 font-medium">
                          {mcqFile.name}
                        </p>
                        <p className="text-xs text-gray-600">
                          {uploadedMCQs.length} MCQs loaded
                        </p>
                      </div>
                    </div>
                  )}
                </div>

                <div className="bg-gray-100 border-l-4 border-gray-400 p-4 rounded-lg">
                  <p className="text-sm text-gray-800">
                    <span className="font-semibold">ℹ️ Note:</span> Upload a JSON file containing MCQs in the format:
                  </p>
                  <pre className="mt-2 text-xs text-gray-800 bg-white p-3 rounded border border-gray-300 overflow-x-auto">
{`[
  {
    "question": "Question text?",
    "options": {
      "A": "Option 1",
      "B": "Option 2"
    },
    "answer": "Correct answer",
    "explanation": "Explanation text"
  }
]`}
                  </pre>
                </div>

                <button
                  onClick={handleMCQUpload}
                  disabled={!mcqFile || uploadedMCQs.length === 0}
                  className="w-full flex items-center justify-center gap-3 py-4 px-6 bg-blue-600 text-white font-semibold rounded-lg hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed shadow-md transition-all duration-200"
                >
                  <Upload className="w-5 h-5" />
                  Upload MCQs
                </button>
              </div>
            </div>
          </div>
        )}

        {/* Index Confirmation Modal */}
        {showIndexModal && (
          <div className="fixed inset-0 bg-black bg-opacity-50 z-[60] flex items-center justify-center p-4">
            <div className="bg-white rounded-xl shadow-xl w-full max-w-lg animate-in zoom-in-95 duration-200">
              <div className="flex items-center justify-between p-6 border-b border-gray-200">
                <h3 className="text-2xl font-bold text-gray-900">Confirm Indexing</h3>
              </div>
              
              <div className="p-6 space-y-4">
                <div className="bg-gray-50 border-l-4 border-gray-700 p-4 rounded-lg">
                  <p className="text-sm text-gray-800">
                    You are about to index <span className="font-bold">{uploadedMCQs.length} MCQs</span> to the vector database for:
                  </p>
                  <div className="mt-3">
                    <p className="text-sm font-semibold text-gray-900">
                      📚 Course: <span className="text-gray-700">{courseCode.toUpperCase()}</span>
                    </p>
                  </div>
                </div>

                <p className="text-sm text-gray-700">
                  This will make the MCQs searchable and available in the chatbot for student queries. 
                  This process may take a few moments.
                </p>

                <div className="flex gap-3 pt-4">
                  <button
                    onClick={() => setShowIndexModal(false)}
                    disabled={indexMutation.isPending}
                    className="flex-1 py-3 px-4 bg-gray-100 text-gray-700 font-semibold rounded-lg hover:bg-gray-200 disabled:opacity-50 disabled:cursor-not-allowed transition-all duration-200"
                  >
                    Cancel
                  </button>
                  <button
                    onClick={handleConfirmIndex}
                    disabled={indexMutation.isPending}
                    className="flex-1 py-3 px-4 bg-blue-600 text-white font-semibold rounded-lg hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed shadow-md transition-all duration-200 flex items-center justify-center gap-2"
                  >
                    {indexMutation.isPending ? (
                      <>
                        <Loader2 className="w-5 h-5 animate-spin" />
                        Indexing...
                      </>
                    ) : (
                      <>
                        <Database className="w-5 h-5" />
                        Index to Database
                      </>
                    )}
                  </button>
                </div>
              </div>
            </div>
          </div>
        )}

        {/* Book Upload Modal */}
        {showBookUpload && (
          <div className="fixed inset-0 bg-black bg-opacity-50 z-50 flex items-center justify-center p-4">
            <div className="bg-white rounded-xl shadow-xl w-full max-w-2xl animate-in zoom-in-95 duration-200">
              <div className="flex items-center justify-between p-6 border-b border-gray-200">
                <h3 className="text-2xl font-bold text-gray-900">Add Book to Graph Database</h3>
                <button
                  onClick={() => {
                    setShowBookUpload(false)
                    setBookFile(null)
                  }}
                  className="p-2 hover:bg-gray-100 rounded-lg transition-all"
                >
                  <XCircle className="w-6 h-6 text-gray-600" />
                </button>
              </div>
              
              <div className="p-6 space-y-6">
                <div>
                  <label className="block text-sm font-semibold text-gray-700 mb-3 uppercase tracking-wide">
                    Upload Book File
                  </label>
                  <div className="relative">
                    <input
                      type="file"
                      accept=".pdf,.txt,.doc,.docx"
                      className="w-full px-5 py-4 border-2 border-dashed border-gray-300 rounded-xl hover:border-cyan-400 transition-all cursor-pointer file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-cyan-50 file:text-cyan-700 hover:file:bg-cyan-100"
                      onChange={handleBookFileChange}
                    />
                  </div>
                  {bookFile && (
                    <div className="mt-3 flex items-center gap-2 p-4 bg-gray-50 border border-gray-200 rounded-lg">
                      <CheckCircle2 className="w-5 h-5 text-gray-700" />
                      <div className="flex-1">
                        <p className="text-sm text-gray-700 font-medium">
                          {bookFile.name}
                        </p>
                        <p className="text-xs text-gray-600">
                          {(bookFile.size / 1024 / 1024).toFixed(2)} MB
                        </p>
                      </div>
                    </div>
                  )}
                </div>

                <div className="bg-gray-100 border-l-4 border-gray-400 p-4 rounded-lg">
                  <p className="text-sm text-gray-800">
                    <span className="font-semibold">ℹ️ Note:</span> Upload a book file (PDF, TXT, DOC, DOCX) to be indexed into the knowledge graph database. This will enable semantic search and relationship mapping.
                  </p>
                </div>

                <button
                  onClick={handleBookUpload}
                  disabled={!bookFile}
                  className="w-full flex items-center justify-center gap-3 py-4 px-6 bg-blue-600 text-white font-semibold rounded-lg hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed shadow-md transition-all duration-200"
                >
                  <Upload className="w-5 h-5" />
                  Index Book
                </button>
              </div>
            </div>
          </div>
        )}

        {/* Graph Index Confirmation Modal */}
        {showGraphIndexModal && (
          <div className="fixed inset-0 bg-black bg-opacity-50 z-[60] flex items-center justify-center p-4">
            <div className="bg-white rounded-xl shadow-xl w-full max-w-lg animate-in zoom-in-95 duration-200">
              <div className="flex items-center justify-between p-6 border-b border-gray-200">
                <h3 className="text-2xl font-bold text-gray-900">Confirm Graph Indexing</h3>
              </div>
              
              <div className="p-6 space-y-4">
                <div className="bg-gray-50 border-l-4 border-gray-700 p-4 rounded-lg">
                  <p className="text-sm text-gray-800">
                    You are about to index <span className="font-bold">{bookFile?.name}</span> to the knowledge graph database for:
                  </p>
                  <div className="mt-3">
                    <p className="text-sm font-semibold text-gray-900">
                      📚 Course: <span className="text-gray-700">{courseCode.toUpperCase()}</span>
                    </p>
                  </div>
                </div>

                <p className="text-sm text-gray-700">
                  This will extract entities, relationships, and concepts from the book to build a knowledge graph. 
                  This process may take several minutes depending on the file size.
                </p>

                <div className="flex gap-3 pt-4">
                  <button
                    onClick={() => setShowGraphIndexModal(false)}
                    disabled={graphIndexMutation.isPending}
                    className="flex-1 py-3 px-4 bg-gray-100 text-gray-700 font-semibold rounded-lg hover:bg-gray-200 disabled:opacity-50 disabled:cursor-not-allowed transition-all duration-200"
                  >
                    Cancel
                  </button>
                  <button
                    onClick={handleConfirmGraphIndex}
                    disabled={graphIndexMutation.isPending}
                    className="flex-1 py-3 px-4 bg-blue-600 text-white font-semibold rounded-lg hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed shadow-md transition-all duration-200 flex items-center justify-center gap-2"
                  >
                    {graphIndexMutation.isPending ? (
                      <>
                        <Loader2 className="w-5 h-5 animate-spin" />
                        Indexing...
                      </>
                    ) : (
                      <>
                        <BookOpen className="w-5 h-5" />
                        Index to Graph
                      </>
                    )}
                  </button>
                </div>
              </div>
            </div>
          </div>
        )}

        {/* New Week Upload Modal */}
        {showNewWeekUpload && (
          <div className="fixed inset-0 bg-black bg-opacity-50 z-50 flex items-center justify-center p-4">
            <div className="bg-white rounded-xl shadow-xl w-full max-w-2xl animate-in zoom-in-95 duration-200">
              <div className="flex items-center justify-between p-6 border-b border-gray-200">
                <h3 className="text-2xl font-bold text-gray-900">Upload Lecture - Week {newWeekNumber}</h3>
                <button
                  onClick={() => {
                    setShowNewWeekUpload(false)
                    setUploadFile(null)
                  }}
                  className="p-2 hover:bg-gray-100 rounded-lg transition-all"
                >
                  <XCircle className="w-6 h-6 text-gray-600" />
                </button>
              </div>
              
              <div className="p-6 space-y-6">
                <div>
                  <label className="block text-sm font-semibold text-gray-700 mb-3 uppercase tracking-wide">
                    Select Lecture File
                  </label>
                  <div className="relative">
                    <input
                      type="file"
                      accept=".pdf,.doc,.docx,.txt,.ppt,.pptx"
                      className="w-full px-5 py-4 border-2 border-dashed border-gray-300 rounded-xl hover:border-green-400 transition-all cursor-pointer file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-green-50 file:text-green-700 hover:file:bg-green-100"
                      onChange={(e) => setUploadFile(e.target.files?.[0] || null)}
                    />
                  </div>
                  {uploadFile && (
                    <div className="mt-3 flex items-center gap-2 p-4 bg-green-50 border border-green-200 rounded-lg">
                      <CheckCircle2 className="w-5 h-5 text-green-600" />
                      <div className="flex-1">
                        <p className="text-sm text-gray-700 font-medium">
                          {uploadFile.name}
                        </p>
                        <p className="text-xs text-gray-600">
                          {(uploadFile.size / 1024 / 1024).toFixed(2)} MB
                        </p>
                      </div>
                    </div>
                  )}
                </div>

                <div className="bg-gray-100 border-l-4 border-gray-400 p-4 rounded-lg">
                  <p className="text-sm text-gray-800">
                    <span className="font-semibold">ℹ️ Note:</span> This will create Week {newWeekNumber} with your uploaded lecture file.
                  </p>
                </div>

                <button
                  onClick={handleNewWeekFileUpload}
                  disabled={!uploadFile || uploadMutation.isPending}
                  className="w-full flex items-center justify-center gap-3 py-4 px-6 bg-blue-600 text-white font-semibold rounded-lg hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed shadow-md transition-all duration-200"
                >
                  {uploadMutation.isPending ? (
                    <>
                      <Loader2 className="w-5 h-5 animate-spin" />
                      Uploading...
                    </>
                  ) : (
                    <>
                      <Upload className="w-5 h-5" />
                      Upload & Create Week {newWeekNumber}
                    </>
                  )}
                </button>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  )
}
