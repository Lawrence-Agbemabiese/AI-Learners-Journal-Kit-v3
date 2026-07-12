@echo off
REM Friendly top-level launcher for non-technical Windows users.
cd /d "%~dp0"

if exist "Start AI Journal (Web).bat" (
  call "Start AI Journal (Web).bat"
  exit /b
)

if exist "scripts\web_server.py" (
  echo Starting AI Journal...
  echo Your browser will open automatically.
  echo Keep this window open while using the journal.
  python "scripts\web_server.py"
) else (
  echo AI Journal files could not be found.
  echo Please read START_HERE.md or contact support.
  pause
)
