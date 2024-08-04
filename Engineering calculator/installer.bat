@echo off
REM Navigate to the directory containing setup.py
cd /d "%~dp0"
echo Current directory: %cd%

REM Check if python is installed
echo Checking for python...
where python >nul 2>&1
if %errorlevel% equ 0 (
    echo Python found. Using python...
    echo Installing packages with python...
    python -m ensurepip --default-pip
    if %errorlevel% neq 0 (
        echo Failed to ensure pip with python.
        pause
        exit /b 1
    )
    python -m pip install cx_Freeze==7.2.0 PyQt5==5.15.10 sympy==1.12 numpy==1.26.4 scipy==1.14.0 matplotlib==3.8.3
    if %errorlevel% neq 0 (
        echo Failed to install packages with python.
        pause
        exit /b 1
    )
    python setup.py build
    if %errorlevel% equ 0 (
        echo Python setup script executed successfully.
    ) else (
        echo Python setup script failed to execute.
    )
    goto :end
)

REM Check if py is installed
echo Checking for py...
where py >nul 2>&1
if %errorlevel% equ 0 (
    echo Py found. Using py...
    echo Installing packages with py...
    py -m ensurepip --default-pip
    if %errorlevel% neq 0 (
        echo Failed to ensure pip with py.
        pause
        exit /b 1
    )
    py -m pip install cx_Freeze==7.2.0 PyQt5==5.15.10 sympy==1.12 numpy==1.26.4 scipy==1.14.0 matplotlib==3.8.3
    if %errorlevel% neq 0 (
        echo Failed to install packages with py.
        pause
        exit /b 1
    )
    py setup.py build
    if %errorlevel% equ 0 (
        echo Python setup script executed successfully.
    ) else (
        echo Python setup script failed to execute.
    )
    goto :end
)

REM If neither python nor py is found, display an error message
echo Neither python nor py command is available.
pause
exit /b 1

:end
REM Pause to keep the window open
pause
