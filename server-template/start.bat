@echo off
cd /d "%~dp0"
title GT-Cataclysm Server

set PACK_URL=https://raw.githubusercontent.com/ManHazz/GT-Cataclysm/pack/pack.toml

rem ---- Backup world on each start ----
if not exist backups mkdir backups

if exist world (
    powershell -NoProfile -Command "Compress-Archive -Path 'world' -DestinationPath ('backups\world-' + (Get-Date -Format 'yyyyMMdd-HHmmss') + '.zip') -Force"
    powershell -NoProfile -Command "Get-ChildItem -Path 'backups\world-*.zip' | Sort-Object Name -Descending | Select-Object -Skip 7 | Remove-Item -Force"
)

rem ---- Server loop ----
:loop
rem Update mods/config from the published pack before every launch.
rem Needs packwiz-installer-bootstrap.jar in this folder.
java -jar packwiz-installer-bootstrap.jar -g -s server %PACK_URL%
if errorlevel 1 echo WARNING: pack update failed, continuing with current files.

java @user_jvm_args.txt @libraries/net/minecraftforge/forge/1.20.1-47.4.13/win_args.txt nogui
echo Server stopped. Restarting in 10s - press Ctrl+C to quit.
timeout /t 10
goto loop
