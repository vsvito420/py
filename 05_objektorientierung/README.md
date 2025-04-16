# Objektorientierte Programmierung in Python

Dieses Modul behandelt die Grundlagen der objektorientierten Programmierung (OOP) in Python und vergleicht sie mit C++.

## Inhaltsübersicht

1. [Klassen und Objekte](01_klassen.py)
   - Klassendefinition
   - Konstruktoren und Destruktoren
   - Attribute und Methoden
   - Instanziierung von Objekten
   - Zugriffsmodifikatoren und Properties
   - Klassenmethoden und statische Methoden
   - Dunder-Methoden (Magic Methods)

2. [Vererbung und Polymorphismus](02_vererbung.py)
   - Einfache Vererbung
   - Mehrfachvererbung
   - Methodenüberschreibung
   - Abstrakte Klassen und Interfaces
   - Polymorphismus
   - Mixin-Klassen

## Unterschiede zu C++

Python und C++ haben unterschiedliche Ansätze zur objektorientierten Programmierung:

| Konzept | Python | C++ |
|---------|--------|-----|
| Zugriffsmodifikatoren | Konventionen (z.B. `_private`) | Schlüsselwörter (`private`, `protected`, `public`) |
| Konstruktoren | `__init__` Methode | Konstruktoren mit Klassenname |
| Destruktoren | `__del__` Methode (selten verwendet) | Destruktoren mit `~Klassenname` |
| Vererbung | Klassen in Klammern angeben | Klassen mit `:` angeben |
| Mehrfachvererbung | Direkt unterstützt | Direkt unterstützt, aber komplexer (diamond problem) |
| Methodenüberschreibung | Einfach durch Neudefinition | `virtual` und `override` Schlüsselwörter |
| Abstrakte Klassen | `abc`-Modul | `abstract` Schlüsselwort |
| Operatorüberladung | Dunder-Methoden (`__add__`, etc.) | Operatorfunktionen (`operator+`, etc.) |

## Lernziele

Nach Abschluss dieses Moduls solltest du:

- Klassen und Objekte in Python erstellen können
- Die Unterschiede zwischen Python und C++ in Bezug auf OOP verstehen
- Vererbung und Polymorphismus in Python anwenden können
- Die speziellen Methoden (Dunder-Methoden) in Python verstehen und nutzen können
- Abstrakte Klassen und Interfaces in Python implementieren können

## Weiterführende Ressourcen

- [Python Dokumentation zu Klassen](https://docs.python.org/3/tutorial/classes.html)
- [Python Dunder-Methoden](https://docs.python.org/3/reference/datamodel.html#special-method-names)
- [Abstract Base Classes (abc)](https://docs.python.org/3/library/abc.html)