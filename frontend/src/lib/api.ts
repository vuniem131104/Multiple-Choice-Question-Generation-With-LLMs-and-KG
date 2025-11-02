import axios from 'axios'

const BASE_URL = 'http://localhost:3002'

export const api = axios.create({
  baseURL: BASE_URL,
})

// MCQ API
export const mcqApi = {
  saveMCQs: (questions: any[]) =>
    api.post('/api/mcq/questions', questions),
  
  getMCQsByWeek: (courseCode: string, weekNumber: number) =>
    api.get(`/api/mcq/questions/${courseCode}/${weekNumber}`),
  
  getMCQById: (mcqId: number) =>
    api.get(`/api/mcq/questions/${mcqId}`),
}

// Activity API
export const activityApi = {
  logActivity: (data: {
    type_activity: string
    course_code: string
    week_number: number
    user_id: number
  }) => api.post('/api/activities/log', data),
  
  completeActivity: (data: {
    activity_id: number
    status: string
  }) => api.put('/api/activities/complete', data),
  
  getMyLogs: (userId: number, limit = 50) =>
    api.get(`/api/activities/user/${userId}?limit=${limit}`),
  
  getCourseActivities: (courseCode: string) =>
    api.get(`/api/activities/course/${courseCode}`),
}

// Student History API
export const historyApi = {
  submitAttempt: (data: {
    student_id: number
    course_code: string
    week_number: number
    mcq_id: number
    student_answer: string
  }) => api.post('/api/history/attempt', data),
  
  getMyHistory: (studentId: number, limit = 50) =>
    api.get(`/api/history/student/${studentId}?limit=${limit}`),
  
  getPerformance: (studentId: number, courseCode: string) =>
    api.get(`/api/history/performance/${studentId}/${courseCode}`),
}

// Generation API (existing service)
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
}
