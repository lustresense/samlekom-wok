@echo off
REM SIMRP Server Startup Script
REM For production deployment

cd /d %~dp0..

echo ============================================
echo SIMRP Server Starting...
echo ============================================
echo.

REM Check Python installation
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Python not found. Please install Python 3.10+
    pause
    exit /b 1
)

echo Python found
echo.

REM Check environment file
if exist ".env.local" (
    echo Environment file: .env.local found
) else (
    echo WARNING: .env.local not found
    echo Copy .env.example to .env.local and configure it
    echo.
)

echo.
echo Starting server...
echo Press Ctrl+C to stop
echo.

REM Start server
python backend\server.py
