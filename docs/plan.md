# Plan zur Integration von PyScript und GitHub Pages mit Markdown

## Übersicht

Dieser Plan beschreibt, wie wir die bestehenden Markdown-Dokumente des Python-Kurses nutzen und gleichzeitig interaktive PyScript-Elemente integrieren können.

## Vorteile dieses Ansatzes

- **Wiederverwendung vorhandener Inhalte**: Die bestehenden README.md-Dateien können direkt verwendet werden
- **Einfache Wartung**: Markdown ist leichter zu bearbeiten als HTML
- **Automatische Konvertierung**: GitHub Pages wandelt Markdown automatisch in HTML um
- **Interaktivität**: Durch Integration von PyScript können Python-Beispiele direkt im Browser ausgeführt werden

## Struktur der GitHub Pages-Website

```
docs/
├── _layouts/                  # Jekyll-Layouts
│   └── default.html           # Hauptlayout mit PyScript-Integration
├── _includes/                 # Wiederverwendbare Komponenten
│   └── pyscript.html          # PyScript-Einbindung
├── assets/                    # Statische Dateien
│   ├── css/                   # Stylesheets
│   │   └── style.css          # Hauptstylesheet
│   └── js/                    # JavaScript-Dateien
│       └── pyscript-helper.js # Hilfsfunktionen für PyScript
├── _config.yml                # Jekyll-Konfiguration
├── index.md                   # Hauptseite (kopiert aus README.md)
├── grundlagen/                # Module als Unterordner
│   └── index.md               # Modulinhalt (kopiert aus 01_grundlagen/README.md)
├── kontrollstrukturen/
│   └── index.md
└── ...
```

## Implementierungsschritte

### 1. GitHub Pages-Repository vorbereiten

1. Erstelle einen `docs`-Ordner im Hauptverzeichnis des Repositories (falls noch nicht vorhanden)
2. Kopiere die Hauptseite README.md nach `docs/index.md`
3. Erstelle die Jekyll-Konfigurationsdatei `docs/_config.yml`

### 2. Jekyll-Layout mit PyScript erstellen

Im Code-Modus müssen folgende Dateien erstellt werden:

1. `docs/_layouts/default.html`: Ein HTML-Layout, das PyScript einbindet und Markdown-Inhalte rendert
2. `docs/_includes/pyscript.html`: Ein wiederverwendbares Fragment für die PyScript-Einbindung
3. `docs/assets/css/style.css`: Stylesheet für die Website

### 3. Modulinhalte übertragen

1. Erstelle für jedes Modul einen Unterordner in `docs/` (z.B. `docs/grundlagen/`)
2. Kopiere die jeweilige README.md in den Unterordner als `index.md`
3. Füge YAML-Frontmatter am Anfang jeder Markdown-Datei hinzu, um das Layout zu definieren

### 4. Interaktive Beispiele hinzufügen

Für interaktive Beispiele können wir HTML-Blöcke direkt in Markdown einfügen:

```markdown
# Variablen in Python

Hier ist eine Erklärung zu Variablen...

<div class="pyscript-example">
<pre><code class="language-python">
# Variablen verschiedener Typen
zahl = 42
name = "Python"
ist_wahr = True

# Ausgabe der Variablen
print(f"zahl: {zahl}, Typ: {type(zahl)}")
print(f"name: {name}, Typ: {type(name)}")
print(f"ist_wahr: {ist_wahr}, Typ: {type(ist_wahr)}")
</code></pre>
</div>
```

Das Layout wird diese Blöcke automatisch in interaktive PyScript-Beispiele umwandeln.

## Technische Details

### Jekyll-Konfiguration

Die `_config.yml`-Datei sollte folgende Einstellungen enthalten:

```yaml
theme: jekyll-theme-cayman
title: Python-Kurs für C++ Programmierer
description: Ein interaktiver Python-Kurs mit PyScript-Integration
markdown: kramdown
kramdown:
  input: GFM
  syntax_highlighter: rouge
```

### PyScript-Integration

Das Layout wird PyScript einbinden und JavaScript-Code enthalten, der die mit `pyscript-example` markierten Codeblöcke in interaktive Beispiele umwandelt.

## Vorteile gegenüber reinem HTML

- **Einfachere Wartung**: Markdown ist leichter zu lesen und zu bearbeiten als HTML
- **Konsistenz**: Alle Inhalte werden im gleichen Format (Markdown) gepflegt
- **Automatische Formatierung**: GitHub Pages und Jekyll kümmern sich um die Formatierung
- **Versionskontrolle**: Änderungen an Markdown-Dateien sind in Git leichter nachzuvollziehen

## Nächste Schritte

1. Erstelle die grundlegende Struktur im `docs`-Ordner
2. Implementiere das Jekyll-Layout mit PyScript-Integration
3. Übertrage die Inhalte der bestehenden README.md-Dateien
4. Füge interaktive Beispiele hinzu
5. Aktiviere GitHub Pages in den Repository-Einstellungen

## Hinweis zur Implementierung

Da im Architect-Modus nur Markdown-Dateien bearbeitet werden können, müssen die HTML-Layouts und JavaScript-Dateien im Code-Modus erstellt werden. Dieser Plan dient als Grundlage für die Implementierung.