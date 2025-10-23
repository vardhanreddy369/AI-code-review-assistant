import axios from 'axios'

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api/v1'

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
})

export const dashboardService = {
  getDashboard: (days: number = 30) =>
    apiClient.get('/metrics/dashboard', { params: { days } }),
  
  getTeamMetrics: (teamId: string, days: number = 30) =>
    apiClient.get(`/metrics/team/${teamId}/metrics`, { params: { days } }),
  
  getRepositoryMetrics: (repoId: string, days: number = 30) =>
    apiClient.get(`/metrics/repository/${repoId}/metrics`, { params: { days } }),
  
  getSecurityReport: (days: number = 30) =>
    apiClient.get('/metrics/security/report', { params: { days } }),
  
  getQualityTrends: (days: number = 30) =>
    apiClient.get('/metrics/quality/trends', { params: { days } }),
}

export const analysisService = {
  analyzeCode: (files: Array<{ path: string; content: string }>) =>
    apiClient.post('/analysis/analyze', { files }),
  
  getAnalysis: (analysisId: string) =>
    apiClient.get(`/analysis/analysis/${analysisId}`),
}

export default apiClient
