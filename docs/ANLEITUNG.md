# Anleitung: Interaktive Python-Lehrmaterialien mit GitHub Pages und PyScript

Diese Anleitung erklärt, wie du die interaktiven Python-Lehrmaterialien auf GitHub Pages deployen und lokal mit Jekyll testen kannst.

## 1. Deployment mit GitHub Actions (empfohlen)

Die einfachste Methode, um die Seite auf GitHub Pages zu deployen, ist die Verwendung von GitHub Actions. Ich habe bereits eine Workflow-Datei erstellt, die automatisch die Jekyll-Seite baut und auf GitHub Pages deployt.

Folge diesen Schritten, um GitHub Actions zu aktivieren:

1. Gehe zu deinem GitHub Repository (`https://github.com/v.skolan/py`)
2. Klicke auf "Settings" (Zahnrad-Symbol)
3. Klicke im linken Menü auf "Pages"
4. Wähle unter "Build and deployment" > "Source" die Option "GitHub Actions" aus
5. Klicke auf "Save"

Bei jedem Push in den main-Branch wird die Seite automatisch gebaut und auf GitHub Pages deployt. Die Seite wird unter `https://v.skolan.github.io/py/` verfügbar sein.

Der Workflow führt folgende Schritte aus:
- Checkout des Repositories
- Einrichtung von Ruby und Jekyll
- Bau der Jekyll-Seite
- Deployment auf GitHub Pages

Du kannst den Status des Workflows unter dem Tab "Actions" in deinem Repository verfolgen.

## 2. Manuelle Aktivierung von GitHub Pages (alternative Methode)

Alternativ kannst du GitHub Pages auch manuell aktivieren:

1. Gehe zu deinem GitHub Repository (`https://github.com/v.skolan/py`)
2. Klicke auf "Settings" (Zahnrad-Symbol)
3. Scrolle nach unten zum Abschnitt "GitHub Pages"
4. Wähle unter "Source" den Branch "main" und den Ordner "/docs" aus
5. Klicke auf "Save"

GitHub Pages wird nun automatisch deine Markdown-Dateien mit Jekyll verarbeiten und als HTML-Seiten bereitstellen. Die Seite wird unter `https://v.skolan.github.io/py/` verfügbar sein.

## 3. Lokales Testen mit Jekyll (optional)

Um die Seite lokal mit Jekyll zu testen, benötigst du:

1. Ruby (https://www.ruby-lang.org/de/downloads/)
2. RubyGems (wird mit Ruby installiert)
3. Jekyll und Bundler

### Installation von Jekyll und Bundler

```bash
# Installation von Jekyll und Bundler
gem install jekyll bundler

# Wechsle in das docs-Verzeichnis
cd docs

# Installiere die Abhängigkeiten
bundle install
```

### Lokalen Server starten

```bash
# Starte den lokalen Jekyll-Server
bundle exec jekyll serve
```

Die Seite ist dann unter `http://localhost:4000` verfügbar.

## 4. Hinzufügen neuer Inhalte

Um neue Inhalte hinzuzufügen, folge diesen Schritten:

1. Erstelle eine neue Markdown-Datei im entsprechenden Verzeichnis (z.B. `docs/kontrollstrukturen/index.md`)
2. Füge YAML-Frontmatter am Anfang der Datei hinzu:
   ```yaml
   ---
   layout: default
   title: Dein Seitentitel
   ---
   ```
3. Füge den Inhalt hinzu, einschließlich interaktiver Python-Beispiele:
   ```markdown
   <div class="pyscript-example">
   <pre><code class="language-python">
   # Dein Python-Code hier
   print("Hallo, Welt!")
   </code></pre>
   </div>
   ```
4. Füge Übungen hinzu:
   ```markdown
   <div class="pyscript-exercise">
   <pre><code class="language-python">
   # TODO: Deine Übungsaufgabe hier
   
   </code></pre>
   </div>
   ```

## 5. Anpassen des Designs

Das Design kann über folgende Dateien angepasst werden:

- `docs/_layouts/default.html` - Das Hauptlayout
- `docs/assets/css/style.css` - CSS für das Styling
- `docs/assets/js/pyscript-helper.js` - JavaScript für die PyScript-Integration

## 6. Hinzufügen von Python-Paketen

Um zusätzliche Python-Pakete für PyScript verfügbar zu machen, bearbeite die `docs/_includes/pyscript.html`-Datei und füge die Pakete zur `packages`-Liste hinzu:

```html
<py-config>
    packages = ["numpy", "matplotlib", "pandas"]
</py-config>
```

## 7. Fehlerbehebung

### PyScript lädt nicht

Wenn PyScript nicht lädt, überprüfe die Konsole des Browsers auf Fehlermeldungen. Häufige Probleme sind:

- Falsche URLs zu PyScript-Dateien
- Fehler im JavaScript-Code
- Probleme mit der Internetverbindung

### Jekyll-Fehler

Wenn Jekyll-Fehler auftreten, überprüfe:

- Die YAML-Frontmatter (muss korrekt formatiert sein)
- Die Verzeichnisstruktur
- Die _config.yml-Datei

### GitHub Actions Fehler

Wenn der GitHub Actions Workflow fehlschlägt, überprüfe:

- Die Logs unter dem Tab "Actions" in deinem Repository
- Die Gemfile-Datei im docs-Verzeichnis
- Die _config.yml-Datei

## 8. Ressourcen

- [PyScript Dokumentation](https://pyscript.net/docs/)
- [Jekyll Dokumentation](https://jekyllrb.com/docs/)
- [GitHub Pages Dokumentation](https://docs.github.com/de/pages)
- [GitHub Actions Dokumentation](https://docs.github.com/de/actions)
- [Markdown Guide](https://www.markdownguide.org/)