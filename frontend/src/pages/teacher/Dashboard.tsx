import { useState, useEffect } from 'react'
import { useMutation, useQuery } from '@tanstack/react-query'
import { generationApi } from '@/lib/api'
import { useAuthStore } from '@/stores/authStore'
import toast from 'react-hot-toast'
import { BookOpen, Upload, Loader2, Plus, CheckCircle2, XCircle, Trash2, Sparkles, FileText, Eye } from 'lucide-react'

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
  const [weeks, setWeeks] = useState<number[]>([1])
  const [showTopicSelector, setShowTopicSelector] = useState(false)
  const [numberOfTopics, setNumberOfTopics] = useState(5)
  const [selectedPdf, setSelectedPdf] = useState<string | null>(null)

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
      const formData = new FormData()
      formData.append('file', data.file)
      formData.append('course_code', data.course_code)
      formData.append('week_number', data.week_number.toString())

      const response = await fetch('http://localhost:3005/upload', {
        method: 'POST',
        body: formData,
      })

      if (!response.ok) {
        throw new Error('Failed to upload file')
      }

      return response.json()
    },
    onSuccess: () => {
      toast.success('Lecture uploaded successfully!')
      setUploadFile(null)
      setShowUpload(false)
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

  const addWeek = () => {
    const nextWeek = weeks.length > 0 ? Math.max(...weeks) + 1 : 1
    setWeeks([...weeks, nextWeek])
  }

  const removeWeek = (weekNumber: number) => {
    if (weeks.length <= 1) {
      toast.error('You must have at least one week')
      return
    }
    setWeeks(weeks.filter(w => w !== weekNumber))
    if (selectedWeek === weekNumber) {
      setSelectedWeek(null)
      setShowUpload(false)
      setGeneratedMCQs([])
    }
  }

  const getDifficultyColor = (difficulty?: string) => {
    switch (difficulty?.toLowerCase()) {
      case 'easy':
        return 'bg-green-100 text-green-800 border-green-200'
      case 'medium':
        return 'bg-yellow-100 text-yellow-800 border-yellow-200'
      case 'hard':
        return 'bg-red-100 text-red-800 border-red-200'
      default:
        return 'bg-gray-100 text-gray-800 border-gray-200'
    }
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-indigo-50 to-purple-50 p-6">
      <div className="max-w-7xl mx-auto">
        {/* Header */}
        <div className="mb-8 text-center">
          <div className="flex items-center justify-center gap-3 mb-3">
            <Sparkles className="w-8 h-8 text-indigo-600" />
            <h1 className="text-4xl font-bold bg-gradient-to-r from-blue-600 via-indigo-600 to-purple-600 bg-clip-text text-transparent">
              Teacher Dashboard
            </h1>
          </div>
          <p className="text-gray-600 text-lg">Upload lectures and generate intelligent MCQs for your courses</p>
        </div>

        {/* Course Selector */}
        <div className="bg-white rounded-2xl shadow-lg p-8 mb-8 border border-indigo-100">
          <label className="block text-sm font-semibold text-gray-700 mb-3 uppercase tracking-wide">
            Select Course
          </label>
          {user?.teaching_courses && user.teaching_courses.length > 0 ? (
            <div className="flex flex-wrap gap-3">
              {user.teaching_courses.map((course) => (
                <button
                  key={course}
                  onClick={() => setCourseCode(course)}
                  className={`px-6 py-3 rounded-xl font-semibold transition-all duration-200 transform hover:scale-[1.02] ${
                    courseCode === course
                      ? 'bg-gradient-to-r from-blue-600 via-indigo-600 to-purple-600 text-white shadow-lg'
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
          <div className="bg-white rounded-2xl shadow-lg p-8 mb-8 border border-indigo-100">
            <div className="flex items-center justify-between mb-6">
              <h2 className="text-2xl font-bold text-gray-900 flex items-center gap-3">
                <FileText className="w-7 h-7 text-indigo-600" />
                My Lectures - {courseCode.toUpperCase()}
              </h2>
              <div className="flex items-center gap-3">
                <button
                  onClick={addWeek}
                  className="flex items-center gap-2 px-5 py-2.5 bg-gradient-to-r from-indigo-600 to-purple-600 text-white font-semibold rounded-xl hover:from-indigo-700 hover:to-purple-700 shadow-lg hover:shadow-xl transition-all duration-200 transform hover:scale-[1.02]"
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
                
                // Combine existing weeks with manually added weeks
                const allWeeks = Array.from(new Set([...existingWeeks, ...weeks])).sort((a, b) => a - b)
                
                return allWeeks.length > 0 ? (
                  <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                    {allWeeks.map((week) => {
                      // Find lectures for this week
                      const weekLectures = lecturesData?.courses
                        ?.find((course: CourseData) => course.course_code.toLowerCase() === courseCode.toLowerCase())
                        ?.weeks.find((w: WeekData) => w.week_number === week)?.files || []

                      const hasLectures = weekLectures.length > 0

                      return (
                        <div
                          key={week}
                          className="relative border-2 border-gray-200 rounded-2xl p-6 hover:shadow-xl hover:border-indigo-300 transition-all duration-200 bg-gradient-to-br from-white to-gray-50 group"
                        >
                          {/* Delete Week Button - only for manually added weeks without lectures */}
                          {!hasLectures && weeks.includes(week) && weeks.length > 1 && (
                            <button
                              onClick={() => removeWeek(week)}
                              className="absolute top-3 right-3 p-1.5 text-gray-400 hover:text-red-600 hover:bg-red-50 rounded-lg transition-all opacity-0 group-hover:opacity-100"
                              title="Remove week"
                            >
                              <Trash2 className="w-4 h-4" />
                            </button>
                          )}

                          <div className="flex items-center justify-between mb-4">
                            <h3 className="text-xl font-bold text-gray-900">Week {week}</h3>
                            <div className={`p-2 rounded-lg ${hasLectures ? 'bg-green-100' : 'bg-indigo-100'}`}>
                              <BookOpen className={`w-6 h-6 ${hasLectures ? 'text-green-600' : 'text-indigo-600'}`} />
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
                                  className="w-full flex items-center gap-2 p-3 bg-green-50 hover:bg-green-100 border border-green-200 rounded-lg transition-all text-left group/file"
                                >
                                  <FileText className="w-4 h-4 text-green-600 flex-shrink-0" />
                                  <span className="flex-1 text-sm text-gray-800 font-medium truncate">
                                    {file.file_name}
                                  </span>
                                  <Eye className="w-4 h-4 text-green-600 flex-shrink-0" />
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
                                className="w-full py-3 px-4 bg-gradient-to-r from-green-500 to-emerald-500 text-white font-semibold rounded-xl hover:from-green-600 hover:to-emerald-600 disabled:opacity-50 disabled:cursor-not-allowed shadow-md hover:shadow-lg transition-all duration-200 transform hover:scale-[1.02] flex items-center justify-center gap-2"
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
                                className="w-full py-3 px-4 bg-gradient-to-r from-blue-500 to-indigo-500 text-white font-semibold rounded-xl hover:from-blue-600 hover:to-indigo-600 disabled:opacity-50 disabled:cursor-not-allowed shadow-md hover:shadow-lg transition-all duration-200 transform hover:scale-[1.02] flex items-center justify-center gap-2"
                              >
                                {generateMutation.isPending && selectedWeek === week ? (
                                  <>
                                    <Loader2 className="w-4 h-4 animate-spin" />
                                    Generating...
                                  </>
                                ) : (
                                  <>
                                    <Sparkles className="w-4 h-4" />
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
          <div className="bg-white rounded-2xl shadow-xl p-8 mb-8 border-2 border-purple-200 animate-in slide-in-from-top duration-300">
            <div className="flex items-center justify-between mb-6">
              <div className="flex items-center gap-3">
                <div className="bg-gradient-to-r from-purple-500 to-pink-500 p-3 rounded-xl">
                  <Sparkles className="w-6 h-6 text-white" />
                </div>
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
                    className="flex-1 h-3 bg-gradient-to-r from-purple-200 to-pink-200 rounded-lg appearance-none cursor-pointer
                      [&::-webkit-slider-thumb]:appearance-none [&::-webkit-slider-thumb]:w-6 [&::-webkit-slider-thumb]:h-6 
                      [&::-webkit-slider-thumb]:rounded-full [&::-webkit-slider-thumb]:bg-gradient-to-r 
                      [&::-webkit-slider-thumb]:from-purple-600 [&::-webkit-slider-thumb]:to-pink-600 
                      [&::-webkit-slider-thumb]:cursor-pointer [&::-webkit-slider-thumb]:shadow-lg
                      [&::-moz-range-thumb]:w-6 [&::-moz-range-thumb]:h-6 [&::-moz-range-thumb]:rounded-full 
                      [&::-moz-range-thumb]:bg-gradient-to-r [&::-moz-range-thumb]:from-purple-600 
                      [&::-moz-range-thumb]:to-pink-600 [&::-moz-range-thumb]:cursor-pointer 
                      [&::-moz-range-thumb]:border-0 [&::-moz-range-thumb]:shadow-lg"
                  />
                  <div className="flex items-center justify-center w-16 h-16 bg-gradient-to-r from-purple-600 to-pink-600 text-white text-2xl font-bold rounded-xl shadow-lg">
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
                className="w-full flex items-center justify-center gap-3 py-4 px-6 bg-gradient-to-r from-purple-600 to-pink-600 text-white font-semibold rounded-xl hover:from-purple-700 hover:to-pink-700 disabled:opacity-50 disabled:cursor-not-allowed shadow-lg hover:shadow-xl transition-all duration-200 transform hover:scale-[1.02]"
              >
                {generateMutation.isPending ? (
                  <>
                    <Loader2 className="w-5 h-5 animate-spin" />
                    Generating MCQs...
                  </>
                ) : (
                  <>
                    <Sparkles className="w-5 h-5" />
                    Generate {numberOfTopics} {numberOfTopics === 1 ? 'Topic' : 'Topics'}
                  </>
                )}
              </button>
            </div>
          </div>
        )}

        {/* Upload Section */}
        {showUpload && selectedWeek && (
          <div className="bg-white rounded-2xl shadow-xl p-8 mb-8 border-2 border-indigo-200 animate-in slide-in-from-top duration-300">
            <div className="flex items-center justify-between mb-6">
              <div className="flex items-center gap-3">
                <div className="bg-gradient-to-r from-green-500 to-emerald-500 p-3 rounded-xl">
                  <Upload className="w-6 h-6 text-white" />
                </div>
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
                    className="w-full px-5 py-4 border-2 border-dashed border-gray-300 rounded-xl hover:border-indigo-400 transition-all cursor-pointer file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-indigo-50 file:text-indigo-700 hover:file:bg-indigo-100"
                    onChange={(e) => setUploadFile(e.target.files?.[0] || null)}
                  />
                </div>
                {uploadFile && (
                  <div className="mt-3 flex items-center gap-2 p-3 bg-indigo-50 border border-indigo-200 rounded-lg">
                    <CheckCircle2 className="w-5 h-5 text-indigo-600" />
                    <p className="text-sm text-gray-700 font-medium">
                      {uploadFile.name} <span className="text-gray-500">({(uploadFile.size / 1024 / 1024).toFixed(2)} MB)</span>
                    </p>
                  </div>
                )}
              </div>

              <button
                onClick={handleFileUpload}
                disabled={!uploadFile || uploadMutation.isPending}
                className="w-full flex items-center justify-center gap-3 py-4 px-6 bg-gradient-to-r from-green-600 to-emerald-600 text-white font-semibold rounded-xl hover:from-green-700 hover:to-emerald-700 disabled:opacity-50 disabled:cursor-not-allowed shadow-lg hover:shadow-xl transition-all duration-200 transform hover:scale-[1.02]"
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
          <div className="bg-white rounded-2xl shadow-xl p-8 mb-8 border-2 border-purple-200">
            <div className="flex items-center gap-3 mb-6">
              <div className="bg-gradient-to-r from-purple-500 to-pink-500 p-3 rounded-xl">
                <Sparkles className="w-6 h-6 text-white" />
              </div>
              <h2 className="text-2xl font-bold text-gray-900">
                Generated MCQs - Week {selectedWeek}
              </h2>
              <span className="ml-auto bg-purple-100 text-purple-700 px-4 py-2 rounded-full font-semibold text-sm">
                {generatedMCQs.length} Questions
              </span>
            </div>
            
            <div className="space-y-6">
              {generatedMCQs.map((mcq, index) => (
                <div 
                  key={index} 
                  className="bg-gradient-to-r from-white to-indigo-50 border-l-4 border-indigo-500 rounded-xl p-6 shadow-md hover:shadow-lg transition-all duration-200"
                >
                  {/* Question Header */}
                  <div className="flex items-start justify-between mb-4">
                    <div className="flex-1">
                      <div className="flex items-center gap-2 mb-2">
                        <span className="flex items-center justify-center w-8 h-8 bg-indigo-600 text-white font-bold rounded-full text-sm">
                          {index + 1}
                        </span>
                        {mcq.topic_name && (
                          <span className="px-3 py-1 bg-blue-100 text-blue-700 rounded-full text-xs font-semibold">
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
                    <div className="flex items-start gap-3 p-4 bg-green-50 border-2 border-green-200 rounded-lg">
                      <CheckCircle2 className="w-5 h-5 text-green-600 flex-shrink-0 mt-0.5" />
                      <p className="text-gray-900 font-medium">{mcq.answer}</p>
                    </div>
                    
                    {/* Distractors */}
                    {mcq.distractors.map((distractor, idx) => (
                      <div key={idx} className="flex items-start gap-3 p-4 bg-gray-50 border-2 border-gray-200 rounded-lg">
                        <XCircle className="w-5 h-5 text-gray-400 flex-shrink-0 mt-0.5" />
                        <p className="text-gray-700">{distractor}</p>
                      </div>
                    ))}
                  </div>

                  {/* Explanation */}
                  {mcq.explanation && (
                    <div className="mt-4 p-4 bg-amber-50 border-l-4 border-amber-400 rounded-lg">
                      <p className="text-sm text-gray-700">
                        <span className="font-semibold text-amber-700">💡 Explanation: </span>
                        {mcq.explanation}
                      </p>
                    </div>
                  )}
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  )
}
