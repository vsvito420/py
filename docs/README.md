# Python-Kurs für C++ Programmierer mit PyScript

Willkommen zum Python-Kurs! Dieser Kurs ist speziell für Lernende mit C++-Vorkenntnissen konzipiert und führt schrittweise in die Python-Programmierung ein. Das Besondere an diesem Kurs ist die Integration von **PyScript**, wodurch Python-Code direkt im Browser ausgeführt werden kann.

## Kursstruktur

Der Kurs ist in folgende Module unterteilt:

1. [**Grundlagen**](grundlagen/index.html): Variablen, Datentypen, Operatoren, Ein-/Ausgabe
2. [**Kontrollstrukturen**](kontrollstrukturen/index.html): Bedingungen, Schleifen, List Comprehensions
3. [**Funktionen**](funktionen/index.html): Definition, Parameter, Rekursion
4. [**Datenstrukturen**](datenstrukturen/index.html): Listen, Dictionaries, Sets, Tuples
5. [**Objektorientierung**](objektorientierung/index.html): Klassen, Vererbung
6. [**Module und Pakete**](module_und_pakete/index.html): Eigene Module, Standardbibliothek
7. [**Dateien**](dateien/index.html): Lesen und Schreiben von Dateien
8. [**Ausnahmebehandlung**](ausnahmebehandlung/index.html): Try/Except
9. [**Projekte**](projekte/index.html): Praktische Anwendungen

## Neues Feature: Interaktive Python-Umgebung mit PyScript

Dieser Kurs enthält jetzt eine interaktive Webversion mit PyScript-Integration, die es ermöglicht, Python-Code direkt im Browser auszuführen.

### Vorteile der PyScript-Integration:

- Schüler können Python-Code direkt im Browser ausführen, ohne Installation
- Interaktive Beispiele und Übungen mit sofortigem Feedback
- Nahtlose Integration von Erklärungen und ausführbarem Code
- Zugänglich von jedem Gerät mit einem modernen Webbrowser

## Lokales Testen

Es gibt mehrere Möglichkeiten, die Webseite lokal zu testen:

### Option 1: Mit Jekyll (empfohlen)

Wenn Sie Jekyll installiert haben, können Sie den Jekyll-Server starten:

1. Öffnen Sie das Projekt in VS Code
2. Drücken Sie `F5` und wählen Sie "Jekyll Serve" aus der Dropdown-Liste
3. Der Browser öffnet sich automatisch mit der lokalen Webseite

Alternativ können Sie folgende Befehle in der Kommandozeile ausführen:

```bash
cd docs
bundle install
bundle exec jekyll serve --livereload
```

Die Webseite ist dann unter http://localhost:4000 verfügbar.

### Option 2: Mit Python HTTP-Server

Wenn Sie Jekyll nicht installiert haben, können Sie einen einfachen Python-HTTP-Server verwenden:

1. Öffnen Sie das Projekt in VS Code
2. Drücken Sie `F5` und wählen Sie "Python HTTP Server" aus der Dropdown-Liste
3. Der Browser öffnet sich automatisch mit der lokalen Webseite

Alternativ können Sie folgende Befehle in der Kommandozeile ausführen:

```bash
cd docs
python -m http.server 4000
```

Die Webseite ist dann unter http://localhost:4000 verfügbar.

## Projektstruktur

- `docs/`: Hauptverzeichnis der Webseite
  - `_layouts/`: Jekyll-Layouts
  - `assets/`: CSS, JavaScript und andere Assets
    - `css/`: CSS-Dateien
    - `js/`: JavaScript-Dateien
  - `anleitungen/`: Python-Dateien für die Lernmodule
    - `01_grundlagen/`: Grundlagen-Module
    - `02_kontrollstrukturen/`: Kontrollstrukturen-Module
    - usw.
  - `grundlagen/`, `kontrollstrukturen/`, usw.: Markdown-Dateien für die einzelnen Seiten

## Hinweise zur Entwicklung

- Die Webseite verwendet Jekyll, ein statisches Site-Generator
- PyScript wird verwendet, um Python-Code im Browser auszuführen
- Die Code-Loader-Funktionalität lädt Python-Dateien und zeigt sie auf der Webseite an
- Die Code-Execution-Funktionalität ermöglicht die Ausführung von Code in der rechten Spalte

## Bekannte Probleme

- PyScript kann in manchen Browsern langsam sein
- Die `input()`-Funktion funktioniert in PyScript nicht wie in einer normalen Python-Umgebung