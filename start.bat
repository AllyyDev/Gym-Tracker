@echo off

setlocal
set SCRIPT_DIR=%~dp0

start "" cmd /k "cd /d "%SCRIPT_DIR%" && python -m uvicorn backend.main:app --reload --port 8000 || (echo Uvicorn not found - installing... & python -m pip install uvicorn[standard] && python -m uvicorn backend.main:app --reload --port 8000)"

REM open frontend
start "" "%SCRIPT_DIR%frontend\index.html"

endlocal
exit /b
