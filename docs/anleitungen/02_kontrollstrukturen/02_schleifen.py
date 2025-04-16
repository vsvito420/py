#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Schleifen in Python (for, while)
Vergleich mit C++
"""

# ===== For-Schleife mit range() =====
print("=== For-Schleife mit range() ===")

# In C++:
# for (int i = 0; i < 5; i++) {
#     std::cout << i << " ";
# }

# In Python:
print("Zählen von 0 bis 4:")
for i in range(5):  # range(5) erzeugt Sequenz: 0, 1, 2, 3, 4
    print(i, end=" ")
print("\n")

# range() mit Start- und Endwert
print("Zählen von 1 bis 5:")
for i in range(1, 6):  # range(1, 6) erzeugt Sequenz: 1, 2, 3, 4, 5
    print(i, end=" ")
print("\n")

# range() mit Schrittweite
print("Zählen von 0 bis 10 in 2er-Schritten:")
for i in range(0, 11, 2):  # range(0, 11, 2) erzeugt Sequenz: 0, 2, 4, 6, 8, 10
    print(i, end=" ")
print("\n")

# Rückwärts zählen
print("Rückwärts zählen von 5 bis 1:")
for i in range(5, 0, -1):  # range(5, 0, -1) erzeugt Sequenz: 5, 4, 3, 2, 1
    print(i, end=" ")
print("\n")

# ===== For-Schleife über Sequenzen =====
print("=== For-Schleife über Sequenzen ===")

# In C++:
# std::vector<std::string> fruits = {"Apfel", "Banane", "Kirsche"};
# for (const auto& fruit : fruits) {
#     std::cout << fruit << " ";
# }

# In Python:
früchte = ["Apfel", "Banane", "Kirsche"]
print("Iteration über eine Liste:")
for frucht in früchte:
    print(frucht, end=" ")
print("\n")

# Iteration über einen String
text = "Python"
print("Iteration über einen String:")
for buchstabe in text:
    print(buchstabe, end=" ")
print("\n")

# Iteration über ein Dictionary
personen = {"Max": 30, "Anna": 25, "Tim": 35}
print("Iteration über Dictionary-Schlüssel:")
for name in personen:
    print(f"{name}: {personen[name]}", end=" | ")
print("\n")

print("Iteration über Dictionary-Items:")
for name, alter in personen.items():
    print(f"{name}: {alter}", end=" | ")
print("\n")

# ===== Enumerate für Index und Wert =====
print("=== Enumerate für Index und Wert ===")

# In C++:
# for (size_t i = 0; i < fruits.size(); i++) {
#     std::cout << i << ": " << fruits[i] << " ";
# }

# In Python:
print("Enumerate für Index und Wert:")
for index, frucht in enumerate(früchte):
    print(f"{index}: {frucht}", end=" | ")
print("\n")

# Mit Startindex
print("Enumerate mit Startindex 1:")
for index, frucht in enumerate(früchte, 1):
    print(f"{index}: {frucht}", end=" | ")
print("\n")

# ===== Zip für parallele Iteration =====
print("=== Zip für parallele Iteration ===")

# In C++:
# for (size_t i = 0; i < std::min(names.size(), ages.size()); i++) {
#     std::cout << names[i] << ": " << ages[i] << " ";
# }

# In Python:
namen = ["Max", "Anna", "Tim"]
alter = [30, 25, 35]

print("Parallele Iteration mit zip:")
for name, a in zip(namen, alter):
    print(f"{name}: {a}", end=" | ")
print("\n")

# ===== While-Schleife =====
print("=== While-Schleife ===")

# In C++:
# int count = 0;
# while (count < 5) {
#     std::cout << count << " ";
#     count++;
# }

# In Python:
print("Einfache While-Schleife:")
count = 0
while count < 5:
    print(count, end=" ")
    count += 1
print("\n")

# While mit break
print("While mit break:")
count = 0
while True:
    print(count, end=" ")
    count += 1
    if count >= 5:
        break
print("\n")

# While mit continue
print("While mit continue (nur gerade Zahlen):")
count = 0
while count < 10:
    count += 1
    if count % 2 != 0:  # Ungerade Zahlen überspringen
        continue
    print(count, end=" ")
print("\n")

# ===== Do-While Emulation =====
print("=== Do-While Emulation ===")

# In C++:
# do {
#     std::cout << count << " ";
#     count++;
# } while (count < 5);

# In Python (Emulation):
print("Do-While Emulation:")
count = 0
while True:
    print(count, end=" ")
    count += 1
    if count >= 5:
        break
print("\n")

# ===== Schleifensteuerung: break, continue, else =====
print("=== Schleifensteuerung: break, continue, else ===")

# break: Beendet die Schleife vorzeitig
print("break-Beispiel:")
for i in range(10):
    if i == 5:
        break
    print(i, end=" ")
print("\n")

# continue: Überspringt den Rest des aktuellen Durchlaufs
print("continue-Beispiel:")
for i in range(10):
    if i % 2 == 0:  # Gerade Zahlen überspringen
        continue
    print(i, end=" ")
print("\n")

# else-Klausel bei Schleifen (wird ausgeführt, wenn die Schleife normal beendet wird)
print("for-else-Beispiel (Suche nach 5):")
for i in range(1, 5):
    print(i, end=" ")
    if i == 5:
        print("\nGefunden!")
        break
else:
    print("\n5 wurde nicht gefunden!")

print("\nfor-else-Beispiel (Suche nach 3):")
for i in range(1, 5):
    print(i, end=" ")
    if i == 3:
        print("\nGefunden!")
        break
else:
    print("\n3 wurde nicht gefunden!")
print()

# ===== Verschachtelte Schleifen =====
print("=== Verschachtelte Schleifen ===")

# In C++:
# for (int i = 1; i <= 3; i++) {
#     for (int j = 1; j <= 3; j++) {
#         std::cout << i << "," << j << " ";
#     }
#     std::cout << std::endl;
# }

# In Python:
print("Verschachtelte Schleifen:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i},{j}", end=" ")
    print()  # Neue Zeile nach jeder äußeren Iteration
print()

# ===== Beispiel: Multiplikationstabelle =====
print("=== Beispiel: Multiplikationstabelle ===")

print("Multiplikationstabelle (1-5):")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:2d}", end=" ")
    print()
print()

# ===== ÜBUNG =====
print("=== ÜBUNG ===")
print("1. Schreibe eine Schleife, die die Summe der Zahlen von 1 bis 100 berechnet")
print("2. Schreibe eine Schleife, die alle Primzahlen bis 50 ausgibt")
print("3. Schreibe eine Funktion, die das Fibonacci-Sequenz bis zum n-ten Element berechnet")

# TODO: Schreibe deinen Code hier
# aufgabe1 = ...

# Beispiellösung (auskommentiert)
"""
# 1. Summe der Zahlen von 1 bis 100
summe = 0
for i in range(1, 101):
    summe += i
print(f"Die Summe der Zahlen von 1 bis 100 ist: {summe}")

# 2. Primzahlen bis 50
print("Primzahlen bis 50:")
for num in range(2, 51):
    ist_primzahl = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            ist_primzahl = False
            break
    if ist_primzahl:
        print(num, end=" ")
print()

# 3. Fibonacci-Sequenz
def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n+1):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    return fib_sequence

print(f"Fibonacci-Sequenz bis zum 10. Element: {fibonacci(10)}")
"""