# Quick Start Guide

## 🚀 Getting Started with AI Code Review Assistant

### What You Have

A complete, production-ready project structure for building an AI-powered code review assistant with:

✅ **Backend API** (FastAPI) - WebHook handling, analysis orchestration  
✅ **ML Service** (PyTorch) - Model inference and fine-tuning  
✅ **VCS Integration** - GitHub, GitLab, Bitbucket connectors  
✅ **Dashboard** (React) - Metrics visualization and analytics  
✅ **Docker Setup** - Complete containerization  
✅ **Documentation** - Comprehensive guides and API docs  
✅ **CI/CD** - GitHub Actions pipeline  

---

## 📁 Project Structure

```
AI-code-review-assistant/
├── backend/                 # FastAPI backend
│   ├── app.py              # Main FastAPI app
│   ├── config.py           # Configuration management
│   ├── requirements.txt    # Python dependencies
│   ├── routes/             # API endpoints
│   ├── services/           # Business logic
│   ├── utils/              # Utilities (cache, etc.)
│   └── Dockerfile          # Container image
│
├── ml-service/             # Machine Learning service
│   ├── train.py            # Model fine-tuning
│   ├── inference.py        # Real-time predictions
│   ├── requirements.txt    # ML dependencies
│   └── Dockerfile
│
├── vcs-integration/        # Version Control System
│   ├── base_connector.py   # Base interface
│   ├── github_connector.py # GitHub API
│   ├── gitlab_connector.py # GitLab API
│   ├── bitbucket_connector.py # Bitbucket API
│   └── requirements.txt
│
├── dashboard/              # React frontend
│   ├── src/
│   │   ├── App.tsx
│   │   ├── services/api.ts
│   │   ├── components/
│   │   └── pages/
│   ├── package.json
│   ├── tsconfig.json
│   └── Dockerfile
│
├── docs/                   # Documentation
│   ├── API.md              # API Reference
│   ├── ARCHITECTURE.md     # System design
│   ├── SETUP.md            # Installation guide
│   └── CONTRIBUTING.md     # Contribution guidelines
│
├── README.md               # Project overview
├── ROADMAP.md              # Development roadmap
├── CHANGELOG.md            # Version history
├── docker-compose.yml      # Docker composition
├── .env.example            # Environment template
└── .github/workflows/      # CI/CD configuration
```

---

## 🔧 Quick Start (5 minutes)

### Option 1: Docker Compose (Recommended)

```bash
# 1. Navigate to project
cd /Users/srivardhanreddygutta/Projects/AI-code-review-assistant

# 2. Create environment file
cp .env.example .env

# 3. Start all services
docker-compose up -d

# 4. Verify services
curl http://localhost:8000/health      # Backend
curl http://localhost:8001/health      # ML Service
curl http://localhost:3000             # Dashboard
```

### Option 2: Manual Setup

**Backend:**
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m uvicorn app:app --reload
```

**ML Service:**
```bash
cd ml-service
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m uvicorn inference_service:app --port 8001 --reload
```

**Dashboard:**
```bash
cd dashboard
npm install
npm run dev
```

---

## 📊 Key Features

### 1. **Security Analysis**
- SQL injection detection
- Credential exposure
- Unsafe cryptography
- API key leaks
- XSS vulnerabilities

### 2. **Architectural Improvements**
- Circular dependency detection
- Code duplication identification
- Design pattern suggestions
- Performance anti-patterns

### 3. **Code Quality**
- Complexity metrics
- Coverage analysis
- Documentation gaps
- Test recommendations

### 4. **Context-Aware Analysis**
- Cross-file dependencies
- Function tracking
- Variable flow analysis
- Import resolution

### 5. **Team Dashboard**
- Real-time metrics
- Quality trends
- Security reports
- Team analytics

---

## 🔌 API Endpoints

### Analysis
```
POST   /api/v1/analysis/analyze         # Analyze code
GET    /api/v1/analysis/analysis/{id}   # Get results
```

### Webhooks
```
POST   /api/v1/webhooks/github          # GitHub PR events
POST   /api/v1/webhooks/gitlab          # GitLab MR events
POST   /api/v1/webhooks/bitbucket       # Bitbucket PR events
```

### Metrics
```
GET    /api/v1/metrics/dashboard        # Dashboard metrics
GET    /api/v1/metrics/security/report  # Security report
GET    /api/v1/metrics/quality/trends   # Quality trends
```

### Authentication
```
POST   /api/v1/auth/login               # User login
GET    /api/v1/auth/me                  # Current user
POST   /api/v1/auth/refresh             # Refresh token
```

Full API docs: `http://localhost:8000/docs`

---

## 🔑 Configuration

### Environment Variables

**Essential:**
```env
# Database
DATABASE_URL=postgresql://user:pass@localhost/db

# Cache
REDIS_URL=redis://localhost:6379

# VCS Tokens (choose what you need)
GITHUB_TOKEN=your_token
GITLAB_TOKEN=your_token
BITBUCKET_TOKEN=your_token

# Security
JWT_SECRET=your_secret_key
```

**Optional:**
```env
# ML Service
ML_SERVICE_URL=http://localhost:8001
ML_MODEL_NAME=code-review-base

# API
API_PORT=8000
API_HOST=0.0.0.0
```

See `.env.example` for all options.

