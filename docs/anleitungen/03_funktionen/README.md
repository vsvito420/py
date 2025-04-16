# Modul 3: Funktionen

[&larr; Modul 2: Kontrollstrukturen](../02_kontrollstrukturen/README.md) | [Zurück zur Übersicht](../README.md) | [Modul 4: Datenstrukturen &rarr;](../04_datenstrukturen/README.md)

In diesem Modul lernst du, wie Funktionen in Python definiert und verwendet werden und wie sie sich von C++ unterscheiden.

## Lernziele

- Funktionen definieren und aufrufen
- Parameter und Rückgabewerte verstehen
- Verschiedene Arten von Parametern (Positions-, Schlüsselwort-, Default-Parameter) kennenlernen
- Rekursion in Python anwenden
- Lambda-Funktionen verstehen und nutzen
- Unterschiede zu C++ erkennen

## Dateien in diesem Modul

1. [01_funktionen_grundlagen.py](01_funktionen_grundlagen.py) - Grundlagen der Funktionsdefinition und -verwendung
2. [02_parameter.py](02_parameter.py) - Verschiedene Arten von Parametern und Argumenten
3. [03_rekursion.py](03_rekursion.py) - Rekursive Funktionen und ihre Anwendungen

## Wichtige Unterschiede zu C++

| C++ | Python | Beispiel Python |
|-----|--------|----------------|
| `int add(int a, int b) { return a + b; }` | `def add(a, b): return a + b` | `def add(a, b): return a + b` |
| Typisierte Parameter | Dynamisch typisierte Parameter | `def func(x): ...` |
| Überladung von Funktionen | Keine direkte Überladung | `def func(*args, **kwargs): ...` |
| Default-Parameter nur am Ende | Default-Parameter überall möglich | `def func(a=1, b=2): ...` |
| Keine Schlüsselwortargumente | Schlüsselwortargumente | `func(name="Max", alter=30)` |
| Lambda: `auto f = [](int x) { return x*x; };` | Lambda: `lambda x: x*x` | `square = lambda x: x*x` |

## Übungen

Nach dem Durcharbeiten der Beispiele solltest du die Übungen im Ordner `übungen` lösen:
- [übung_03.py](../übungen/übung_03.py) - Funktionen und Parameter

## Weiterführende Themen

- [Objektorientierung](../05_objektorientierung/01_klassen.py) - Methoden in Klassen
- [Eigene Module](../06_module_und_pakete/01_eigene_module.py) - Funktionen in Modulen organisieren
- [Funktionen höherer Ordnung](../06_module_und_pakete/02_standard_bibliothek.py) - Funktionen wie map, filter und reduce

---

[&larr; Modul 2: Kontrollstrukturen](../02_kontrollstrukturen/README.md) | [Zurück zur Übersicht](../README.md) | [Modul 4: Datenstrukturen &rarr;](../04_datenstrukturen/README.md)