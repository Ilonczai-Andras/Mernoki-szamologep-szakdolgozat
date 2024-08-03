@echo off
REM Navigate to the directory containing setup.py
cd /d D:\Andreas\Szakdolgozat\Mernoki-szamologep-szakdolgozat\Engineering calculator

REM Run the Python setup script with the build command
python setup.py build

REM Optionally, check if the script executed successfully
if %errorlevel% equ 0 (
    echo Python setup script executed successfully.
) else (
    echo Python setup script failed to execute.
)
pause
