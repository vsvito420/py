# Python-Kurs für C++ Programmierer mit PyScript

Willkommen zum Python-Kurs! Dieser Kurs ist speziell für Lernende mit C++-Vorkenntnissen konzipiert und führt schrittweise in die Python-Programmierung ein. Das Besondere an diesem Kurs ist die Integration von **PyScript**, wodurch Python-Code direkt im Browser ausgeführt werden kann.

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

## Neues Feature: Interaktive Python-Umgebung mit PyScript

Dieser Kurs enthält jetzt eine interaktive Webversion mit PyScript-Integration, die es ermöglicht, Python-Code direkt im Browser auszuführen. Die Webversion ist unter [GitHub Pages](https://dein-username.github.io/py/) verfügbar.

### Vorteile der PyScript-Integration:

- Schüler können Python-Code direkt im Browser ausführen, ohne Installation
- Interaktive Beispiele und Übungen mit sofortigem Feedback
- Nahtlose Integration von Erklärungen und ausführbarem Code
- Zugänglich von jedem Gerät mit einem modernen Webbrowser

## Einrichtung der GitHub Pages-Website

Um die interaktive Webversion des Kurses einzurichten:

1. Stelle sicher, dass dein Repository öffentlich ist
2. Gehe zu den Repository-Einstellungen > Pages
3. Wähle als Source "Deploy from a branch"
4. Wähle den Branch "main" und den Ordner "/docs"
5. Klicke auf "Save"

Die Website wird unter `https://dein-username.github.io/py/` verfügbar sein.

## Hinzufügen weiterer interaktiver Module

Um weitere Module zur interaktiven Webversion hinzuzufügen:

1. Kopiere die Vorlage aus `docs/grundlagen/index.html`
2. Erstelle einen neuen Ordner für das Modul in `docs/` (z.B. `docs/kontrollstrukturen/`)
3. Passe den Inhalt an das jeweilige Modul an
4. Füge interaktive Python-Beispiele mit PyScript hinzu
5. Aktualisiere die Links in der Hauptseite (`docs/index.md`)

## Lokale Entwicklung

### Voraussetzungen

- Python 3.8 oder höher
- Git
- Visual Studio Code (empfohlen)

### Einrichtung

1. Klone das Repository:
   ```bash
   git clone https://github.com/dein-username/py.git
   cd py
   ```

2. Erstelle eine virtuelle Umgebung:
   ```bash
   python -m venv .venv
   
   # Windows:
   .venv\Scripts\activate
   # macOS/Linux:
   source .venv/bin/activate
   ```

3. Installiere die benötigten Pakete:
   ```bash
   pip install -r requirements.txt
   ```

### Lokales Testen der GitHub Pages-Website

Um die GitHub Pages-Website lokal zu testen:

1. Installiere Jekyll (benötigt Ruby):
   ```bash
   gem install bundler jekyll
   ```

2. Navigiere zum docs-Verzeichnis:
   ```bash
   cd docs
   ```

3. Starte den lokalen Server:
   ```bash
   bundle exec jekyll serve
   ```

4. Öffne http://localhost:4000 in deinem Browser

### Testen der PyScript-Integration

Um die PyScript-Integration ohne Jekyll zu testen:

1. Navigiere zum docs-Verzeichnis:
   ```bash
   cd docs
   ```

2. Starte einen einfachen HTTP-Server:
   ```bash
   # Python 3
   python -m http.server
   ```

3. Öffne http://localhost:8000 in deinem Browser

## Empfohlene VSCode-Erweiterungen

- Python (Microsoft)
- Pylint
- Python Test Explorer
- Python Docstring Generator
- Python Indent
- Jupyter
- Live Server (für lokales Testen der HTML-Seiten)
- Markdown All in One (für die Bearbeitung von Markdown-Dateien)

## Beitragen

Beiträge zum Kurs sind willkommen! Wenn du Verbesserungen oder Ergänzungen vorschlagen möchtest:

1. Forke das Repository
2. Erstelle einen Feature-Branch (`git checkout -b feature/neue-funktion`)
3. Committe deine Änderungen (`git commit -m 'Neue Funktion hinzugefügt'`)
4. Pushe zum Branch (`git push origin feature/neue-funktion`)
5. Erstelle einen Pull Request

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert - siehe die [LICENSE](LICENSE) Datei für Details.