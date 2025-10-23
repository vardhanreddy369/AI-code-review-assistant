"""
Configuration management for the backend service.
Loads settings from environment variables with sensible defaults.
"""

from pydantic_settings import BaseSettings
from typing import List
import os

class Settings(BaseSettings):
    """Application settings"""
    
    # API Configuration
    API_HOST: str = os.getenv("API_HOST", "0.0.0.0")
    API_PORT: int = int(os.getenv("API_PORT", "8000"))
    API_VERSION: str = "v1"
    
    # Environment
    ENV: str = os.getenv("ENV", "development")
    DEBUG: bool = ENV == "development"
    
    # CORS
    CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:8000",
        os.getenv("FRONTEND_URL", "http://localhost:3000")
    ]
    
    # Database
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql://user:password@localhost/code_review_db"
    )
    
    # Redis Cache
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379")
    CACHE_TTL: int = int(os.getenv("CACHE_TTL", "3600"))
    
    # ML Service
    ML_SERVICE_URL: str = os.getenv("ML_SERVICE_URL", "http://localhost:8001")
    ML_MODEL_NAME: str = os.getenv("ML_MODEL_NAME", "code-review-base")
    BATCH_SIZE: int = int(os.getenv("BATCH_SIZE", "32"))
    
    # GitHub Integration
    GITHUB_TOKEN: str = os.getenv("GITHUB_TOKEN", "")
    GITHUB_WEBHOOK_SECRET: str = os.getenv("GITHUB_WEBHOOK_SECRET", "")
    GITHUB_APP_ID: str = os.getenv("GITHUB_APP_ID", "")
    GITHUB_PRIVATE_KEY: str = os.getenv("GITHUB_PRIVATE_KEY", "")
    
    # GitLab Integration
    GITLAB_TOKEN: str = os.getenv("GITLAB_TOKEN", "")
    GITLAB_WEBHOOK_SECRET: str = os.getenv("GITLAB_WEBHOOK_SECRET", "")
    GITLAB_URL: str = os.getenv("GITLAB_URL", "https://gitlab.com")
    
    # Bitbucket Integration
    BITBUCKET_TOKEN: str = os.getenv("BITBUCKET_TOKEN", "")
    BITBUCKET_WEBHOOK_SECRET: str = os.getenv("BITBUCKET_WEBHOOK_SECRET", "")
    
    # Security
    JWT_SECRET: str = os.getenv("JWT_SECRET", "your-secret-key-change-in-production")
    JWT_ALGORITHM: str = "HS256"
    TOKEN_EXPIRY_MINUTES: int = int(os.getenv("TOKEN_EXPIRY_MINUTES", "60"))
    
    # Analysis Configuration
    MAX_FILES_PER_PR: int = int(os.getenv("MAX_FILES_PER_PR", "100"))
    MAX_FILE_SIZE_MB: int = int(os.getenv("MAX_FILE_SIZE_MB", "1"))
    ANALYSIS_TIMEOUT_SECONDS: int = int(os.getenv("ANALYSIS_TIMEOUT_SECONDS", "300"))
    
    # Supported file extensions for analysis
    SUPPORTED_EXTENSIONS: List[str] = [
        ".py", ".js", ".ts", ".tsx", ".jsx",
        ".java", ".go", ".rs", ".cpp", ".c",
        ".cs", ".php", ".rb", ".sql", ".yaml", ".yml"
    ]
    
    # Webhook Configuration
    WEBHOOK_TIMEOUT_SECONDS: int = 30
    WEBHOOK_RETRY_ATTEMPTS: int = 3
    
    # Celery Configuration
    CELERY_BROKER_URL: str = os.getenv("CELERY_BROKER_URL", "redis://localhost:6379")
    CELERY_RESULT_BACKEND: str = os.getenv("CELERY_RESULT_BACKEND", "redis://localhost:6379")
    
    # Logging
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    
    class Config:
        env_file = ".env"
        case_sensitive = True

# Create settings instance
settings = Settings()
