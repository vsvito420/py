# Python-Kurs für C++ Programmierer

Willkommen zum Python-Kurs! Dieser Kurs ist speziell für Lernende mit C++-Vorkenntnissen konzipiert und führt schrittweise in die Python-Programmierung ein.

## Kursstruktur

Der Kurs ist in folgende Module unterteilt:

1. [**Grundlagen**](01_grundlagen/README.md): Variablen, Datentypen, Operatoren, Ein-/Ausgabe
2. [**Kontrollstrukturen**](02_kontrollstrukturen/README.md): Bedingungen, Schleifen, List Comprehensions
3. [**Funktionen**](03_funktionen/README.md): Definition, Parameter, Rekursion
4. [**Datenstrukturen**](04_datenstrukturen/README.md): Listen, Dictionaries, Sets, Tuples
5. [**Objektorientierung**](05_objektorientierung/README.md): Klassen, Vererbung
6. [**Module und Pakete**](06_module_und_pakete/README.md): Eigene Module, Standardbibliothek
7. [**Dateien**](07_dateien/README.md): Lesen und Schreiben von Dateien
8. [**Ausnahmebehandlung**](08_ausnahmebehandlung/README.md): Try/Except
9. [**Projekte**](09_projekte/README.md): Praktische Anwendungen

## Schnellzugriff auf wichtige Themen

### Grundlagen
- [Variablen](01_grundlagen/01_variablen.py)
- [Datentypen](01_grundlagen/02_datentypen.py)
- [Operatoren](01_grundlagen/03_operatoren.py)
- [Ein-/Ausgabe](01_grundlagen/04_eingabe_ausgabe.py)

### Kontrollstrukturen
- [If/Else](02_kontrollstrukturen/01_if_else.py)
- [Schleifen](02_kontrollstrukturen/02_schleifen.py)
- [List Comprehensions](02_kontrollstrukturen/03_listen_comprehension.py)

### Funktionen
- [Funktionsgrundlagen](03_funktionen/01_funktionen_grundlagen.py)
- [Parameter](03_funktionen/02_parameter.py)
- [Rekursion](03_funktionen/03_rekursion.py)

### Datenstrukturen
- [Listen](04_datenstrukturen/01_listen.py)
- [Dictionaries](04_datenstrukturen/02_dictionaries.py)
- [Sets](04_datenstrukturen/03_sets.py)
- [Tuples](04_datenstrukturen/04_tuples.py)

### Objektorientierung
- [Klassen](05_objektorientierung/01_klassen.py)
- [Vererbung](05_objektorientierung/02_vererbung.py)

### Module und Pakete
- [Eigene Module](06_module_und_pakete/01_eigene_module.py)
- [Standardbibliothek](06_module_und_pakete/02_standard_bibliothek.py)

### Dateien und Ausnahmebehandlung
- [Dateien lesen und schreiben](07_dateien/01_lesen_schreiben.py)
- [Try/Except](08_ausnahmebehandlung/01_try_except.py)

### Übungen
- [Übungsaufgaben](übungen/README.md)

## Einrichtung der Entwicklungsumgebung

### Installation von Python

1. Lade Python von [python.org](https://www.python.org/downloads/) herunter
2. Installiere Python mit der Option "Add Python to PATH"
3. Überprüfe die Installation mit `python --version` im Terminal

### Virtuelle Umgebung einrichten

```bash
# Erstellen der virtuellen Umgebung
python -m venv .venv

# Aktivieren der Umgebung
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Installation der benötigten Pakete
pip install -r requirements.txt
```

### Empfohlene VSCode-Erweiterungen

- Python (Microsoft)
- Pylint
- Python Test Explorer
- Python Docstring Generator
- Python Indent

## Wie man diesen Kurs nutzt

1. Arbeite die Module der Reihe nach durch
2. Jedes Modul enthält Beispielcode und Übungen
3. Löse die Übungen selbstständig
4. Vergleiche deine Lösungen mit den Musterlösungen im Ordner `übungen/lösungen`
5. Wende das Gelernte in den Projekten an

## Unterschiede zu C++

Dieser Kurs hebt die wichtigsten Unterschiede zwischen Python und C++ hervor:

- Python verwendet Einrückungen statt geschweifter Klammern
- Dynamische Typisierung statt statischer Typisierung
- Automatische Speicherverwaltung
- Alles ist ein Objekt
- Einfachere Syntax mit weniger Boilerplate-Code

## Ressourcen

- [Offizielle Python-Dokumentation](https://docs.python.org/de/3/)
- [Python für C++-Programmierer](https://realpython.com/python-vs-cpp/)
- [Python Cheat Sheet](https://www.pythoncheatsheet.org/)