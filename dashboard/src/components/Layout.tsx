import { ReactNode } from 'react'
import './Layout.css'

interface LayoutProps {
  children: ReactNode
}

export default function Layout({ children }: LayoutProps) {
  return (
    <div className="layout">
      <nav className="navbar">
        <div className="navbar-brand">
          <h2>🔍 AI Code Review</h2>
        </div>
        <ul className="nav-links">
          <li><a href="/">Dashboard</a></li>
          <li><a href="/repositories">Repositories</a></li>
          <li><a href="/security">Security</a></li>
          <li><a href="/settings">Settings</a></li>
        </ul>
      </nav>
      <main className="main-content">
        {children}
      </main>
    </div>
  )
}
