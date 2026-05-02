# 🚀 SIMRP Production Deployment Guide

## ✅ PRODUCTION READY STATUS

**Version**: 2.0.0 Professional  
**Status**: READY FOR DEPLOYMENT  
**Architecture**: Layered (Repository-Service-Route)  
**Database**: SQLite (single file, easy backup)  
**Server**: Python built-in HTTP server (no external dependencies)

---

## 📦 DEPLOYMENT PACKAGES

### What You Get:
- ✅ **Single Python file** backend (`backend/server.py`)
- ✅ **Static frontend files** (build from `frontend/dist/`)
- ✅ **SQLite database** (auto-created in `database/runtime/`)
- ✅ **Environment configuration** (`.env.local`)
- ✅ **Backup scripts** (automated)

---

## 🎯 DEPLOYMENT STEPS

### For Diskominfo Server

#### Step 1: Prerequisites

**Server Requirements:**
- Python 3.10 or higher
- Node.js 18+ (for building frontend)
- 2 GB RAM minimum
- 10 GB storage
- Windows Server 2019+ or Linux Ubuntu 20.04+

**Check Python:**
```bash
python --version
# Should be 3.10+
```

**Check Node.js:**
```bash
node --version
# Should be 18+
```

---

#### Step 2: Copy Files to Server

Copy entire project folder to server:
```
D:\Diskominfo\SIMRP\
├── backend/
├── frontend/
├── database/
├── docs/
├── .env.example
├── package.json
└── README.md
```

---

#### Step 3: Configure Environment

Create `.env.local` file:

```bash
# Copy from example
copy .env.example .env.local
```

Edit `.env.local`:

```bash
# PRODUCTION CONFIGURATION
SIMRP_ENV=production

# CRITICAL: Change these!
SIMRP_ADMIN_LOGIN_USERNAME=admin_surabaya
SIMRP_ADMIN_PASSWORD=Str0ng!P@ssw0rd#2026#Secure

# Security
SIMRP_PBKDF2_ITERATIONS=600000
SIMRP_SESSION_TTL_HOURS=12

# CORS (add your domain)
SIMRP_ALLOWED_ORIGINS=https://simrp.surabaya.go.id

# Database path
SIMRP_DB_PATH=D:/Diskominfo/SIMRP/database/runtime/database.db
```

---

#### Step 4: Install Dependencies

**Install Python dependencies** (none needed - using built-in libraries only!)

**Install Node.js dependencies:**
```bash
cd D:\Diskominfo\SIMRP
npm install
```

---

#### Step 5: Build Frontend

```bash
npm run build
```

This creates optimized static files in `frontend/dist/`.

---

#### Step 6: Initialize Database

Database auto-initializes on first run. To manually initialize:

```bash
python backend/server.py
# Press Ctrl+C after seeing "Database initialized successfully"
```

---

#### Step 7: Start Server

**Option A: Manual Start (for testing)**
```bash
python backend/server.py
```

Server will start at: `http://127.0.0.1:8000`

**Option B: Windows Service (for production)**

Create `start_simrp.bat`:
```batch
@echo off
cd /d D:\Diskominfo\SIMRP
python backend/server.py
```

Create Windows Scheduled Task:
1. Open Task Scheduler
2. Create Basic Task
3. Name: "SIMRP Server"
4. Trigger: "When the computer starts"
5. Action: "Start a program"
6. Program: `D:\Diskominfo\SIMRP\start_simrp.bat`
7. Finish

**Option C: Linux systemd (for Ubuntu server)**

