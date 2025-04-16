# Modul 6: Module und Pakete in Python

[&larr; Modul 5: Objektorientierung](../05_objektorientierung/README.md) | [Zurück zur Übersicht](../README.md) | [Modul 7: Dateien &rarr;](../07_dateien/README.md)

Dieses Modul behandelt die Verwendung und Erstellung von Modulen und Paketen in Python und vergleicht sie mit C++.

## Inhaltsübersicht

1. [Eigene Module](01_eigene_module.py)
   - Module erstellen
   - Module importieren
   - Namespaces und Scoping
   - Ausführung als Skript oder Modul
   - Relative und absolute Imports

2. [Standard-Bibliothek](02_standard_bibliothek.py)
   - Überblick über wichtige Module
   - Mathematische Module
   - Datei- und Pfadoperationen
   - Datum und Zeit
   - Zufallszahlen
   - Datenstrukturen
   - Weitere nützliche Module

## Unterschiede zu C++

Python und C++ haben unterschiedliche Ansätze zur Modularisierung von Code:

| Konzept | Python | C++ |
|---------|--------|-----|
| Modularisierung | Module und Pakete | Header-Dateien und Bibliotheken |
| Import | `import module` oder `from module import item` | `#include <header>` oder `#include "header"` |
| Namespaces | Implizit durch Module | Explizit mit `namespace` |
| Sichtbarkeit | Konventionen (z.B. `_private`) | Access specifiers (`private`, `public`) |
| Standardbibliothek | Umfangreiche Standardbibliothek | C++-Standardbibliothek und STL |
| Paketmanagement | pip, conda, etc. | CMake, vcpkg, Conan, etc. |

## Lernziele

Nach Abschluss dieses Moduls solltest du:

- Eigene Module und Pakete erstellen können
- Module korrekt importieren und verwenden können
- Die wichtigsten Module der Python-Standardbibliothek kennen
- Die Unterschiede zwischen Python und C++ in Bezug auf Modularisierung verstehen

## Übungen

Nach dem Durcharbeiten der Beispiele solltest du die Übungen im Ordner `übungen` lösen:
- [übung_06.py](../übungen/übung_06.py) - Module und Pakete

## Weiterführende Themen

- [Objektorientierung](../05_objektorientierung/README.md) - Organisation von Klassen in Modulen
- [Dateien](../07_dateien/01_lesen_schreiben.py) - Arbeiten mit externen Daten
- [Projekte](../09_projekte/README.md) - Strukturierung größerer Anwendungen

## Weiterführende Ressourcen

- [Python Module und Pakete](https://docs.python.org/3/tutorial/modules.html)
- [Python Standard Library](https://docs.python.org/3/library/index.html)
- [Python Package Index (PyPI)](https://pypi.org/)

---

[&larr; Modul 5: Objektorientierung](../05_objektorientierung/README.md) | [Zurück zur Übersicht](../README.md) | [Modul 7: Dateien &rarr;](../07_dateien/README.md)