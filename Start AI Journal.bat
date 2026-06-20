@echo off
REM Double-click launcher for the beginner AI Journal menu.

title AI Journal

set "LAUNCHER_DIR=%~dp0"

if exist "%USERPROFILE%\AI-Journal\ai-journal.bat" (
    call "%USERPROFILE%\AI-Journal\ai-journal.bat" menu
) else if exist "%LAUNCHER_DIR%scripts\journal_cli.py" (
    python "%LAUNCHER_DIR%scripts\journal_cli.py" menu
) else (
    echo AI Journal is not installed yet.
    echo Run installers\Installer.bat first.
)

echo.
pause
