@echo off
title elimNMS Server
color 0A
echo.
echo ================================
echo    elimNMS Network Management
echo ================================
echo.
echo Starting elimNMS server...
echo Please wait...
echo.

cd /d "C:\Users\user\Downloads\elim-NMS\elimNMS-public"

echo Starting Flask application at http://localhost:5000
echo Press Ctrl+C to stop the server
echo.

"C:\Users\user\Downloads\elim-NMS\.venv\Scripts\python.exe" app.py

echo.
echo ================================
echo Server has been stopped.
echo ================================
pause