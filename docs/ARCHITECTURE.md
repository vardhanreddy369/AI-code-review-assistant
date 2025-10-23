# Architecture Overview

## System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     Engineers & Teams                            │
└─────────────┬──────────────────────────┬──────────────────────────┘
              │                          │
    ┌─────────▼──────────┐    ┌──────────▼──────────┐
    │  GitHub/GitLab/    │    │  Dashboard (React)  │
    │  Bitbucket         │    │  Web Interface      │
    └─────────┬──────────┘    └──────────┬──────────┘
              │                          │
              └──────────────┬───────────┘
                             │
         ┌───────────────────▼────────────────────┐
         │    Backend API (FastAPI)               │
         │  - Webhook Handlers                    │
         │  - Code Analysis Orchestration         │
         │  - Metrics & Analytics                 │
         └───────────────────┬────────────────────┘
                             │
         ┌───────────────────┼────────────────────┐
         │                   │                    │
    ┌────▼─────┐    ┌────────▼────────┐   ┌──────▼──────┐
    │ ML Service│    │  VCS Integration│   │  PostgreSQL │
    │ (PyTorch) │    │  - GitHub       │   │  Database   │
    │           │    │  - GitLab       │   │             │
    │ - Inference    │  - Bitbucket    │   └─────────────┘
    │ - Fine-tuning  └─────────────────┘
    └────┬─────┘
         │
    ┌────▼──────────────┐
    │  Model Registry   │
    │  - CodeBERT       │
    │  - CodeT5         │
    │  - Fine-tuned     │
    └───────────────────┘
```

## Component Details

### 1. Backend API (FastAPI)

**Responsibilities:**
- REST API for code analysis requests
- Webhook handling for VCS events
- Authentication and authorization
- Request routing and orchestration
- Result caching and storage

**Key Features:**
- Async request handling
- Background task processing with Celery
- Database persistence
- Redis caching layer

### 2. ML Service

**Responsibilities:**
- Code feature extraction and analysis
- Model inference for issue detection
- Fine-tuning on custom datasets
- Model versioning and evaluation

**Key Components:**
- `train.py`: Model fine-tuning pipeline
- `inference.py`: Real-time prediction service
- Feature extractors for code analysis
- Model loading and optimization

**Models Supported:**
- CodeBERT (base)
- CodeT5
- Custom fine-tuned models

### 3. VCS Integration

**Supported Platforms:**
- GitHub (via REST API)
- GitLab (via REST API)
- Bitbucket (via REST API)

**Capabilities:**
- PR/MR file retrieval
- Review comment posting
- Webhook setup and validation
- OAuth authentication

### 4. Database

**PostgreSQL Schema:**
- Users & Teams
- Repositories
- Pull Requests/Merge Requests
- Analysis Results
- Review Comments
- Metrics & Aggregations

### 5. Cache Layer

**Redis:**
- Analysis results caching
- Session management
- Rate limiting
- Temporary storage

### 6. Dashboard

**Frontend (React + TypeScript):**
- Real-time metrics visualization
- Code quality trends
- Security issue tracking
- Team analytics
- Repository management

## Data Flow

### Analysis Flow

```
1. Webhook Event (PR/MR Created/Updated)
   ↓
2. Backend Receives & Validates Event
   ↓
3. Fetch File Changes from VCS
   ↓
4. Extract Code Features
   ↓
5. Call ML Service for Analysis
   ├─ Security Check
   ├─ Architecture Check
   └─ Quality Check
   ↓
6. Aggregate Results
   ↓
7. Generate Review Comments
   ↓
8. Post Comments to VCS
   ↓
9. Store Results in Database
   ↓
10. Update Dashboard Metrics
```

### Metrics Collection

```
Analysis Results
   ↓
Database Storage
   ↓
Metrics Aggregation
   ├─ By Team
   ├─ By Repository
   ├─ By Time Period
   └─ By Issue Category
   ↓
Dashboard Display
```

## Security Considerations

### Authentication
- JWT-based token authentication
- OAuth2 for VCS providers
- API key rotation support

### Data Protection
- Encrypted sensitive data (credentials, API keys)
- HTTPS/TLS for all communications
- Rate limiting per user/IP
- Input validation and sanitization

### Code Analysis
- Sandboxed model inference
- No code storage (temporary processing)
- Configurable retention policies
- Audit logging of all operations

## Scalability

### Horizontal Scaling
- Stateless API design
- Load balancing support
- Database connection pooling
- Cache replication

### Performance
- Async/await throughout
- Batch processing support
- Model optimization (quantization, pruning)
- Efficient feature extraction

## Deployment

### Local Development
- Docker Compose setup
- SQLite for development
- Redis for caching

### Production
- Kubernetes deployment ready
- PostgreSQL cluster
- Redis cluster
- CDN for static assets
- Monitoring and logging infrastructure

## Integration Points

### Incoming
- GitHub/GitLab/Bitbucket webhooks
- Manual analysis API calls
- Dashboard user interactions

### Outgoing
- PR/MR comments
- Team notifications
- Metrics exports
- External analytics tools

## Technology Stack

**Backend:**
- FastAPI (Python web framework)
- SQLAlchemy (ORM)
- PostgreSQL (database)
- Redis (caching)
- Celery (task queue)

**ML:**
- PyTorch (deep learning)
- HuggingFace Transformers (pre-trained models)
- Scikit-learn (feature extraction)

**VCS Integration:**
- requests/aiohttp (HTTP clients)
- GitPython (local git operations)

**Frontend:**
- React 18 (UI framework)
- TypeScript (type safety)
- Recharts (data visualization)
- Tailwind CSS (styling)

**DevOps:**
- Docker & Docker Compose
- GitHub Actions (CI/CD)
- Kubernetes (orchestration)