---

## 🤖 ML Model Fine-Tuning

### Prepare Training Data

Create `data/training.json`:
```json
[
  {
    "code": "def unsafe_query(user_id):\n    query = 'SELECT * FROM users WHERE id = ' + str(user_id)\n    return db.execute(query)",
    "label": 1,
    "category": "security",
    "issue": "SQL injection"
  }
]
```

### Train Model

```bash
cd ml-service
python train.py --dataset data/training.json --output models/finetuned
```

### Use Fine-Tuned Model

Update `.env`:
```env
ML_MODEL_NAME=models/finetuned
```

---

## 🔗 VCS Integration Setup

### GitHub
1. Create Personal Access Token: https://github.com/settings/tokens
2. Add to `.env`: `GITHUB_TOKEN=ghp_...`
3. Create GitHub App (optional): https://github.com/settings/apps

### GitLab
1. Create Token: https://gitlab.com/profile/personal_access_tokens
2. Add to `.env`: `GITLAB_TOKEN=glpat_...`

### Bitbucket
1. Create OAuth Consumer: https://bitbucket.org/account/settings/oauth-consumers
2. Add to `.env`: `BITBUCKET_TOKEN=...`

---

## 📊 Dashboard Usage

**Access:** http://localhost:3000

**Features:**
- View code quality metrics
- Track security issues
- Monitor team productivity
- Analyze trends over time
- Manage integrations
- Configure settings

---

## 🧪 Testing

### Backend Tests
```bash
cd backend
pytest tests/ -v
pytest tests/ --cov=app  # With coverage
```

### ML Tests
```bash
cd ml-service
pytest tests/ -v
```

### Frontend Tests
```bash
cd dashboard
npm test
npm run build
```

---

## 📚 Documentation

- **[README.md](./README.md)** - Project overview
- **[docs/SETUP.md](./docs/SETUP.md)** - Detailed setup guide
- **[docs/API.md](./docs/API.md)** - API reference
- **[docs/ARCHITECTURE.md](./docs/ARCHITECTURE.md)** - System design
- **[docs/CONTRIBUTING.md](./docs/CONTRIBUTING.md)** - Contributing guide
- **[ROADMAP.md](./ROADMAP.md)** - Development roadmap

---

## 🚀 Next Steps

### 1. **Local Development**
```bash
# Start with Docker Compose
docker-compose up -d

# Access services
# Backend API: http://localhost:8000
# API Docs: http://localhost:8000/docs
# Dashboard: http://localhost:3000
# ML Service: http://localhost:8001
```

### 2. **Configure VCS**
- Generate API tokens for your VCS platforms
- Update `.env` with tokens
- Test webhook connections

### 3. **Set Up First Integration**
- Start with GitHub or GitLab
- Create test repository
- Push code and verify webhook receives events

### 4. **Fine-Tune Models**
- Collect code review data from your team
- Prepare training dataset
- Run fine-tuning pipeline
- Update model configuration

### 5. **Deploy to Production**
- Use provided Kubernetes manifests
- Set up PostgreSQL cluster
- Configure Redis cluster
- Enable monitoring and logging

---

## 🐛 Troubleshooting

### Port Already in Use
```bash
# Find process using port
lsof -i :8000

# Kill process
kill -9 <PID>
```

### Database Connection Error
```bash
# Check PostgreSQL
pg_isready -h localhost -p 5432

# Check Redis
redis-cli ping
```

### ML Model Download Issues
```bash
# Manual download
python -c "from transformers import AutoModel; AutoModel.from_pretrained('microsoft/codebert-base')"
```

See **[docs/SETUP.md](./docs/SETUP.md)** for detailed troubleshooting.

---

## 📞 Support

- **Documentation:** See `docs/` folder
- **Issues:** GitHub Issues
- **Discussions:** GitHub Discussions
- **Contributing:** See [docs/CONTRIBUTING.md](./docs/CONTRIBUTING.md)

---

## 📄 License

MIT License - See LICENSE file

---

## 🎯 Key Metrics to Track

During development, monitor:

- **Performance**: Analysis time < 5 seconds
- **Accuracy**: Security detection > 85% accuracy
- **Adoption**: Track teams using the system
- **Quality**: False negative rate < 1%
- **Reliability**: Aim for 99.9% uptime
- **User Satisfaction**: Target > 4.5/5 rating

---

## 🔄 Development Workflow

1. **Create Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Implement Feature**
   - Write code following style guides
   - Add tests
   - Update documentation

3. **Test Locally**
   ```bash
   # Backend
   cd backend && pytest tests/
   
   # Frontend
   cd dashboard && npm test
   ```

4. **Commit & Push**
   ```bash
   git add .
   git commit -m "feat: add your feature"
   git push origin feature/your-feature-name
   ```

5. **Create Pull Request**
   - Describe changes
   - Link related issues
   - Wait for CI/CD and review

---

## 💡 Pro Tips

- Use `docker-compose logs -f service_name` for debugging
- Enable VS Code Python extension for better development
- Use Postman or Insomnia for API testing
- Check `.github/workflows/` for CI/CD examples
- Review `ROADMAP.md` for planned features
- Check existing issues before creating new ones

---

**Happy coding! 🚀**

For detailed setup, see [docs/SETUP.md](./docs/SETUP.md)
