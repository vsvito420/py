#!/bin/bash

echo "Python-Lernwebseite - Lokaler Server"
echo "==================================="
echo
echo "Bitte wählen Sie eine Option:"
echo "1. Jekyll-Server starten (empfohlen, benötigt Ruby und Jekyll)"
echo "2. Python HTTP-Server starten (einfach, benötigt nur Python)"
echo

read -p "Option (1 oder 2): " option

if [ "$option" = "1" ]; then
    echo
    echo "Starte Jekyll-Server..."
    echo
    cd docs
    bundle exec jekyll serve --livereload
elif [ "$option" = "2" ]; then
    echo
    echo "Starte Python HTTP-Server..."
    echo
    cd docs
    python -m http.server 4000
else
    echo
    echo "Ungültige Option. Bitte 1 oder 2 eingeben."
    read -p "Drücken Sie eine Taste, um fortzufahren..."
    exit 1
fi

read -p "Drücken Sie eine Taste, um fortzufahren..."