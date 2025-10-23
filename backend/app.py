"""
FastAPI application for AI Code Review Assistant.
Handles API endpoints, webhook receivers, and code analysis orchestration.
"""

from fastapi import FastAPI, HTTPException, Header, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from dotenv import load_dotenv
import logging
import structlog
import os

from config import settings
from routes import webhooks, analysis, metrics, auth
from services.code_analyzer import code_analyzer
from services.vcs_manager import vcs_manager
from utils.cache import redis_client

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = structlog.get_logger()

# Lifespan context manager
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    logger.info("Starting AI Code Review Assistant API")
    await code_analyzer.initialize()
    await vcs_manager.initialize()
    
    yield
    
    # Shutdown
    logger.info("Shutting down API")
    await redis_client.close()

# Create FastAPI app
app = FastAPI(
    title="AI Code Review Assistant API",
    description="AI-powered code review system for engineering teams",
    version="1.0.0",
    lifespan=lifespan
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/api/v1/auth", tags=["Authentication"])
app.include_router(webhooks.router, prefix="/api/v1/webhooks", tags=["Webhooks"])
app.include_router(analysis.router, prefix="/api/v1/analysis", tags=["Analysis"])
app.include_router(metrics.router, prefix="/api/v1/metrics", tags=["Metrics"])

# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint for load balancers and monitoring."""
    return {
        "status": "healthy",
        "version": "1.0.0",
        "service": "AI Code Review Assistant API"
    }

# Root endpoint
@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "name": "AI Code Review Assistant API",
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/health"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host=settings.API_HOST,
        port=settings.API_PORT,
        log_level="info"
    )
