import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Layout from './components/Layout.tsx'
import DashboardPage from './pages/Dashboard.tsx'
import RepositoriesPage from './pages/Repositories.tsx'
import SecurityPage from './pages/Security.tsx'
import SettingsPage from './pages/Settings.tsx'
import './App.css'

function App() {
  return (
    <Router>
      <Layout>
        <Routes>
          <Route path="/" element={<DashboardPage />} />
          <Route path="/repositories" element={<RepositoriesPage />} />
          <Route path="/security" element={<SecurityPage />} />
          <Route path="/settings" element={<SettingsPage />} />
        </Routes>
      </Layout>
    </Router>
  )
}

export default App
