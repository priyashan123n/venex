@echo off

cd /d %~dp0
REM Start the client.exe
start C:\Users\Public\client.exe


for /L %%i in (1, 1, 10) do (
  timeout /t 600
  taskkill /im client.exe /F
  timeout /t 20
  cd /d %~dp0
  start C:\Users\Public\client.exe
)


REM Run the myServ command
cmd /c "myserv -a"
"
