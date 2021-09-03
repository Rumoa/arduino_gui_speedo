
@Echo off
Pushd "%~dp0"
title This is your first batch script!
start python arduino_stuff.py
start python gui.py
pause