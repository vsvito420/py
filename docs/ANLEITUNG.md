# Anleitung: Interaktive Python-Lehrmaterialien mit GitHub Pages und PyScript

Diese Anleitung erklärt, wie du die interaktiven Python-Lehrmaterialien auf GitHub Pages deployen und lokal mit Jekyll testen kannst.

## 1. GitHub Pages aktivieren

Um die Seite auf GitHub Pages zu deployen, folge diesen Schritten:

1. Gehe zu deinem GitHub Repository (`https://github.com/vsvito420/py`)
2. Klicke auf "Settings" (Zahnrad-Symbol)
3. Scrolle nach unten zum Abschnitt "GitHub Pages"
4. Wähle unter "Source" den Branch "main" und den Ordner "/docs" aus
5. Klicke auf "Save"

GitHub Pages wird nun automatisch deine Markdown-Dateien mit Jekyll verarbeiten und als HTML-Seiten bereitstellen. Die Seite wird unter `https://vsvito420.github.io/py/` verfügbar sein.

## 2. Lokales Testen mit Jekyll (optional)

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

# Erstelle eine Gemfile-Datei
echo "source 'https://rubygems.org'" > Gemfile
echo "gem 'github-pages', group: :jekyll_plugins" >> Gemfile

# Installiere die Abhängigkeiten
bundle install
```

### Lokalen Server starten

```bash
# Starte den lokalen Jekyll-Server
bundle exec jekyll serve
```

Die Seite ist dann unter `http://localhost:4000` verfügbar.

## 3. Hinzufügen neuer Inhalte

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

## 4. Anpassen des Designs

Das Design kann über folgende Dateien angepasst werden:

- `docs/_layouts/default.html` - Das Hauptlayout
- `docs/assets/css/style.css` - CSS für das Styling
- `docs/assets/js/pyscript-helper.js` - JavaScript für die PyScript-Integration

## 5. Hinzufügen von Python-Paketen

Um zusätzliche Python-Pakete für PyScript verfügbar zu machen, bearbeite die `docs/_includes/pyscript.html`-Datei und füge die Pakete zur `packages`-Liste hinzu:

```html
<py-config>
    packages = ["numpy", "matplotlib", "pandas"]
</py-config>
```

## 6. Fehlerbehebung

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

## 7. Ressourcen

- [PyScript Dokumentation](https://pyscript.net/docs/)
- [Jekyll Dokumentation](https://jekyllrb.com/docs/)
- [GitHub Pages Dokumentation](https://docs.github.com/de/pages)
- [Markdown Guide](https://www.markdownguide.org/)