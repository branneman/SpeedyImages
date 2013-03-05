@echo off
setlocal

:: Check if Python is installed
set PATH=%PATH%
for %%P in ( python.exe ) do set PYTHON=%%~f$PATH:P
if not exist "%PYTHON%" goto nopython

:: Check if Python is version 3.3 or higher
python.exe -c "import sys; (exit(0) if sys.version_info >= (3, 3) else exit(1))"
if %errorlevel% GEQ 1 goto nopython

python.exe lib/speedypng.py %*
if %errorlevel% GEQ 1 exit %errorlevel%
exit

:nopython
echo Python version 3.3 or higher is required.
echo  Download from: http://www.python.org/download/