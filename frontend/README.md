# Educational Platform - Frontend

Modern React application for the Educational Platform MCQ system.

## Features

- 🎨 **Modern UI** with TailwindCSS
- 🔐 **JWT Authentication** with token refresh
- 📱 **Responsive Design** for mobile and desktop
- ⚡ **Fast Development** with Vite and Hot Module Replacement
- 🎯 **Type Safety** with TypeScript
- 🔄 **Smart Data Fetching** with TanStack Query
- 🗂️ **State Management** with Zustand
- 🎭 **Role-Based Views** for teachers and students

## Tech Stack

- **React 18** - UI library
- **TypeScript** - Type safety
- **Vite** - Build tool
- **TailwindCSS** - Styling
- **React Router** - Client-side routing
- **TanStack Query** - Server state management
- **Zustand** - Client state management
- **Axios** - HTTP client
- **React Hot Toast** - Toast notifications
- **Lucide React** - Icon library

## Getting Started

### Prerequisites

- Node.js 18+ (LTS recommended)
- npm or yarn

### Installation

```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Open http://localhost:3000
```

### Build for Production

```bash
# Create optimized production build
npm run build

# Preview production build
npm run preview
```

## Project Structure

```
frontend/
├── public/              # Static assets
├── src/
│   ├── components/      # Reusable UI components
│   │   └── Layout.tsx  # Main layout with navigation
│   ├── pages/          # Page components
│   │   ├── LoginPage.tsx
│   │   ├── RegisterPage.tsx
│   │   ├── teacher/    # Teacher-specific pages
│   │   │   └── TeacherDashboard.tsx
│   │   └── student/    # Student-specific pages
│   │       └── StudentDashboard.tsx
│   ├── stores/         # Zustand stores
│   │   └── authStore.ts
│   ├── lib/            # Utilities
│   │   └── api.ts      # API client
│   ├── App.tsx         # Root component
│   ├── main.tsx        # Entry point
│   └── index.css       # Global styles
├── index.html
├── package.json
├── tsconfig.json
├── vite.config.ts
└── tailwind.config.js
```

## Configuration

### Environment Variables

The frontend uses proxying for API calls. Configure in `vite.config.ts`:

```typescript
server: {
  port: 3000,
  proxy: {
    '/api': {
      target: 'http://localhost:3002',
      changeOrigin: true,
    },
  },
}
```

### API Endpoints

API base URLs are configured in `src/lib/api.ts`:

```typescript
// Auth Service
http://localhost:3001/api/auth/*

// Platform API
http://localhost:3002/api/*

// Generation Service
http://localhost:3005/generate_quiz
```

## Development

### Available Scripts

```bash
npm run dev      # Start development server
npm run build    # Build for production
npm run preview  # Preview production build
npm run lint     # Lint code
```

### Code Style

- Use TypeScript for type safety
- Follow React best practices
- Use functional components with hooks
- Prefer composition over inheritance
- Keep components small and focused

### Adding New Pages

1. Create component in `src/pages/`
2. Add route in `src/App.tsx`
3. Protect route if needed with `PrivateRoute`

Example:
```typescript
<Route path="/teacher/new-feature" element={
  <PrivateRoute requiredRole="teacher">
    <Layout>
      <NewFeaturePage />
    </Layout>
  </PrivateRoute>
} />
```

### Adding New API Calls

Add functions in `src/lib/api.ts`:

```typescript
export const myApi = {
  getData: () => api.get('/api/my-endpoint'),
  postData: (data: any) => api.post('/api/my-endpoint', data),
}
```

Use with TanStack Query:
```typescript
const { data, isLoading } = useQuery({
  queryKey: ['my-data'],
  queryFn: async () => {
    const res = await myApi.getData()
    return res.data
  },
})
```

## Features Guide

### Teacher Dashboard

**Generate MCQs**
- Input course code, week number, number of topics
- Triggers AI generation
- Automatically logs activity
- Saves questions to database

**Activity Logs**
- View all generation activities
- Filter by course/week
- See timestamps and status

**View MCQs**
- Browse generated questions
- Filter by course and week
- See all question details

### Student Dashboard

**Practice Quiz**
- Select course and week
- Answer MCQs interactively
- Get instant feedback
- View explanations

**My History**
- See all past attempts
- Review correct/incorrect answers
- Track improvement

**Performance**
- View statistics by course
- See accuracy percentages
- Track progress over time

## Authentication Flow

1. User logs in → JWT tokens stored in Zustand + localStorage
2. Axios interceptor adds token to all requests
3. Protected routes check authentication
4. Token refresh on expiry
5. Logout clears all tokens

## State Management

### Auth State (Zustand)

```typescript
const { user, login, logout, isAuthenticated } = useAuthStore()
```

### Server State (TanStack Query)

```typescript
const { data, isLoading, error, refetch } = useQuery({
  queryKey: ['key'],
  queryFn: fetchFunction,
})
```

## Styling

### TailwindCSS Classes

Common patterns used:
- Layout: `flex`, `grid`, `space-x-4`, `gap-4`
- Spacing: `p-4`, `m-4`, `px-6`, `py-2`
- Colors: `bg-blue-600`, `text-gray-900`, `border-gray-300`
- Responsive: `md:grid-cols-3`, `lg:px-8`

### Custom Classes

Defined in `tailwind.config.js`:
```javascript
theme: {
  extend: {
    colors: {
      primary: { ... },
    },
  },
}
```

## Testing

### Manual Testing

1. **Login Flow**
   - Test teacher and student logins
   - Verify token persistence
   - Check role-based redirects

2. **Teacher Features**
   - Generate MCQs
   - View activity logs
   - Browse questions

3. **Student Features**
   - Take quizzes
   - Submit answers
   - View history
   - Check performance

## Troubleshooting

### Build Errors

```bash
# Clear cache and reinstall
rm -rf node_modules package-lock.json
npm install
```

### TypeScript Errors

```bash
# Check TypeScript configuration
npx tsc --noEmit
```

### API Connection Issues

- Check backend services are running
- Verify proxy configuration in `vite.config.ts`
- Check CORS settings in backend

### Hot Reload Not Working

```bash
# Restart dev server
npm run dev
```

## Browser Support

- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers (iOS Safari, Chrome Android)

## Performance Optimization

- Code splitting with React.lazy()
- Image optimization
- Bundle size monitoring
- React Query caching
- Debounced searches
- Virtualized lists for large datasets

## Security

- XSS protection via React's JSX
- CSRF tokens for sensitive operations
- JWT token in memory + localStorage
- Input validation
- Sanitized API responses

## Contributing

1. Follow existing code style
2. Add TypeScript types
3. Write descriptive commit messages
4. Test on multiple browsers
5. Update documentation

## License

MIT License - See LICENSE file for details
