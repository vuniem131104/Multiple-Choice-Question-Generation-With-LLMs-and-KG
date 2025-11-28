import axios from 'axios'

export const generationApi = {
  generateQuiz: (data: {
    course_code: string
    week_number: number
    number_of_topics: number
    common_mistakes?: string[]
  }) => axios.post('http://localhost:3005/generate_quiz', data),
  
  listLectures: (courseCode: string) =>
    axios.get('http://localhost:3005/lectures', {
      params: { course_code: courseCode }
    }),
  
  getLectureDownloadUrl: (bucket: string, filePath: string) =>
    `http://localhost:3005/lectures/download?bucket=${encodeURIComponent(bucket)}&file_path=${encodeURIComponent(filePath)}`,
  
  indexMCQs: (data: {
    mcqs: any[]
    course_code: string
  }) => axios.post('http://localhost:3005/index_mcqs', data),

  uploadFile: async (file: File, courseCode: string) => {
    const formData = new FormData()
    formData.append('file', file)
    formData.append('course_code', courseCode)
    return axios.post('http://localhost:3005/upload', formData)
  },
}
