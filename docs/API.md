# API Documentation

## Overview

The AI Code Review Assistant API provides endpoints for:
- Receiving and analyzing code from pull requests/merge requests
- Posting reviews back to version control systems
- Tracking team metrics and code quality
- Managing authentication and integrations

## Base URL

```
http://localhost:8000/api/v1
```

## Authentication

All endpoints (except `/health` and `/`) require Bearer token authentication:

```
Authorization: Bearer <your-jwt-token>
```

### Login

**POST** `/auth/login`

```json
{
  "email": "user@example.com",
  "password": "password"
}
```

**Response:**
```json
{
  "access_token": "eyJhbGc...",
  "token_type": "bearer",
  "expires_in": 3600
}
```

## Endpoints

### Analysis

#### Analyze Code

**POST** `/analysis/analyze`

Analyze code files for issues and improvements.

**Request Body:**
```json
{
  "files": [
    {
      "path": "src/main.py",
      "content": "...",
      "language": "python"
    }
  ],
  "check_security": true,
  "check_architecture": true,
  "check_quality": true,
  "custom_rules": {}
}
```

**Response:**
```json
{
  "analysis_id": "analysis_123",
  "status": "completed",
  "comments": [
    {
      "file_path": "src/main.py",
      "line_number": 42,
      "severity": "high",
      "category": "security",
      "message": "SQL injection vulnerability detected",
      "suggestion": "Use parameterized queries"
    }
  ],
  "summary": {
    "total_issues": 3,
    "security_issues": 1,
    "architecture_issues": 1,
    "quality_issues": 1
  },
  "processing_time_seconds": 2.5
}
```

#### Get Analysis Result

**GET** `/analysis/analysis/{analysis_id}`

Retrieve results from a previous analysis.

**Response:** Same as analyze endpoint

### Webhooks

#### GitHub Webhook

**POST** `/webhooks/github`

Receive GitHub pull request events.

**Headers:**
- `x-hub-signature-256`: GitHub signature validation

#### GitLab Webhook

**POST** `/webhooks/gitlab`

Receive GitLab merge request events.

**Headers:**
- `x-gitlab-token`: GitLab token validation

#### Bitbucket Webhook

**POST** `/webhooks/bitbucket`

Receive Bitbucket pull request events.

### Metrics

#### Dashboard Metrics

**GET** `/metrics/dashboard?days=30&team_id=team_123`

Get comprehensive dashboard metrics for code quality tracking.

**Response:**
```json
{
  "period": "last_30_days",
  "summary": {
    "total_reviews": 100,
    "avg_review_time_minutes": 15,
    "issues_found": 250,
    "critical_issues": 5,
    "security_issues": 12,
    "avg_quality_score": 85.5
  },
  "trends": {
    "issues_over_time": [],
    "quality_score_trend": [],
    "review_time_trend": []
  },
  "top_issues": [],
  "team_stats": []
}
```

#### Team Metrics

**GET** `/metrics/team/{team_id}/metrics?days=30`

Get metrics for a specific team.

#### Repository Metrics

**GET** `/metrics/repository/{repo_id}/metrics?days=30`

Get metrics for a specific repository.

#### Security Report

**GET** `/metrics/security/report?days=30`

Get security issues report.

**Response:**
```json
{
  "period": "last_30_days",
  "total_issues": 42,
  "by_severity": {
    "critical": [],
    "high": [],
    "medium": [],
    "low": []
  },
  "patterns": []
}
```

#### Quality Trends

**GET** `/metrics/quality/trends?days=30`

Get code quality trends over time.

## Error Responses

### 400 Bad Request
```json
{
  "detail": "Invalid request parameters"
}
```

### 401 Unauthorized
```json
{
  "detail": "Authentication required"
}
```

### 403 Forbidden
```json
{
  "detail": "Insufficient permissions"
}
```

### 404 Not Found
```json
{
  "detail": "Resource not found"
}
```

### 500 Internal Server Error
```json
{
  "detail": "Internal server error"
}
```

## Rate Limiting

- 1000 requests per hour per user
- 10000 requests per hour per API key

Rate limit headers:
- `X-RateLimit-Limit`: Total requests allowed
- `X-RateLimit-Remaining`: Requests remaining
- `X-RateLimit-Reset`: Unix timestamp of rate limit reset

## Pagination

List endpoints support pagination:

**Query Parameters:**
- `page`: Page number (default: 1)
- `per_page`: Items per page (default: 20, max: 100)

**Response:**
```json
{
  "items": [],
  "total": 100,
  "page": 1,
  "per_page": 20,
  "total_pages": 5
}
```
