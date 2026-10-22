@echo off
title Novel Factory - Web Dashboard
setlocal enabledelayedexpansion

cd /d "%~dp0"

set "PROJECT=the_ranch_maid_heiress"
if not "%~1"=="" set "PROJECT=%~1"

echo ===================================================
echo   Novel Factory - Local Production Dashboard
echo ===================================================
echo.
echo Project: %PROJECT%
echo Starting local server and opening browser...
echo (Keep this window open while using the dashboard)
echo.

call "%~dp0novelfactory.bat" dashboard "%PROJECT%" --serve --open

if errorlevel 1 (
    echo.
    echo [ERROR] Failed to start Novel Factory dashboard.
    echo.
    pause
)
