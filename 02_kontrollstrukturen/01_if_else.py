#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Bedingte Anweisungen in Python (if, elif, else)
Vergleich mit C++
"""

# ===== Einfache if-Anweisung =====
print("=== Einfache if-Anweisung ===")

# In C++:
# if (x > 0) {
#     std::cout << "x ist positiv" << std::endl;
# }

x = 10

# In Python:
if x > 0:
    print("x ist positiv")

# Beachte: Keine Klammern um die Bedingung nötig
# Beachte: Einrückung statt geschweifter Klammern
print()

# ===== if-else-Anweisung =====
print("=== if-else-Anweisung ===")

# In C++:
# if (x % 2 == 0) {
#     std::cout << "x ist gerade" << std::endl;
# } else {
#     std::cout << "x ist ungerade" << std::endl;
# }

# In Python:
if x % 2 == 0:
    print("x ist gerade")
else:
    print("x ist ungerade")
print()

# ===== if-elif-else-Anweisung =====
print("=== if-elif-else-Anweisung ===")

# In C++:
# if (x > 0) {
#     std::cout << "x ist positiv" << std::endl;
# } else if (x < 0) {
#     std::cout << "x ist negativ" << std::endl;
# } else {
#     std::cout << "x ist null" << std::endl;
# }

# In Python:
if x > 0:
    print("x ist positiv")
elif x < 0:
    print("x ist negativ")
else:
    print("x ist null")

# Beachte: 'elif' statt 'else if' in C++
print()

# ===== Mehrere elif-Blöcke =====
print("=== Mehrere elif-Blöcke ===")

note = 85

if note >= 90:
    print("Sehr gut")
elif note >= 80:
    print("Gut")
elif note >= 70:
    print("Befriedigend")
elif note >= 60:
    print("Ausreichend")
else:
    print("Nicht bestanden")
print()

# ===== Verschachtelte if-Anweisungen =====
print("=== Verschachtelte if-Anweisungen ===")

alter = 25
hat_führerschein = True

if alter >= 18:
    print("Volljährig")
    if hat_führerschein:
        print("Darf Auto fahren")
    else:
        print("Darf kein Auto fahren (kein Führerschein)")
else:
    print("Minderjährig")
    print("Darf kein Auto fahren (zu jung)")
print()

# ===== Logische Operatoren in Bedingungen =====
print("=== Logische Operatoren in Bedingungen ===")

# In C++: && (und), || (oder), ! (nicht)
# In Python: and, or, not

a, b = 5, 10

# Logisches UND
if a > 0 and b > 0:
    print("Beide Zahlen sind positiv")

# Logisches ODER
if a > 0 or b > 0:
    print("Mindestens eine Zahl ist positiv")

# Logisches NICHT
if not (a > b):
    print("a ist nicht größer als b")
print()

# ===== Kurzform für einfache Bedingungen =====
print("=== Kurzform für einfache Bedingungen ===")

# Bedingte Zuweisung (Ternärer Operator)
# In C++: int max_val = (a > b) ? a : b;
# In Python:
max_val = a if a > b else b
print(f"Maximum von {a} und {b} ist {max_val}")
print()

# ===== Wahrheitswerte in Python =====
print("=== Wahrheitswerte in Python ===")

# In Python gelten folgende Werte als False:
# - False
# - None
# - 0 (Null)
# - Leere Sequenzen: "", [], (), {}
# - Alles andere gilt als True

# Beispiele:
werte = [True, False, 0, 1, "", "Hallo", [], [1, 2], None]

for wert in werte:
    if wert:
        print(f"{wert} wird als True ausgewertet")
    else:
        print(f"{wert} wird als False ausgewertet")
print()

# ===== Identitäts- und Mitgliedschaftsprüfungen =====
print("=== Identitäts- und Mitgliedschaftsprüfungen ===")

# is-Operator (Identität)
a = [1, 2, 3]
b = a  # b verweist auf dasselbe Objekt wie a
c = [1, 2, 3]  # c ist ein neues Objekt mit gleichem Inhalt

if a is b:
    print("a und b sind dasselbe Objekt")
if a is not c:
    print("a und c sind verschiedene Objekte")
if a == c:
    print("a und c haben den gleichen Inhalt")

# in-Operator (Mitgliedschaft)
liste = [1, 2, 3, 4, 5]
if 3 in liste:
    print("3 ist in der Liste enthalten")
if 6 not in liste:
    print("6 ist nicht in der Liste enthalten")
print()

# ===== Vergleichsketten =====
print("=== Vergleichsketten ===")

# In C++: if (x > 0 && x < 10) { ... }
# In Python:
x = 5
if 0 < x < 10:
    print("x liegt zwischen 0 und 10")

# Mehrfachvergleiche
if 0 <= x <= 10 <= 20:
    print("x liegt zwischen 0 und 10, und 10 ist kleiner oder gleich 20")
print()

# ===== ÜBUNG =====
print("=== ÜBUNG ===")
print("1. Schreibe eine Funktion, die prüft, ob eine Zahl gerade oder ungerade ist")
print("2. Schreibe eine Funktion, die eine Note (0-100) in einen Buchstaben (A, B, C, D, F) umwandelt")
print("3. Schreibe eine Funktion, die prüft, ob ein Jahr ein Schaltjahr ist")

# TODO: Schreibe deinen Code hier
# def ist_gerade(zahl):
#     ...

# Beispiellösung (auskommentiert)
"""
# 1. Gerade oder ungerade
def ist_gerade(zahl):
    if zahl % 2 == 0:
        return True
    else:
        return False
    # Oder kürzer: return zahl % 2 == 0

print(f"Ist 4 gerade? {ist_gerade(4)}")
print(f"Ist 7 gerade? {ist_gerade(7)}")

# 2. Notenumwandlung
def note_zu_buchstabe(note):
    if note >= 90:
        return "A"
    elif note >= 80:
        return "B"
    elif note >= 70:
        return "C"
    elif note >= 60:
        return "D"
    else:
        return "F"

print(f"Note 95: {note_zu_buchstabe(95)}")
print(f"Note 82: {note_zu_buchstabe(82)}")
print(f"Note 45: {note_zu_buchstabe(45)}")

# 3. Schaltjahr
def ist_schaltjahr(jahr):
    # Ein Jahr ist ein Schaltjahr, wenn es durch 4 teilbar ist,
    # es sei denn, es ist durch 100 teilbar, aber nicht durch 400
    if jahr % 400 == 0:
        return True
    elif jahr % 100 == 0:
        return False
    elif jahr % 4 == 0:
        return True
    else:
        return False

print(f"Ist 2020 ein Schaltjahr? {ist_schaltjahr(2020)}")
print(f"Ist 2100 ein Schaltjahr? {ist_schaltjahr(2100)}")
print(f"Ist 2000 ein Schaltjahr? {ist_schaltjahr(2000)}")
"""