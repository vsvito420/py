#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Eigene Module in Python
Vergleich mit C++
"""

# ===== Module erstellen und importieren =====
print("=== Module erstellen und importieren ===")

# In C++:
# // math_utils.h
# #ifndef MATH_UTILS_H
# #define MATH_UTILS_H
# 
# namespace math_utils {
#     double add(double a, double b);
#     double subtract(double a, double b);
# }
# 
# #endif
# 
# // math_utils.cpp
# #include "math_utils.h"
# 
# namespace math_utils {
#     double add(double a, double b) {
#         return a + b;
#     }
#     
#     double subtract(double a, double b) {
#         return a - b;
#     }
# }
# 
# // main.cpp
# #include <iostream>
# #include "math_utils.h"
# 
# int main() {
#     double result = math_utils::add(5.0, 3.0);
#     std::cout << "5 + 3 = " << result << std::endl;
#     return 0;
# }

# In Python:
# Wir erstellen ein Beispielmodul direkt hier

print("Dieses Skript demonstriert, wie man Module in Python erstellt und verwendet.")
print("Normalerweise würde man Module in separaten Dateien definieren.")
print()

# Angenommen, wir haben ein Modul 'math_utils.py' mit folgendem Inhalt:
"""
# math_utils.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

PI = 3.14159

class Calculator:
    def __init__(self, name):
        self.name = name
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division durch Null")
        return a / b

# Private Funktion (Konvention mit _)
def _internal_function():
    return "Diese Funktion ist für interne Zwecke gedacht."

if __name__ == "__main__":
    # Dieser Code wird nur ausgeführt, wenn die Datei direkt ausgeführt wird
    print("math_utils.py wird als Skript ausgeführt")
    print(f"5 + 3 = {add(5, 3)}")
else:
    # Dieser Code wird ausgeführt, wenn das Modul importiert wird
    print("math_utils Modul wurde importiert")
"""

# Wir simulieren das Importieren dieses Moduls:
print("Simulation des Imports von math_utils:")
print("math_utils Modul wurde importiert")
print()

# ===== Verschiedene Import-Methoden =====
print("=== Verschiedene Import-Methoden ===")

# 1. Gesamtes Modul importieren
# import math_utils
print("# import math_utils")
print("# math_utils.add(5, 3)  # Ergebnis: 8")
print("# math_utils.PI  # Ergebnis: 3.14159")
print()

# 2. Spezifische Elemente importieren
# from math_utils import add, subtract, PI
print("# from math_utils import add, subtract, PI")
print("# add(5, 3)  # Ergebnis: 8")
print("# PI  # Ergebnis: 3.14159")
print()

# 3. Alles importieren (nicht empfohlen)
# from math_utils import *
print("# from math_utils import *")
print("# add(5, 3)  # Ergebnis: 8")
print("# PI  # Ergebnis: 3.14159")
print("# Nicht empfohlen, da es den Namespace verschmutzt und unklar ist, woher die Funktionen kommen")
print()

# 4. Mit Alias importieren
# import math_utils as mu
print("# import math_utils as mu")
print("# mu.add(5, 3)  # Ergebnis: 8")
print()

# 5. Elemente mit Alias importieren
# from math_utils import add as addition, subtract as subtraction
print("# from math_utils import add as addition, subtract as subtraction")
print("# addition(5, 3)  # Ergebnis: 8")
print()

# ===== Module und Namespaces =====
print("=== Module und Namespaces ===")

# In C++:
# namespace math {
#     double PI = 3.14159;
# }
# 
# namespace physics {
#     double PI = 3.14159265359;
# }
# 
# // Verwendung
# double area = math::PI * radius * radius;
# double wavelength = 2 * physics::PI * frequency;

# In Python:
# Angenommen, wir haben zwei Module mit gleichen Namen für Variablen/Funktionen

print("# import math")
print("# import physics")
print("# ")
print("# # Verwendung")
print("# area = math.pi * radius * radius")
print("# wavelength = 2 * physics.PI * frequency")
print()

# ===== Module als Skript oder als Modul ausführen =====
print("=== Module als Skript oder als Modul ausführen ===")

# Die if __name__ == "__main__": Konstruktion

print("Beispiel für if __name__ == \"__main__\":")
print("""
def main():
    print("Hauptfunktion wird ausgeführt")
    # Hier kommt der Hauptcode hin

if __name__ == "__main__":
    # Dieser Code wird nur ausgeführt, wenn die Datei direkt ausgeführt wird
    print("Dieses Skript wird direkt ausgeführt")
    main()
else:
    # Dieser Code wird ausgeführt, wenn das Modul importiert wird
    print("Dieses Modul wurde importiert")
""")

# Demonstration
print(f"In dieser Datei ist __name__ = {__name__}")
print()

# ===== Pakete erstellen =====
print("=== Pakete erstellen ===")

# In C++ gibt es kein direktes Äquivalent zu Python-Paketen
# Am nächsten kommen Namespaces und Verzeichnisstrukturen

# In Python:
# Ein Paket ist ein Verzeichnis mit Python-Dateien und einer __init__.py Datei

print("Struktur eines Python-Pakets:")
print("""
mein_paket/
    __init__.py          # Macht das Verzeichnis zu einem Paket
    modul1.py
    modul2.py
    unterpaket/
        __init__.py      # Macht das Unterverzeichnis zu einem Unterpaket
        modul3.py
        modul4.py
