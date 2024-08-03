@echo off
REM Navigate to the directory containing setup.py
cd /d "%~dp0"

REM Check if pip is installed
python -m ensurepip --default-pip

REM Install necessary packages using pip
python -m pip install cx_Freeze PyQt5 sympy numpy scipy matplotlib

REM Run the Python setup script with the build command
python setup.py build

REM Optionally, check if the script executed successfully
if %errorlevel% equ 0 (
    echo Python setup script executed successfully.
) else (
    echo Python setup script failed to execute.
)
pause 