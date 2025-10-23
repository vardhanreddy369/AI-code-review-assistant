# Setup and Installation Guide

## Prerequisites

- Python 3.10 or higher
- Node.js 16+ and npm
- Docker and Docker Compose
- PostgreSQL 13+
- Redis 6+
- Git

## Quick Start with Docker Compose

### 1. Clone and Configure

```bash
cd /Users/srivardhanreddygutta/Projects/AI-code-review-assistant
cp .env.example .env
```

### 2. Edit Environment Variables

Update `.env` with your configuration:

```env
# Backend
API_HOST=0.0.0.0
API_PORT=8000
ENV=development

# Database
DATABASE_URL=postgresql://code_review:password@postgres:5432/code_review_db

# Redis
REDIS_URL=redis://redis:6379

# GitHub
GITHUB_TOKEN=your_github_token
GITHUB_WEBHOOK_SECRET=your_webhook_secret

# GitLab
GITLAB_TOKEN=your_gitlab_token
GITLAB_URL=https://gitlab.com

# Bitbucket
BITBUCKET_TOKEN=your_bitbucket_token

# ML Service
ML_SERVICE_URL=http://ml-service:8001
ML_MODEL_NAME=code-review-base

# Security
JWT_SECRET=your_secret_key_change_this
```

### 3. Start Services

```bash
docker-compose up -d
```

This starts:
- Backend API (port 8000)
- ML Service (port 8001)
- PostgreSQL (port 5432)
- Redis (port 6379)
- Dashboard (port 3000)

### 4. Verify Setup

```bash
# Check backend health
curl http://localhost:8000/health

# Check API docs
curl http://localhost:8000/docs
```

## Manual Setup (Development)

### Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp ../.env.example .env

# Run migrations (if using Alembic)
# alembic upgrade head

# Start server
python -m uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

### ML Service Setup

```bash
cd ml-service

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Download pre-trained models
python -c "from transformers import AutoModel; AutoModel.from_pretrained('microsoft/codebert-base')"

# Start inference service
python -m uvicorn inference_service:app --reload --host 0.0.0.0 --port 8001
```

### Dashboard Setup

```bash
cd dashboard

# Install dependencies
npm install

# Create environment file
cp .env.example .env.local

# Start development server
npm run dev
```

### VCS Integration Setup

```bash
cd vcs-integration

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Database Setup

### PostgreSQL

```bash
# Create database
createdb code_review_db

# Create user
createuser code_review -P

# Grant privileges
psql code_review_db -c "GRANT ALL PRIVILEGES ON DATABASE code_review_db TO code_review;"
```

### Run Migrations

```bash
cd backend
alembic upgrade head
```

## GitHub Integration

### Create GitHub App

1. Go to https://github.com/settings/apps
2. Click "New GitHub App"
3. Fill in:
   - App name: "AI Code Review Assistant"
   - Homepage URL: `http://localhost:3000`
   - Webhook URL: `http://your-domain.com/api/v1/webhooks/github`
   - Webhook Secret: Generate a secure secret
4. Permissions:
   - Pull requests: Read & write
   - Repository contents: Read
   - Issues: Read & write
5. Subscribe to:
   - Pull request
   - Push
6. Click "Create GitHub App"

### Configure

```env
GITHUB_APP_ID=your_app_id
GITHUB_PRIVATE_KEY=your_private_key
GITHUB_WEBHOOK_SECRET=your_webhook_secret
```

## GitLab Integration

### Create Personal Access Token

1. Go to https://gitlab.com/profile/personal_access_tokens
2. Create token with scopes:
   - `api`
   - `read_user`
   - `write_repository`

### Configure

```env
GITLAB_TOKEN=your_personal_access_token
GITLAB_URL=https://gitlab.com
GITLAB_WEBHOOK_SECRET=your_webhook_secret
```

## Bitbucket Integration

### Create OAuth Application

1. Go to https://bitbucket.org/account/settings/oauth-consumers/new
2. Fill in application details
3. Grant permissions:
   - `repository:read`
   - `pullrequest:write`

### Configure

```env
BITBUCKET_TOKEN=your_oauth_token
BITBUCKET_WEBHOOK_SECRET=your_webhook_secret
```

## Testing

### Backend Tests

```bash
cd backend
pytest tests/ -v
pytest tests/ -v --cov=app  # With coverage
```

### ML Service Tests

```bash
cd ml-service
pytest tests/ -v
```

### Dashboard Tests

```bash
cd dashboard
npm test
npm run build  # Build for production
```

## Troubleshooting

### PostgreSQL Connection Error

```bash
# Check if PostgreSQL is running
pg_isready -h localhost -p 5432

# Check database exists
psql -l | grep code_review_db
```

### Redis Connection Error

```bash
# Check if Redis is running
redis-cli ping

# Should respond with PONG
```

### ML Model Download Issues

```bash
# Manual model download
python -c "
from transformers import AutoModel, AutoTokenizer
model = AutoModel.from_pretrained('microsoft/codebert-base')
tokenizer = AutoTokenizer.from_pretrained('microsoft/codebert-base')
"
```

### Port Already in Use

```bash
# Find process using port
lsof -i :8000

# Kill process
kill -9 <PID>
```

## Production Deployment

### Using Docker

```bash
# Build production image
docker build -t code-review-assistant:latest .

# Run with environment
docker run -d \
  --name code-review \
  -e DATABASE_URL="postgresql://..." \
  -p 8000:8000 \
  code-review-assistant:latest
```

### Using Kubernetes

```bash
# Create namespace
kubectl create namespace code-review

# Apply manifests
kubectl apply -f k8s/ -n code-review

# Check status
kubectl get pods -n code-review
```

### Environment Optimization

For production, ensure:
- Enable HTTPS/SSL
- Use strong JWT secrets
- Configure database backups
- Set up monitoring and logging
- Enable rate limiting
- Use environment-specific settings

## Monitoring

### Logs

```bash
# Backend logs
docker logs code-review-backend

# ML Service logs
docker logs code-review-ml-service

# Dashboard logs
npm run dev -- --debug
```

### Metrics

- Prometheus metrics available at `/metrics`
- Grafana dashboard configurations in `monitoring/`

## Next Steps

1. Configure webhooks for your repositories
2. Fine-tune ML models on your code review data
3. Set up team notifications
4. Configure custom analysis rules
5. Enable security integrations (e.g., Snyk, SAST tools)

For more information, see [Architecture Documentation](./ARCHITECTURE.md) and [API Documentation](./API.md).