""")

print("Inhalt von __init__.py (kann leer sein oder Initialisierungscode enthalten):")
print("""
# __init__.py
print("mein_paket wurde initialisiert")

# Öffentliche API definieren
from .modul1 import funktion1, Klasse1
from .modul2 import funktion2

# Version definieren
__version__ = "1.0.0"
""")

print("Import aus einem Paket:")
print("""
# Gesamtes Paket importieren
import mein_paket

# Spezifisches Modul importieren
import mein_paket.modul1

# Spezifische Funktion aus einem Modul importieren
from mein_paket.modul1 import funktion1

# Aus einem Unterpaket importieren
from mein_paket.unterpaket import modul3
""")
print()

# ===== Relative und absolute Imports =====
print("=== Relative und absolute Imports ===")

print("Absolute Imports (empfohlen):")
print("""
# Von überall im Code
import mein_paket.modul1
from mein_paket.unterpaket import modul3
""")

print("Relative Imports (innerhalb eines Pakets):")
print("""
# In mein_paket/modul2.py
from . import modul1                # Importiert modul1 aus dem gleichen Paket
from .modul1 import funktion1       # Importiert funktion1 aus modul1
from .. import anderes_paket        # Importiert anderes_paket aus dem übergeordneten Paket
from ..anderes_paket import modul5  # Importiert modul5 aus anderes_paket
""")
print()

# ===== Suchpfad für Module =====
print("=== Suchpfad für Module ===")

import sys

print("Python sucht Module in folgender Reihenfolge:")
print("1. Das aktuelle Verzeichnis")
print("2. PYTHONPATH (Umgebungsvariable)")
print("3. Standardverzeichnisse für Bibliotheken")
print()

print("Aktueller Suchpfad (sys.path):")
for path in sys.path:
    print(f"- {path}")
print()

print("Hinzufügen eines Verzeichnisses zum Suchpfad:")
print("""
import sys
sys.path.append('/pfad/zu/meinen/modulen')
""")
print()

# ===== Nützliche Modulinformationen =====
print("=== Nützliche Modulinformationen ===")

import math

print("Informationen über ein Modul:")
print(f"Name: {math.__name__}")
print(f"Datei: {math.__file__}")
print(f"Docstring: {math.__doc__}")

print("\nAlle öffentlichen Namen im Modul:")
print([name for name in dir(math) if not name.startswith('_')])
print()

# ===== ÜBUNG =====
print("=== ÜBUNG ===")
print("1. Erstelle ein Modul 'string_utils.py' mit Funktionen zur Textverarbeitung")
print("2. Erstelle ein Paket 'geometry' mit Modulen für verschiedene geometrische Formen")
print("3. Importiere und verwende deine Module in einem Hauptskript")

# TODO: Schreibe deinen Code hier
# Beispiel für string_utils.py:
# def reverse(text):
#     return text[::-1]
# ...

# Beispiellösung (auskommentiert)
"""
# string_utils.py
def reverse(text):
    # Kehrt einen Text um.
    return text[::-1]

def count_vowels(text):
    # Zählt die Vokale in einem Text.
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

def is_palindrome(text):
    # Prüft, ob ein Text ein Palindrom ist.
    # Leerzeichen und Groß-/Kleinschreibung ignorieren
    text = text.lower().replace(" ", "")
    return text == text[::-1]

if __name__ == "__main__":
    # Test
    test_text = "Python ist cool"
    print(f"Original: {test_text}")
    print(f"Umgekehrt: {reverse(test_text)}")
    print(f"Anzahl Vokale: {count_vowels(test_text)}")
    print(f"Ist Palindrom: {is_palindrome(test_text)}")
    
    palindrom = "Anna"
    print(f"{palindrom} ist Palindrom: {is_palindrome(palindrom)}")
"""

"""
# Paketstruktur für geometry
# geometry/
#     __init__.py
#     circle.py
#     rectangle.py
#     triangle.py

# geometry/__init__.py
from .circle import Circle
from .rectangle import Rectangle
from .triangle import Triangle

__all__ = ['Circle', 'Rectangle', 'Triangle']

# geometry/circle.py
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def circumference(self):
        return 2 * math.pi * self.radius
    
    def __str__(self):
        return f"Circle(radius={self.radius})"

# geometry/rectangle.py
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

# geometry/triangle.py
import math

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def area(self):
        # Heron's formula
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    def perimeter(self):
        return self.a + self.b + self.c
    
    def __str__(self):
        return f"Triangle(a={self.a}, b={self.b}, c={self.c})"
"""

"""
# main.py - Hauptskript, das die Module verwendet
import string_utils
from geometry import Circle, Rectangle, Triangle

# String-Utilities verwenden
text = "Python ist eine tolle Programmiersprache"
print(f"Original: {text}")
print(f"Umgekehrt: {string_utils.reverse(text)}")
print(f"Anzahl Vokale: {string_utils.count_vowels(text)}")
print(f"Ist Palindrom: {string_utils.is_palindrome(text)}")

# Geometrische Formen verwenden
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 4, 5)

print(f"\n{circle}")
print(f"Fläche: {circle.area():.2f}")
print(f"Umfang: {circle.circumference():.2f}")

print(f"\n{rectangle}")
print(f"Fläche: {rectangle.area()}")
print(f"Umfang: {rectangle.perimeter()}")

print(f"\n{triangle}")
print(f"Fläche: {triangle.area()}")
print(f"Umfang: {triangle.perimeter()}")
"""