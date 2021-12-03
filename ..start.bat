@echo off
rem echo (Project) Loading
rem python\python.exe .init.py
python\python.exe .clean.py
echo (Project) Start
echo.
python\python.exe .
echo.
echo (Project) End
python\python.exe .clean.py
pause