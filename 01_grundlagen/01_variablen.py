#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Variablen und Datentypen in Python
Vergleich mit C++
"""

# ===== Variablen in Python =====
# Im Gegensatz zu C++ brauchen wir keine Typdeklaration

# In C++: int zahl = 42;
zahl = 42  # Integer
name = "Python"  # String
ist_wahr = True  # Boolean

print("=== Variablen und ihre Typen ===")
print(f"zahl: {zahl} (Typ: {type(zahl)})")
print(f"name: {name} (Typ: {type(name)})")
print(f"ist_wahr: {ist_wahr} (Typ: {type(ist_wahr)})")
print()

# ===== Dynamische Typisierung =====
# Variablen können ihren Typ ändern - in C++ nicht möglich!
print("=== Dynamische Typisierung ===")
zahl = "Jetzt bin ich ein String"
print(f"zahl ist jetzt: {zahl} (Typ: {type(zahl)})")
print()

# ===== Mehrfachzuweisung =====
# In C++: int a = 1, b = 2, c = 3;
# In Python können wir das kürzer schreiben:
print("=== Mehrfachzuweisung ===")
a, b, c = 1, 2, 3
print(f"a = {a}, b = {b}, c = {c}")

# Werte tauschen (in C++ bräuchte man eine temporäre Variable)
a, b = b, a
print(f"Nach dem Tausch: a = {a}, b = {b}")
print()

# ===== Konstanten =====
# Python hat keine echten Konstanten wie const in C++
# Konvention: Großbuchstaben für "Konstanten"
PI = 3.14159
GRAVITATIONSKONSTANTE = 9.81
print("=== Konstanten (per Konvention) ===")
print(f"PI = {PI}")
print(f"GRAVITATIONSKONSTANTE = {GRAVITATIONSKONSTANTE}")
print()

# ===== Typumwandlung =====
# In C++: int x = (int)3.14;
# In Python:
print("=== Typumwandlung ===")
x = int(3.14)  # Umwandlung in Integer (wird abgeschnitten)
y = float(42)  # Umwandlung in Float
z = str(2.718)  # Umwandlung in String
print(f"x = int(3.14) = {x}")
print(f"y = float(42) = {y}")
print(f"z = str(2.718) = {z} (Typ: {type(z)})")
print()

# ===== None-Typ =====
# Ähnlich wie NULL in C++, aber sicherer
print("=== None-Typ ===")
nichts = None
print(f"nichts = {nichts}")
print(f"Ist nichts None? {nichts is None}")
print()

# ===== Variablennamen =====
# Ähnliche Regeln wie in C++, aber mit Unterstrichen statt camelCase
user_name = "Max"  # In Python bevorzugt: snake_case
userName = "Max"   # In C++ bevorzugt: camelCase
# Beide funktionieren in Python, aber snake_case ist die Konvention

# ===== ÜBUNG =====
print("=== ÜBUNG ===")
print("1. Erstelle eigene Variablen verschiedener Typen")
print("2. Führe Typumwandlungen durch")
print("3. Experimentiere mit Mehrfachzuweisungen")

# TODO: Schreibe deinen Code hier
# meine_variable = ...

# Beispiellösung (auskommentiert)
"""
meine_zahl = 100
mein_text = "Hallo Python"
mein_float = 3.14159
meine_liste = [1, 2, 3, 4, 5]

# Typumwandlungen
zahl_als_text = str(meine_zahl)
text_als_liste = list(mein_text)

# Mehrfachzuweisung
x, y, z = meine_liste[0:3]
print(f"x = {x}, y = {y}, z = {z}")
"""