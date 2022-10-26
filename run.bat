@echo off
set exis=0
if EXIST .\dist\main.exe set exis=1
if %exis%==0 (
    echo Building
    pyinstaller -F main.py
)
.\dist\main.exe