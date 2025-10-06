@echo off
title Emulator OS
echo ===============================
echo        Emulator OS v1.0
echo ===============================
echo.
echo Type 'help' for available commands
echo Type 'exit' to quit
echo.
python emulator.py --vfs-path . --prompt "myos> "
echo.
echo Emulator has been closed.
pause