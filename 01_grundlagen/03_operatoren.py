#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Operatoren in Python
Vergleich mit C++
"""

# ===== Arithmetische Operatoren =====
print("=== Arithmetische Operatoren ===")
a, b = 10, 3

# Addition (+)
print(f"{a} + {b} = {a + b}")

# Subtraktion (-)
print(f"{a} - {b} = {a - b}")

# Multiplikation (*)
print(f"{a} * {b} = {a * b}")

# Division (/)
# In C++: 10 / 3 = 3 (Integer-Division)
# In Python: 10 / 3 = 3.3333... (Float-Division)
print(f"{a} / {b} = {a / b}")

# Ganzzahldivision (//)
# In Python spezifischer Operator für Integer-Division
print(f"{a} // {b} = {a // b}")

# Modulo (%)
print(f"{a} % {b} = {a % b}")

# Potenz (**)
# In C++: pow(a, b) oder std::pow(a, b)
print(f"{a} ** {b} = {a ** b}")
print()

# ===== Zuweisungsoperatoren =====
print("=== Zuweisungsoperatoren ===")
x = 10
print(f"Anfangswert: x = {x}")

# Einfache Zuweisung (=)
x = 5
print(f"Nach x = 5: x = {x}")

# Additionszuweisung (+=)
x += 3  # Entspricht x = x + 3
print(f"Nach x += 3: x = {x}")

# Subtraktionszuweisung (-=)
x -= 2  # Entspricht x = x - 2
print(f"Nach x -= 2: x = {x}")

# Multiplikationszuweisung (*=)
x *= 4  # Entspricht x = x * 4
print(f"Nach x *= 4: x = {x}")

# Divisionszuweisung (/=)
x /= 2  # Entspricht x = x / 2
print(f"Nach x /= 2: x = {x}")

# Ganzzahldivisionszuweisung (//=)
x //= 2  # Entspricht x = x // 2
print(f"Nach x //= 2: x = {x}")

# Modulozuweisung (%=)
x %= 3  # Entspricht x = x % 3
print(f"Nach x %= 3: x = {x}")

# Potenzierungszuweisung (**=)
x **= 3  # Entspricht x = x ** 3
print(f"Nach x **= 3: x = {x}")
print()

# ===== Vergleichsoperatoren =====
print("=== Vergleichsoperatoren ===")
a, b = 5, 10

# Gleich (==)
print(f"{a} == {b}: {a == b}")
print(f"{a} == {a}: {a == a}")

# Ungleich (!=)
print(f"{a} != {b}: {a != b}")

# Größer als (>)
print(f"{a} > {b}: {a > b}")

# Kleiner als (<)
print(f"{a} < {b}: {a < b}")

# Größer oder gleich (>=)
print(f"{a} >= {b}: {a >= b}")
print(f"{a} >= {a}: {a >= a}")

# Kleiner oder gleich (<=)
print(f"{a} <= {b}: {a <= b}")
print(f"{a} <= {a}: {a <= a}")

# Identitätsvergleich (is)
# Prüft, ob zwei Variablen auf dasselbe Objekt verweisen
# In C++ vergleicht man Pointer: &a == &b
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(f"list1 == list2: {list1 == list2}")  # Vergleicht Werte
print(f"list1 is list2: {list1 is list2}")  # Vergleicht Identität (Speicheradresse)
print(f"list1 is list3: {list1 is list3}")  # list3 verweist auf dasselbe Objekt wie list1
print()

# ===== Logische Operatoren =====
print("=== Logische Operatoren ===")
a, b = True, False

# Logisches UND (and)
# In C++: &&
print(f"{a} and {a}: {a and a}")
print(f"{a} and {b}: {a and b}")
print(f"{b} and {b}: {b and b}")

# Logisches ODER (or)
# In C++: ||
print(f"{a} or {a}: {a or a}")
print(f"{a} or {b}: {a or b}")
print(f"{b} or {b}: {b or b}")

# Logisches NICHT (not)
# In C++: !
print(f"not {a}: {not a}")
print(f"not {b}: {not b}")

# Kurzschlussauswertung (Short-circuit evaluation)
# Wie in C++ werden logische Ausdrücke von links nach rechts ausgewertet
# und die Auswertung wird abgebrochen, sobald das Ergebnis feststeht
x = 5
print(f"x > 10 and x < 20: {x > 10 and x < 20}")  # x < 20 wird nicht ausgewertet
print(f"x > 0 or x > 10: {x > 0 or x > 10}")      # x > 10 wird nicht ausgewertet
print()

# ===== Bitweise Operatoren =====
print("=== Bitweise Operatoren ===")
a, b = 60, 13  # In Binär: a = 0011 1100, b = 0000 1101

# Bitweises UND (&)
print(f"{a} & {b} = {a & b}")  # 0000 1100 = 12

# Bitweises ODER (|)
print(f"{a} | {b} = {a | b}")  # 0011 1101 = 61

# Bitweises XOR (^)
print(f"{a} ^ {b} = {a ^ b}")  # 0011 0001 = 49

# Bitweise Negation (~)
print(f"~{a} = {~a}")  # 1100 0011 = -61 (Zweierkomplement)

# Bitweise Linksverschiebung (<<)
print(f"{a} << 2 = {a << 2}")  # 1111 0000 = 240

# Bitweise Rechtsverschiebung (>>)
print(f"{a} >> 2 = {a >> 2}")  # 0000 1111 = 15
print()

# ===== Mitgliedschaftsoperatoren =====
print("=== Mitgliedschaftsoperatoren ===")
# In C++ nicht direkt vorhanden, man verwendet std::find oder ähnliches

# in - prüft, ob ein Wert in einer Sequenz enthalten ist
liste = [1, 2, 3, 4, 5]
print(f"3 in {liste}: {3 in liste}")
print(f"6 in {liste}: {6 in liste}")

text = "Python"
print(f"'th' in '{text}': {'th' in text}")
print(f"'x' in '{text}': {'x' in text}")

dict1 = {"name": "Max", "alter": 30}
print(f"'name' in {dict1}: {'name' in dict1}")  # Prüft Schlüssel, nicht Werte
print(f"'Max' in {dict1}: {'Max' in dict1}")
print(f"'Max' in {dict1.values()}: {'Max' in dict1.values()}")
print()

# ===== Operator-Präzedenz =====
print("=== Operator-Präzedenz ===")
# Ähnlich wie in C++, aber mit einigen Unterschieden

# Beispiel für Präzedenz
result = 2 + 3 * 4
print(f"2 + 3 * 4 = {result}")  # Multiplikation hat Vorrang vor Addition

# Mit Klammern
result = (2 + 3) * 4
print(f"(2 + 3) * 4 = {result}")  # Klammern haben höchste Präzedenz

# Komplexeres Beispiel
result = 2 ** 3 * 4 + 5 // 2 - 1
print(f"2 ** 3 * 4 + 5 // 2 - 1 = {result}")  # 2^3 * 4 + 5//2 - 1 = 8 * 4 + 2 - 1 = 33
print()

# ===== ÜBUNG =====
print("=== ÜBUNG ===")
print("1. Berechne den Rest der Division von 17 durch 5")
print("2. Prüfe, ob 'Python' in der Liste ['Java', 'C++', 'Python', 'JavaScript'] enthalten ist")
print("3. Berechne 2^4 * 3 - 5")

# TODO: Schreibe deinen Code hier
# aufgabe1 = ...

# Beispiellösung (auskommentiert)
"""
# 1. Rest der Division
aufgabe1 = 17 % 5
print(f"17 % 5 = {aufgabe1}")

# 2. Mitgliedschaft prüfen
programmiersprachen = ['Java', 'C++', 'Python', 'JavaScript']
aufgabe2 = 'Python' in programmiersprachen
print(f"'Python' in {programmiersprachen}: {aufgabe2}")

# 3. Berechnung mit Präzedenz
aufgabe3 = 2 ** 4 * 3 - 5
print(f"2 ** 4 * 3 - 5 = {aufgabe3}")
"""