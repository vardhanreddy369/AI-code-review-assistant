# 🐳 Docker Installation & Setup Guide

## Install Docker on macOS

### Option 1: Docker Desktop (Easiest) ⭐

**Download:**
1. Go to https://www.docker.com/products/docker-desktop
2. Click "Download for Mac"
3. Choose **Apple Silicon** (M1/M2/M3) or **Intel** based on your Mac

**Install:**
1. Open the `.dmg` file
2. Drag Docker icon to Applications folder
3. Open Applications → Docker.app
4. Enter your password when prompted
5. Wait for Docker to start (you'll see whale icon in menu bar)

**Verify installation:**
```bash
docker --version
docker-compose --version
```

---

### Option 2: Homebrew (If you have it)

```bash
# Install Docker Desktop via Homebrew
brew install --cask docker

# Then launch Docker.app from Applications
```

---

### Option 3: Manual Installation

```bash
# Install via direct download
# Visit: https://docs.docker.com/desktop/install/mac-install/
```

---

## ⏳ After Installation

**Docker Desktop needs to be running!**

```bash
# Check if Docker is running
docker ps

# If you get "Cannot connect to Docker daemon"
# → Open Docker.app from Applications (⌘ + Space → type "Docker")
```

---

## 🚀 Quick Start (After Docker is Running)

```bash
cd /Users/srivardhanreddygutta/Projects/AI-code-review-assistant

# 1. Copy environment config
cp .env.example .env

# 2. Start all services
docker-compose up -d

# 3. Wait 30-60 seconds for services to start

# 4. Verify services are running
docker-compose ps

# 5. Check if backend is healthy
curl http://localhost:8000/health

# 6. View API documentation
open http://localhost:8000/docs

# 7. View dashboard
open http://localhost:3000
```

---

## 🛠️ Common Docker Commands

```bash
# See what's running
docker-compose ps

# View logs
docker-compose logs -f

# View logs for specific service
docker-compose logs -f backend
docker-compose logs -f ml-service
docker-compose logs -f dashboard

# Stop services
docker-compose down

# Stop and remove everything
docker-compose down -v

# Restart a service
docker-compose restart backend

# Rebuild after code changes
docker-compose up -d --build

# Enter a container (for debugging)
docker-compose exec backend bash
docker-compose exec ml-service bash
```

---

## ✅ After Services Start

You'll have:

| Service | URL | Purpose |
|---------|-----|---------|
| **Backend API** | http://localhost:8000 | Main API server |
| **API Docs** | http://localhost:8000/docs | Interactive API docs |
| **ML Service** | http://localhost:8001 | ML inference service |
| **Dashboard** | http://localhost:3000 | Web dashboard |
| **PostgreSQL** | localhost:5432 | Database |
| **Redis** | localhost:6379 | Cache |

---

## 🎯 What Docker Does Automatically

✅ Installs all Python packages (backend & ML)  
✅ Installs all Node packages (dashboard)  
✅ Creates PostgreSQL database  
✅ Starts Redis cache  
✅ Runs all services  
✅ Sets up networking between services  

**No manual package installation needed!** 🎉

---

## 🆘 Troubleshooting

### Docker Desktop won't start
- Make sure you have enough disk space
- Restart your Mac
- Check System Preferences → Security & Privacy

### "Cannot connect to Docker daemon"
- Open Docker Desktop from Applications
- Wait for the whale icon to appear in menu bar
- Try again

### Port already in use
```bash
# Find what's using port 8000
lsof -i :8000

# Kill it
kill -9 <PID>

# Or just change port in docker-compose.yml
```

### Services keep restarting
```bash
# Check logs
docker-compose logs

# Rebuild from scratch
docker-compose down -v
docker-compose build --no-cache
docker-compose up -d
```

---

## 📚 Once Services Are Running

1. Visit http://localhost:8000/docs to explore API
2. Read [START_HERE.md](../../START_HERE.md)
3. Read [QUICKSTART.md](../../QUICKSTART.md)
4. Start implementing your features!

---

**Next:** Install Docker, then run `docker-compose up -d` from the project root! 🚀