Create `/etc/systemd/system/simrp.service`:
```ini
[Unit]
Description=SIMRP API Server
After=network.target

[Service]
Type=simple
User=simrp
WorkingDirectory=/opt/simrp
EnvironmentFile=/opt/simrp/.env.local
ExecStart=/usr/bin/python3 /opt/simrp/backend/server.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Enable and start:
```bash
sudo systemctl daemon-reload
sudo systemctl enable simrp
sudo systemctl start simrp
sudo systemctl status simrp
```

---

#### Step 8: Setup Reverse Proxy (Optional but Recommended)

**For nginx:**

Install nginx:
```bash
# Windows: Download from nginx.org
# Linux: sudo apt install nginx
```

Configure nginx (`nginx.conf`):
```nginx
server {
    listen 80;
    server_name simrp.surabaya.go.id;

    # Redirect to HTTPS (if SSL configured)
    # return 301 https://$server_name$request_uri;

    # Serve frontend static files
    location / {
        root D:/Diskominfo/SIMRP/frontend/dist;
        try_files $uri $uri/ /index.html;
    }

    # Proxy API requests to backend
    location /make-server-32aa5c5c/ {
        proxy_pass http://127.0.0.1:8000/make-server-32aa5c5c/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Restart nginx:
```bash
# Windows: nginx -s reload
# Linux: sudo systemctl restart nginx
```

---

#### Step 9: Setup SSL/HTTPS (Recommended)

**Using Let's Encrypt (free):**

```bash
# Install Certbot
# Windows: Download from certbot.eff.org
# Linux: sudo apt install certbot python3-certbot-nginx

# Get certificate
certbot --nginx -d simrp.surabaya.go.id
```

Certbot auto-configures nginx with SSL.

---

#### Step 10: Verify Deployment

**Test health endpoint:**
```bash
curl http://127.0.0.1:8000/make-server-32aa5c5c/health
# Expected: {"status": "ok"}
```

**Test frontend:**
Open browser: `http://127.0.0.1:8000` (or your domain)

**Test admin login:**
1. Go to `/admin`
2. Login with credentials from `.env.local`
3. Verify dashboard loads

---

## 🔄 BACKUP STRATEGY

### Database Backup Script

Create `backup_database.bat` (Windows):
```batch
@echo off
set BACKUP_DIR=D:\Diskominfo\SIMRP\database\backups
set DB_FILE=D:\Diskominfo\SIMRP\database\runtime\database.db
set DATE=%date:~-4,4%%date:~-7,2%%date:~-10,2%_%time:~0,2%%time:~3,2%
set DATE=%DATE: =0%

mkdir "%BACKUP_DIR%" 2>nul
copy "%DB_FILE%" "%BACKUP_DIR%\backup_%DATE%.db"

echo Backup completed: backup_%DATE%.db
```

Create `backup_database.sh` (Linux):
```bash
#!/bin/bash
BACKUP_DIR="/opt/simrp/database/backups"
DB_FILE="/opt/simrp/database/runtime/database.db"
DATE=$(date +%Y%m%d_%H%M%S)

mkdir -p "$BACKUP_DIR"
cp "$DB_FILE" "$BACKUP_DIR/backup_$DATE.db"

echo "Backup completed: backup_$DATE.db"
```

### Automated Backups

**Windows Task Scheduler:**
1. Open Task Scheduler
2. Create Basic Task: "SIMRP Daily Backup"
3. Trigger: Daily at 2:00 AM
4. Action: Start program `D:\Diskominfo\SIMRP\backup_database.bat`

**Linux Cron:**
```bash
# Edit crontab
crontab -e

# Add daily backup at 2 AM
0 2 * * * /opt/simrp/backup_database.sh
```

### Backup Retention

Create cleanup script to keep only last 30 days:

**Windows:** `cleanup_backups.bat`
```batch
@echo off
forfiles /p "D:\Diskominfo\SIMRP\database\backups" /s /m *.db /d -30 /c "cmd /c del @path"
echo Old backups cleaned up
```

**Linux:**
```bash
find /opt/simrp/database/backups -name "*.db" -mtime +30 -delete
```

---

## 🛡️ SECURITY CHECKLIST

### Before Going Live:

- [ ] Changed admin password from default
- [ ] Set `SIMRP_ENV=production`
- [ ] Configured `SIMRP_ALLOWED_ORIGINS`
- [ ] Set `SIMRP_PBKDF2_ITERATIONS=600000`
- [ ] Enabled HTTPS/SSL
- [ ] Configured firewall (allow port 80/443 only)
- [ ] Setup database backups
- [ ] Tested all user flows
- [ ] Documented admin credentials securely

---

## 📊 MONITORING

### Health Check Endpoint

```bash
curl http://127.0.0.1:8000/make-server-32aa5c5c/health
```

Expected response: `{"status": "ok"}`

### Log Files

Server logs to console. To save to file:

**Windows:**
```batch
python backend/server.py > logs\server.log 2>&1
```

**Linux:**
```bash
python3 backend/server.py > /var/log/simrp/server.log 2>&1
```

### Metrics to Monitor

- **Response time**: Should be < 200ms
- **Error rate**: Should be < 1%
- **Database size**: Monitor growth
- **Active sessions**: Check for anomalies

---

## 🔧 MAINTENANCE

### Database Vacuum (Monthly)

```bash
python -c "import sqlite3; conn = sqlite3.connect('database/runtime/database.db'); conn.execute('VACUUM'); conn.close()"
```

### Clear Old Sessions (Weekly)

Sessions auto-expire, but manual cleanup:

```bash
python -c "
import sqlite3
from datetime import datetime, timedelta
conn = sqlite3.connect('database/runtime/database.db')
expiry = (datetime.now() - timedelta(hours=24)).isoformat()
conn.execute('DELETE FROM sessions WHERE expires_at < ?', (expiry,))
conn.commit()
conn.close()
"
```

### Update Deployment

1. Backup database
2. Stop server
3. Copy new files
4. Run `npm install` if dependencies changed
5. Run `npm run build`
6. Start server
7. Verify health endpoint

---

## 📞 SUPPORT

### Common Issues

**Server won't start:**
- Check Python version (need 3.10+)
- Check if port 8000 is available
- Check `.env.local` syntax

**Database errors:**
- Check file permissions
- Ensure `database/runtime/` folder exists
- Check disk space

**Frontend not loading:**
- Run `npm run build`
- Check `frontend/dist/` exists
- Clear browser cache

### Contact

For technical support, contact:
- **Development Team**: [Your contact]
- **Diskominfo IT**: [Their contact]

---

## 📈 PERFORMANCE TUNING

### For High Traffic (1000+ concurrent users)

1. **Increase rate limits** in `.env.local`:
   ```bash
   SIMRP_RATE_LIMIT_MUTATION_MAX=300
   ```

2. **Use WAL mode** for database (auto-enabled in production)

3. **Add caching layer** (Redis) - future enhancement

4. **Horizontal scaling** - run multiple instances behind load balancer

---

## ✅ DEPLOYMENT VERIFICATION CHECKLIST

After deployment, verify:

- [ ] Health endpoint returns `{"status": "ok"}`
- [ ] Frontend loads without errors
- [ ] Admin login works
- [ ] User registration works
- [ ] Event creation works
- [ ] Report submission works
- [ ] Database backup script runs
- [ ] Logs are being written
- [ ] HTTPS is working (if configured)
- [ ] All demo accounts can login

---

**Deployment Guide Version**: 1.0  
**Last Updated**: April 2026  
**© 2025 Dinas Komunikasi dan Informatika Kota Surabaya**
