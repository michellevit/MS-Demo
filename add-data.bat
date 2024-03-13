:: reset-database.bat
:: scheduled to run automatically every 10 minutes via the Heroku Scheduler add-on

@echo off
setlocal EnableDelayedExpansion

echo Running batch scripts for Django management commands...
cd ..
cd ..
cd ..
REM Set the base path to the root directory of your Django project
set "basePath=%~dp0"

REM Check if logged in to Heroku
echo Checking Heroku login status...
call heroku auth:whoami
if errorlevel 1 (
    echo Not logged in to Heroku. Please log in...
    call heroku login
    if errorlevel 1 (
        echo Failed to log in to Heroku.
        exit /b
    )
)

REM Navigate back to the directory containing this script
cd /d "%basePath%"

echo %basepath%
:: REM Run Django management commands (in api/management/commands)
echo Updating db data...
"%basePath%\venv\Scripts\python.exe" manage.py new_bucket

