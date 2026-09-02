@echo off
REM Jarvis AI - Automated Windows Installer
REM This script will install and run Jarvis AI

echo.
echo ================================================
echo     JARVIS AI - Automated Installer
echo     Owner: Doctor Yusuph Mponzi
echo ================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please download Python from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

echo [1/5] Python found!
echo.

REM Create virtual environment
echo [2/5] Creating virtual environment...
python -m venv venv
call venv\Scripts\activate.bat

REM Upgrade pip
echo [3/5] Upgrading pip...
python -m pip install --upgrade pip

REM Install dependencies
echo [4/5] Installing dependencies (this may take 2-3 minutes)...
pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo ERROR: Failed to install dependencies
    echo Trying alternative PyAudio installation...
    pip install pipwin
    pipwin install pyaudio
    pip install -r requirements.txt
)

echo.
echo [5/5] Installation complete!
echo.
echo ================================================
echo     STARTING JARVIS AI
echo ================================================
echo.
echo Speak your commands clearly. Examples:
echo  - "What time is it?"
echo  - "Tell me the date"
echo  - "Open browser"
echo  - "Search for [topic]"
echo  - "Goodbye" (to exit)
echo.

REM Run Jarvis
python jarvis.py

pause
