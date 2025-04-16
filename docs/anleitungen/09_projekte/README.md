# Modul 9: Projekte in Python

[&larr; Modul 8: Ausnahmebehandlung](../08_ausnahmebehandlung/README.md) | [Zurück zur Übersicht](../README.md)

Dieses Modul enthält praktische Projekte, die das Gelernte aus den vorherigen Modulen anwenden und vertiefen.

## Projektübersicht

In diesem Verzeichnis können verschiedene Projekte erstellt werden, die unterschiedliche Aspekte der Python-Programmierung abdecken. Hier sind einige Projektideen:

1. **Textanalyse-Tool**
   - Einlesen und Analysieren von Textdateien
   - Wort- und Zeichenhäufigkeiten berechnen
   - Statistiken erstellen und visualisieren

2. **Einfaches Dateiverwaltungssystem**
   - Dateien organisieren und kategorisieren
   - Suchen nach Dateien mit bestimmten Eigenschaften
   - Backup-Funktionalität implementieren

3. **Datenbank-Anwendung**
   - Verbindung zu einer SQLite-Datenbank
   - CRUD-Operationen (Create, Read, Update, Delete)
   - Datenabfragen und -manipulation

4. **Webseiten-Scraper**
   - Daten von Webseiten extrahieren
   - Informationen strukturieren und speichern
   - Regelmäßige Aktualisierungen durchführen

5. **GUI-Anwendung**
   - Benutzeroberfläche mit Tkinter oder PyQt
   - Interaktive Elemente wie Buttons, Eingabefelder, etc.
   - Ereignisbehandlung

6. **API-Client**
   - Verbindung zu einer öffentlichen API
   - Daten abrufen und verarbeiten
   - Ergebnisse darstellen

## Projektstruktur

Jedes Projekt sollte in einem eigenen Unterverzeichnis organisiert sein und folgende Struktur aufweisen:

```
projekt_name/
├── README.md           # Projektbeschreibung und Anleitung
├── requirements.txt    # Abhängigkeiten
├── main.py             # Hauptprogramm
├── src/                # Quellcode
│   ├── __init__.py
│   ├── module1.py
│   └── module2.py
├── tests/              # Tests
│   ├── __init__.py
│   ├── test_module1.py
│   └── test_module2.py
└── data/               # Daten (falls erforderlich)
```

## Vergleich mit C++

| Aspekt | Python | C++ |
|--------|--------|-----|
| Projektorganisation | Pakete und Module | Header und Quelldateien |
| Build-System | setuptools, pip | CMake, Make, etc. |
| Abhängigkeiten | requirements.txt, Pipfile | CMakeLists.txt, vcpkg, Conan |
| Tests | unittest, pytest | Catch2, Google Test, Boost.Test |
| Dokumentation | Docstrings, Sphinx | Doxygen, Sphinx |
| Paketierung | PyPI, Wheels | Binaries, Shared Libraries |

## Lernziele

Durch die Arbeit an diesen Projekten solltest du:

- Die in den vorherigen Modulen erlernten Konzepte praktisch anwenden können
- Erfahrung in der Strukturierung größerer Python-Projekte sammeln
- Den gesamten Entwicklungsprozess von der Planung bis zur Implementierung durchlaufen
- Problemlösungsfähigkeiten und Debugging-Techniken verbessern
- Teamarbeit und Versionskontrolle mit Git üben

## Weiterführende Ressourcen

- [Python Packaging User Guide](https://packaging.python.org/)
- [Python Testing with pytest](https://docs.pytest.org/en/latest/)
- [Python Project Structure](https://docs.python-guide.org/writing/structure/)
- [GitHub Student Developer Pack](https://education.github.com/pack) (für kostenlose Entwicklertools)

## Übungen

Nach dem Durcharbeiten der Beispiele solltest du die Übungen im Ordner `übungen` lösen:
- [übung_08.py](../übungen/übung_08.py) - Praxisprojekt

## Weiterführende Themen

- Alle vorherigen Module werden in Projekten angewendet und vertieft
- [Externe Bibliotheken und Frameworks](https://pypi.org/) - Erweiterung der eigenen Projekte

---

[&larr; Modul 8: Ausnahmebehandlung](../08_ausnahmebehandlung/README.md) | [Zurück zur Übersicht](../README.md)