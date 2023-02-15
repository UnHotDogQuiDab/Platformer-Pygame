@echo off
:retry
pip install pygame --pre
IF %ERRORLEVEL% NEQ 0 goto fix
pip install pytmx --pre
python.exe main.py
pause
exit

:fix
echo "Python is not installed"
echo "Download python and press a key"
python.exe
pause
goto retry