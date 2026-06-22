@echo off
REM Double-click launcher for the friendly AI Journal WEB UI.
REM Starts a tiny local server and opens it in your browser.

title AI Journal (Web)

set "LAUNCHER_DIR=%~dp0"

if exist "%LAUNCHER_DIR%scripts\web_server.py" (
    echo Starting AI Journal ^(web^)...
    echo Your browser will open automatically. Keep this window open while you write.
    echo When you're done, click this window and press Ctrl-C to stop.
    echo.
    python "%LAUNCHER_DIR%scripts\web_server.py"
) else (
    echo AI Journal is not installed yet.
    echo Run installers\Installer.bat first.
)

echo.
pause
