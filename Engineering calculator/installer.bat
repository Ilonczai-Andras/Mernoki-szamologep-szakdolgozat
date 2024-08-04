@echo off
REM Navigate to the directory containing setup.py
cd /d "%~dp0"

REM Function to check if pip is installed and install packages
:install_packages
    %1 -m ensurepip --default-pip
    %1 -m pip install cx_Freeze==7.2.0 PyQt5==5.15.10 sympy==1.12 numpy==1.26.4 scipy==1.14.0 matplotlib==3.8.3
    exit /b

REM Check if python is installed
where python >nul 2>&1
if %errorlevel% equ 0 (
    call :install_packages python
    python setup.py build
    goto :end
)

REM Check if py is installed
where py >nul 2>&1
if %errorlevel% equ 0 (
    call :install_packages py
    py setup.py build
    goto :end
)

REM If neither python nor py is found, display an error message
echo Neither python nor py command is available.
exit /b 1

:end
REM Optionally, check if the script executed successfully
if %errorlevel% equ 0 (
    echo Python setup script executed successfully.
) else (
    echo Python setup script failed to execute.
)
pause