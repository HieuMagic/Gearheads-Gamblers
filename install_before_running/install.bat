@echo off
set PYTHON_VERSION=3.9.7
set PYTHON_INSTALL_DIR=C:\Python

echo Installing Python %PYTHON_VERSION%...

rem Download Python installer
curl -o python-installer.exe https://www.python.org/ftp/python/%PYTHON_VERSION%/python-%PYTHON_VERSION%-amd64.exe

rem Install Python silently
python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

pip install pygame

rem Clean up installer
del python-installer.exe

echo Python %PYTHON_VERSION% has been installed successfully.