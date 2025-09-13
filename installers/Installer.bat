@echo off
REM AI Learner's Journal Kit - Windows Installer
REM Double-click this file to install the AI Journal system

title AI Learner's Journal Kit Installer

echo.
echo ========================================
echo   AI Learner's Journal Kit Installer
echo ========================================
echo.

REM Colors for output (if supported)
echo [32m[INFO][0m Checking system requirements...

REM Check if Python 3 is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [31m[ERROR][0m Python 3 is required but not installed.
    echo.
    echo Please install Python 3 from https://python.org
    echo Make sure to check "Add Python to PATH" during installation.
    echo.
    pause
    exit /b 1
)

for /f "tokens=*" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo [32m[SUCCESS][0m Python found: %PYTHON_VERSION%

REM Set up directories
set "JOURNAL_DIR=%USERPROFILE%\AI-Journal"
set "SCRIPTS_DIR=%JOURNAL_DIR%\scripts"

echo [32m[INFO][0m Setting up AI Journal directory...

if exist "%JOURNAL_DIR%" (
    echo [33m[WARNING][0m AI Journal directory already exists at %JOURNAL_DIR%
    set /p CONTINUE="Continue installation? This will not overwrite existing entries (y/n): "
    if /i not "%CONTINUE%"=="y" (
        echo Installation cancelled.
        pause
        exit /b 0
    )
) else (
    mkdir "%JOURNAL_DIR%"
    mkdir "%JOURNAL_DIR%\entries"
    mkdir "%JOURNAL_DIR%\media"
    mkdir "%SCRIPTS_DIR%"
    echo [32m[SUCCESS][0m Created AI Journal directory structure
)

REM Get the directory where this installer is located
set "INSTALLER_DIR=%~dp0"
set "BUNDLE_DIR=%INSTALLER_DIR%.."

echo [32m[INFO][0m Installing AI Journal files...

REM Copy files if they exist in the bundle
if exist "%BUNDLE_DIR%\ai-journal" (
    copy "%BUNDLE_DIR%\ai-journal" "%JOURNAL_DIR%\" >nul
    echo [32m[SUCCESS][0m Copied ai-journal CLI
) else (
    echo [33m[WARNING][0m ai-journal CLI not found in bundle
)

if exist "%BUNDLE_DIR%\scripts\*.py" (
    copy "%BUNDLE_DIR%\scripts\*.py" "%SCRIPTS_DIR%\" >nul
    echo [32m[SUCCESS][0m Copied Python scripts
) else (
    echo [33m[WARNING][0m Python scripts not found in bundle
)

REM Initialize index.json if it doesn't exist
if not exist "%JOURNAL_DIR%\index.json" (
    echo { > "%JOURNAL_DIR%\index.json"
    echo   "version": "1.0", >> "%JOURNAL_DIR%\index.json"
    echo   "created": "%date% %time%", >> "%JOURNAL_DIR%\index.json"
    echo   "entries": [], >> "%JOURNAL_DIR%\index.json"
    echo   "tags": {}, >> "%JOURNAL_DIR%\index.json"
    echo   "stats": { >> "%JOURNAL_DIR%\index.json"
    echo     "total_entries": 0, >> "%JOURNAL_DIR%\index.json"
    echo     "last_modified": "%date% %time%" >> "%JOURNAL_DIR%\index.json"
    echo   } >> "%JOURNAL_DIR%\index.json"
    echo } >> "%JOURNAL_DIR%\index.json"
    echo [32m[SUCCESS][0m Created journal index file
)

REM Create a batch wrapper for Windows
echo @echo off > "%JOURNAL_DIR%\ai-journal.bat"
echo python "%JOURNAL_DIR%\scripts\entry_saver.py" %%* >> "%JOURNAL_DIR%\ai-journal.bat"

REM Add to PATH (user environment variable)
echo [32m[INFO][0m Adding AI Journal to your PATH...

REM This requires elevated permissions, so we'll create a simple script
echo [33m[INFO][0m To use 'ai-journal' command globally, add this to your PATH:
echo   %JOURNAL_DIR%
echo.
echo Or use the full path: %JOURNAL_DIR%\ai-journal.bat
echo.

REM Test the installation
echo [32m[INFO][0m Testing installation...

python "%SCRIPTS_DIR%\entry_saver.py" --help >nul 2>&1
if %errorlevel% equ 0 (
    echo [32m[SUCCESS][0m AI Journal scripts are working!
) else (
    echo [31m[ERROR][0m Installation test failed. Please check the setup manually.
    pause
    exit /b 1
)

echo.
echo [32m========================================[0m
echo [32m   Installation completed successfully![0m
echo [32m========================================[0m
echo.

echo [36mNext steps:[0m
echo 1. Add %JOURNAL_DIR% to your system PATH for global access
echo 2. Or use: %JOURNAL_DIR%\ai-journal.bat new "My First Entry" learning
echo 3. Read the Quick Start guide in docs\Quick_Start.md
echo.

echo [32mHappy learning! 🚀[0m
echo.

REM Optional: Create a sample entry
set /p CREATE_SAMPLE="Would you like to create a sample journal entry? (y/n): "
if /i "%CREATE_SAMPLE%"=="y" (
    echo [32m[INFO][0m Creating sample entry...
    python "%SCRIPTS_DIR%\entry_saver.py" "Getting Started with AI Journal - Windows" tutorial learning windows
    echo [32m[SUCCESS][0m Sample entry created!
)

echo.
echo Installation complete. You can close this window.
pause
