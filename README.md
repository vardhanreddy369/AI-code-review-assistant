# AI Code Review Assistant

An intelligent code review system powered by fine-tuned language models, designed for engineering teams to automate code quality checks, detect security issues, and track metrics over time.

## 🎯 Key Features

- **AI-Powered Code Analysis**: Uses fine-tuned LLMs to understand code context across multiple files
- **Architectural Improvements**: Suggests refactoring and architectural enhancements
- **Security Analysis**: Flags potential security vulnerabilities and compliance issues
- **VCS Integration**: Seamless integration with GitHub, GitLab, and Bitbucket
- **Webhook Support**: Real-time PR/MR analysis with webhook integration
- **Team Dashboard**: Comprehensive metrics tracking for engineering teams
- **Model Fine-Tuning**: Train custom models on your codebase and review data
- **Context-Aware**: Understands cross-file dependencies and relationships

## 🏗️ Architecture

```
AI Code Review Assistant
├── Backend API (FastAPI)
│   ├── Webhook handlers
│   ├── Code analysis engine
│   └── Database & caching
├── ML Service (PyTorch)
│   ├── Model fine-tuning pipeline
│   ├── Inference service
│   └── Feature extraction
├── VCS Integration
│   ├── GitHub connector
│   ├── GitLab connector
│   └── Bitbucket connector
├── Dashboard (React/TypeScript)
│   ├── Metrics visualization
│   ├── Review history
│   └── Team analytics
└── Documentation & DevOps
    ├── Docker setup
    └── Deployment configs
```

## 📋 Project Structure

```
.
├── backend/                    # FastAPI backend server
│   ├── app.py
│   ├── requirements.txt
│   ├── config.py
│   ├── models/
│   ├── routes/
│   ├── services/
│   └── utils/
├── ml-service/                 # ML model service
│   ├── train.py
│   ├── inference.py
│   ├── requirements.txt
│   ├── models/
│   ├── datasets/
│   ├── config/
│   └── utils/
├── vcs-integration/            # Version control integrations
│   ├── github_connector.py
│   ├── gitlab_connector.py
│   ├── bitbucket_connector.py
│   ├── base_connector.py
│   ├── requirements.txt
│   └── utils/
├── dashboard/                  # React frontend
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   └── App.tsx
│   ├── package.json
│   └── tsconfig.json
├── docs/                       # Documentation
│   ├── API.md
│   ├── SETUP.md
│   ├── ARCHITECTURE.md
│   └── CONTRIBUTING.md
├── docker-compose.yml
├── Dockerfile
├── .env.example
└── README.md
```

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Node.js 16+
- Docker & Docker Compose
- PostgreSQL 13+

### Installation

1. **Clone the repository**
   ```bash
   cd /Users/srivardhanreddygutta/Projects/AI-code-review-assistant
   ```

2. **Backend Setup**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **ML Service Setup**
   ```bash
   cd ml-service
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

4. **Dashboard Setup**
   ```bash
   cd dashboard
   npm install
   npm run dev
   ```

5. **Environment Configuration**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

## 🔧 Configuration

Create a `.env` file with:
```env
# Backend
FLASK_ENV=development
API_HOST=0.0.0.0
API_PORT=8000

# Database
DATABASE_URL=postgresql://user:password@localhost/code_review_db

# ML Service
ML_MODEL_PATH=./models/code-review-model
BATCH_SIZE=32

# GitHub Integration
GITHUB_TOKEN=your_token
GITHUB_WEBHOOK_SECRET=your_secret

# GitLab Integration
GITLAB_TOKEN=your_token
GITLAB_WEBHOOK_SECRET=your_secret

# Cache
REDIS_URL=redis://localhost:6379

# Security
JWT_SECRET=your_secret_key
```

## 🔑 Key Components

### Backend API
- RESTful API for receiving PR/MR data
- Webhook handlers for real-time analysis
- Code analysis orchestration
- Results storage and retrieval

### ML Service
- LLM fine-tuning pipeline (CodeBERT, CodeT5, or similar)
- Batch and real-time inference
- Model versioning and A/B testing
- Feature extraction from source code

### VCS Integration
- OAuth-based authentication
- Pull request/Merge request parsing
- Diff analysis and context gathering
- Review comment posting

### Dashboard
- Real-time metrics visualization
- Code quality trends
- Security vulnerability tracking
- Team productivity analytics

## 🔍 Core Capabilities

### 1. Security Issue Detection
- SQL injection patterns
- Credential exposure
- Unsafe cryptography usage
- API key exposure
- XSS vulnerabilities

### 2. Architectural Improvements
- Circular dependency detection
- Code duplication identification
- Design pattern suggestions
- Performance anti-patterns

### 3. Code Quality Metrics
- Complexity analysis
- Coverage trends
- Test coverage recommendations
- Documentation gaps

### 4. Context Understanding
- Cross-file dependency analysis
- Function signature tracking
- Variable flow analysis
- Import resolution

## 📚 Documentation

- [API Documentation](./docs/API.md)
- [Setup Guide](./docs/SETUP.md)
- [Architecture Guide](./docs/ARCHITECTURE.md)
- [Contributing Guidelines](./docs/CONTRIBUTING.md)

## 🤖 Model Fine-Tuning

The project supports fine-tuning models on:
- Your internal code review datasets
- Security vulnerability databases
- Architectural pattern examples
- Your team's coding standards

```bash
cd ml-service
python train.py --config configs/finetuning_config.yaml
```

## 🐳 Docker Deployment

```bash
docker-compose up -d
```

## 🧪 Testing

```bash
# Backend tests
cd backend && pytest tests/

# ML Service tests
cd ../ml-service && pytest tests/

# Dashboard tests
cd ../dashboard && npm test
```

## 📈 Roadmap

- [ ] Advanced context aggregation (AST analysis)
- [ ] Multi-language support (Java, Go, Rust, etc.)
- [ ] IDE integrations (VSCode, IntelliJ)
- [ ] Self-hosted model options
- [ ] Custom rule engine
- [ ] Automated fixes with ML
- [ ] Team-specific model adaptation

## 🤝 Contributing

See [CONTRIBUTING.md](./docs/CONTRIBUTING.md) for guidelines.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

## 👥 Support

For issues, questions, or suggestions, please open an issue on GitHub.

---

**Built with** ❤️ for engineering teams who care about code quality
