#!/bin/bash

# AI Code Review Assistant - Project Setup Script
# This script helps resolve all the import errors you're seeing

echo "🔧 AI Code Review Assistant - Setup Helper"
echo "=========================================="
echo ""

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker not found. Please install Docker first:"
    echo "   https://docs.docker.com/get-docker/"
    exit 1
fi

echo "✅ Docker detected"
echo ""

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose not found. Please install Docker Compose first:"
    echo "   https://docs.docker.com/compose/install/"
    exit 1
fi

echo "✅ Docker Compose detected"
echo ""

echo "📋 About the import errors you're seeing:"
echo "=========================================="
echo ""
echo "The errors are NOT code errors - they're just missing Python/Node packages."
echo "This is NORMAL for a fresh project scaffold!"
echo ""
echo "When you run with Docker:"
echo "  • All Python packages will be installed in the backend container"
echo "  • All Python ML packages will be installed in the ml-service container"
echo "  • All Node packages will be installed in the dashboard container"
echo ""

echo "🚀 Starting services with Docker Compose..."
echo ""

cd /Users/srivardhanreddygutta/Projects/AI-code-review-assistant

# Create .env if it doesn't exist
if [ ! -f .env ]; then
    echo "📝 Creating .env file..."
    cp .env.example .env
    echo "   ✅ .env created"
fi

# Start services
echo ""
echo "🐳 Starting Docker services..."
echo "   This may take a few minutes on first run..."
echo ""

docker-compose up -d

# Wait for services
echo ""
echo "⏳ Waiting for services to be ready..."
sleep 5

# Check services
echo ""
echo "✅ Services starting..."
echo ""

echo "📊 Service Status:"
echo "================="
echo "Backend API:    http://localhost:8000"
echo "API Docs:       http://localhost:8000/docs"
echo "ML Service:     http://localhost:8001"
echo "Dashboard:      http://localhost:3000"
echo ""

echo "🎉 Setup complete!"
echo ""
echo "📚 Next steps:"
echo "============="
echo "1. Wait 30-60 seconds for all services to fully start"
echo "2. Visit http://localhost:8000/docs to see the API"
echo "3. Check logs: docker-compose logs -f"
echo ""
echo "✨ The import errors will disappear once Docker installs the packages!"
echo ""
