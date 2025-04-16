# Modul 2: Kontrollstrukturen

[&larr; Modul 1: Grundlagen](../01_grundlagen/README.md) | [Zurück zur Übersicht](../README.md) | [Modul 3: Funktionen &rarr;](../03_funktionen/README.md)

In diesem Modul lernst du die Kontrollstrukturen in Python kennen und wie sie sich von C++ unterscheiden.

## Lernziele

- Bedingte Anweisungen (if, elif, else) verstehen und anwenden
- Verschiedene Schleifentypen (for, while) beherrschen
- List Comprehensions als mächtige Python-Funktion nutzen
- Unterschiede zu C++ erkennen und verstehen

## Dateien in diesem Modul

1. [01_if_else.py](01_if_else.py) - Bedingte Anweisungen
2. [02_schleifen.py](02_schleifen.py) - For- und While-Schleifen
3. [03_listen_comprehension.py](03_listen_comprehension.py) - List Comprehensions und Generator Expressions

## Wichtige Unterschiede zu C++

| C++ | Python | Beispiel Python |
|-----|--------|----------------|
| `if (x > 0) { ... }` | `if x > 0:` | `if x > 0:` |
| `else if (x < 0) { ... }` | `elif x < 0:` | `elif x < 0:` |
| `for (int i = 0; i < 10; i++) { ... }` | `for i in range(10):` | `for i in range(10):` |
| `for (auto& item : container) { ... }` | `for item in container:` | `for item in liste:` |
| `while (condition) { ... }` | `while condition:` | `while x > 0:` |
| `do { ... } while (condition);` | Nicht direkt vorhanden | `while True:` <br> `    ...` <br> `    if not condition: break` |
| Keine direkte Entsprechung | List Comprehensions | `[x**2 for x in range(10)]` |

## Übungen

Nach dem Durcharbeiten der Beispiele solltest du die Übungen im Ordner `übungen` lösen:
- [übung_02.py](../übungen/übung_02.py) - Kontrollstrukturen und Schleifen

## Weiterführende Themen

- [Funktionen](../03_funktionen/README.md) - Funktionsdefinitionen und -aufrufe
- [List Comprehensions in Datenstrukturen](../04_datenstrukturen/01_listen.py) - Erweiterte Anwendung von List Comprehensions
- [Schleifen mit Dateien](../07_dateien/01_lesen_schreiben.py) - Dateien zeilenweise durchlaufen

---

[&larr; Modul 1: Grundlagen](../01_grundlagen/README.md) | [Zurück zur Übersicht](../README.md) | [Modul 3: Funktionen &rarr;](../03_funktionen/README.md)