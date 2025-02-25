@echo off
chcp 65001 > nul
cd /d "%~dp0"
echo Checking Python installation...

:: Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python not found! Please install Python 3.x and add it to PATH.
    echo You can download Python from https://www.python.org/downloads/
    pause
    exit /b 1
)

echo Checking Python virtual environment...

if not exist ".venv\Scripts\activate.bat" (
    echo Virtual environment not found, creating...
    python -m venv .venv
    if errorlevel 1 (
        echo Failed to create virtual environment! Please make sure Python 3.x is installed.
        echo Error code: %errorlevel%
        pause
        exit /b 1
    )
    echo Virtual environment created successfully.
)

echo Activating virtual environment...
call .venv\Scripts\activate.bat
if errorlevel 1 (
    echo Failed to activate virtual environment!
    pause
    exit /b 1
)

:: Install or upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip

:: Install required packages
echo Installing required packages...
pip install pyOpenSSL cryptography

echo Running PEM Generator...
python pem_generator.py
if errorlevel 1 (
    echo Program error, code: %errorlevel%
    echo Please check if OpenSSL is installed.
    echo You can download OpenSSL from https://slproweb.com/products/Win32OpenSSL.html
)

echo Deactivating virtual environment...
call deactivate

echo Press any key to exit...
pause 