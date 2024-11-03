@echo off

:: Set the program name (replace with your program's .exe name)
set "programName=Multihack.py"

:: Set the icon file name (replace with your icon file name)
set "iconName=icon.ico"

:: Get the program name without the extension
for %%i in ("%programName%") do set "shortcutName=%%~ni"

:: Create the shortcut on the desktop
set "shortcutPath=%USERPROFILE%\Desktop\%shortcutName%.lnk"

:: Use PowerShell to create the shortcut with a custom icon
powershell "$s=(New-Object -COM WScript.Shell).CreateShortcut('%shortcutPath%'); $s.TargetPath='%cd%\%programName%'; $s.WorkingDirectory='%cd%'; $s.IconLocation='%cd%\%iconName%'; $s.Save()"

echo Shortcut created on the desktop as "%shortcutName%.lnk" with custom icon.
exit