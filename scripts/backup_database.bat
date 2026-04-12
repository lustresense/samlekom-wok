@echo off
REM SIMRP Database Backup Script
REM Run this daily via Task Scheduler

set BACKUP_DIR=%~dp0database\backups
set DB_FILE=%~dp0database\runtime\database.db
set DATE=%date:~-4,4%%date:~-7,2%%date:~-10,2%_%time:~0,2%%time:~3,2%
set DATE=%DATE: =0%

echo ============================================
echo SIMRP Database Backup
echo ============================================
echo.

REM Create backup directory if not exists
if not exist "%BACKUP_DIR%" (
    mkdir "%BACKUP_DIR%"
    echo Created backup directory: %BACKUP_DIR%
)

REM Copy database file
echo Backing up database...
copy "%DB_FILE%" "%BACKUP_DIR%\backup_%DATE%.db"

if %ERRORLEVEL% EQU 0 (
    echo.
    echo SUCCESS: Backup completed
    echo File: backup_%DATE%.db
    echo Location: %BACKUP_DIR%
) else (
    echo.
    echo ERROR: Backup failed
    echo Check if database file is in use
)

echo.
echo ============================================
pause
