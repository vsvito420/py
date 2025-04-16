@echo off
echo Python-Lernwebseite - Lokaler Server
echo ===================================
echo.
echo Bitte waehlen Sie eine Option:
echo 1. Jekyll-Server starten (empfohlen, benoetigt Ruby und Jekyll)
echo 2. Python HTTP-Server starten (einfach, benoetigt nur Python)
echo.
set /p option="Option (1 oder 2): "

if "%option%"=="1" (
    echo.
    echo Starte Jekyll-Server...
    echo.
    cd docs
    bundle exec jekyll serve --livereload
) else if "%option%"=="2" (
    echo.
    echo Starte Python HTTP-Server...
    echo.
    cd docs
    python -m http.server 4000
) else (
    echo.
    echo Ungueltige Option. Bitte 1 oder 2 eingeben.
    pause
    exit /b 1
)

pause