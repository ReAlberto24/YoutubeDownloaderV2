@echo off
echo (Project) Loading
python\python.exe .init.py
python\python.exe .clean.py
echo (Project) Start
echo.
python\python.exe .
echo.
echo (Project) End
python\python.exe .clean.py
pause