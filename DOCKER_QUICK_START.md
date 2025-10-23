# 🚀 Get Docker & Run Everything (Right Now!)

## Step 1: Install Docker Desktop on Mac

**Go to:** https://www.docker.com/products/docker-desktop

**Click:** "Download for Mac"

**Choose:** 
- **Apple Silicon** if you have M1/M2/M3 Mac
- **Intel** if you have older Intel Mac

**Install:** Just drag Docker to Applications folder, then open it

**Verify:** Open Terminal and run:
```bash
docker --version
```

---

## Step 2: Wait for Docker to Start

After opening Docker.app, **wait 1-2 minutes** for it to fully start.

You'll see a whale icon in your Mac menu bar (top right) when it's ready.

---

## Step 3: Run Your Project

Open Terminal and paste this:

```bash
cd /Users/srivardhanreddygutta/Projects/AI-code-review-assistant

cp .env.example .env

docker-compose up -d
```

**Wait 30-60 seconds...**

---

## Step 4: Verify Everything Works

```bash
docker-compose ps
```

You should see 6 services running:
- postgres ✅
- redis ✅
- backend ✅
- ml-service ✅
- dashboard ✅

---

## Step 5: Open Your App

Click these links in your browser:

| What | URL |
|------|-----|
| **API Docs** | http://localhost:8000/docs |
| **Dashboard** | http://localhost:3000 |

---

## 🛑 If Something Goes Wrong

**Check logs:**
```bash
docker-compose logs
```

**Restart everything:**
```bash
docker-compose down
docker-compose up -d
```

**Start fresh:**
```bash
docker-compose down -v
docker-compose build --no-cache
docker-compose up -d
```

---

## ✅ That's It!

Once Docker is installed and running, everything will work automatically!

**Questions?** See [DOCKER_INSTALL.md](./DOCKER_INSTALL.md) for detailed help.
