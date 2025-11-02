import { create } from 'zustand'
import { persist } from 'zustand/middleware'
import axios from 'axios'

interface User {
  user_id: number
  user_name: string
  email: string
  full_name?: string
  teaching_courses?: string[]
}

interface AuthState {
  user: User | null
  isAuthenticated: boolean
  login: (username: string, password: string) => Promise<void>
  register: (data: RegisterData) => Promise<void>
  logout: () => void
  setUser: (user: User) => void
}

interface RegisterData {
  user_name: string
  email: string
  password: string
  full_name?: string
}

export const useAuthStore = create<AuthState>()(
  persist(
    (set) => ({
      user: null,
      isAuthenticated: false,

      login: async (username: string, password: string) => {
        // Send in format expected by FastAPI with Depends()
        const response = await axios.post('http://localhost:3001/api/auth/login', {
          user_name: username,
          password: password
        })
        
        const { user } = response.data

        set({
          user: user,
          isAuthenticated: true,
        })
      },

      register: async (data: RegisterData) => {
        await axios.post('http://localhost:3001/api/auth/register', data)
      },

      logout: () => {
        set({
          user: null,
          isAuthenticated: false,
        })
      },

      setUser: (user: User) => {
        set({ user })
      },
    }),
    {
      name: 'auth-storage',
    }
  )
)
