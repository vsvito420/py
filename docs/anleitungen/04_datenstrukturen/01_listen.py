#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Listen in Python
Vergleich mit C++
"""

# ===== Grundlagen von Listen =====
print("=== Grundlagen von Listen ===")

# In C++:
# std::vector<int> zahlen = {1, 2, 3, 4, 5};
# std::vector<std::string> namen = {"Max", "Anna", "Tim"};

# In Python:
zahlen = [1, 2, 3, 4, 5]
namen = ["Max", "Anna", "Tim"]

print(f"zahlen: {zahlen}")
print(f"namen: {namen}")

# Heterogene Listen (verschiedene Datentypen)
# In C++ nicht direkt möglich ohne Wrapper-Klassen oder std::variant
gemischt = [1, "Text", 3.14, True, [1, 2, 3]]
print(f"gemischt: {gemischt}")
print(f"Typ des ersten Elements: {type(gemischt[0])}")
print(f"Typ des zweiten Elements: {type(gemischt[1])}")
print()

# ===== Zugriff auf Listenelemente =====
print("=== Zugriff auf Listenelemente ===")

# Indexierung (beginnt bei 0)
# In C++: zahlen[0], zahlen[1], ...
print(f"Erstes Element: {zahlen[0]}")
print(f"Zweites Element: {zahlen[1]}")

# Negativer Index (von hinten zählen)
# In C++ nicht direkt möglich
print(f"Letztes Element: {zahlen[-1]}")
print(f"Vorletztes Element: {zahlen[-2]}")

# Slicing (Teilbereiche)
# In C++ nicht direkt möglich, erfordert Iteratoren oder Algorithmen
print(f"Elemente 1-3: {zahlen[1:4]}")  # Indizes 1, 2, 3 (bis 4 exklusiv)
print(f"Elemente bis 3: {zahlen[:3]}")  # Indizes 0, 1, 2
print(f"Elemente ab 2: {zahlen[2:]}")  # Indizes 2, 3, 4
print(f"Letzten 2 Elemente: {zahlen[-2:]}")  # Indizes -2, -1

# Slicing mit Schrittweite
print(f"Jedes zweite Element: {zahlen[::2]}")  # Indizes 0, 2, 4
print(f"Rückwärts: {zahlen[::-1]}")  # Umgekehrte Reihenfolge
print()

# ===== Listen verändern =====
print("=== Listen verändern ===")

# Listen sind veränderbar (mutable)
zahlen[0] = 10
print(f"Nach Änderung des ersten Elements: {zahlen}")

# Teilbereiche ersetzen
zahlen[1:3] = [20, 30]
print(f"Nach Ersetzen von Elementen 1-2: {zahlen}")

# Mehr Elemente einfügen als ersetzt werden
zahlen[1:2] = [22, 23, 24]
print(f"Nach Einfügen mehrerer Elemente: {zahlen}")

# Elemente entfernen durch leere Liste ersetzen
zahlen[1:4] = []
print(f"Nach Entfernen von Elementen: {zahlen}")
print()

# ===== Listenmethoden =====
print("=== Listenmethoden ===")

# Liste erstellen
früchte = ["Apfel", "Banane", "Kirsche"]
print(f"Ursprüngliche Liste: {früchte}")

# append() - Element am Ende hinzufügen
# In C++: früchte.push_back("Orange");
früchte.append("Orange")
print(f"Nach append(): {früchte}")

# insert() - Element an bestimmter Position einfügen
# In C++: früchte.insert(früchte.begin() + 1, "Birne");
früchte.insert(1, "Birne")
print(f"Nach insert(): {früchte}")

# extend() - Liste um mehrere Elemente erweitern
# In C++: früchte.insert(früchte.end(), neue_früchte.begin(), neue_früchte.end());
früchte.extend(["Mango", "Ananas"])
print(f"Nach extend(): {früchte}")

# remove() - Element nach Wert entfernen
# In C++: früchte.erase(std::remove(früchte.begin(), früchte.end(), "Birne"), früchte.end());
früchte.remove("Birne")
print(f"Nach remove(): {früchte}")

# pop() - Element an bestimmter Position entfernen und zurückgeben
# In C++: auto element = früchte[2]; früchte.erase(früchte.begin() + 2);
element = früchte.pop(2)
print(f"Entferntes Element: {element}")
print(f"Nach pop(2): {früchte}")

# pop() ohne Index entfernt das letzte Element
# In C++: auto letztes = früchte.back(); früchte.pop_back();
letztes = früchte.pop()
print(f"Letztes Element: {letztes}")
print(f"Nach pop(): {früchte}")

# clear() - Alle Elemente entfernen
# In C++: früchte.clear();
früchte_kopie = früchte.copy()  # Kopie erstellen, um später zu demonstrieren
früchte_kopie.clear()
print(f"Nach clear(): {früchte_kopie}")
print()

# ===== Suchen und Sortieren =====
print("=== Suchen und Sortieren ===")

# index() - Position eines Elements finden
# In C++: auto pos = std::find(früchte.begin(), früchte.end(), "Apfel") - früchte.begin();
position = früchte.index("Apfel")
print(f"Position von 'Apfel': {position}")

# count() - Anzahl der Vorkommen zählen
# In C++: auto anzahl = std::count(früchte.begin(), früchte.end(), "Apfel");
früchte.append("Apfel")  # Zweites "Apfel" hinzufügen
anzahl = früchte.count("Apfel")
print(f"Anzahl von 'Apfel': {anzahl}")

# sort() - Liste sortieren
# In C++: std::sort(früchte.begin(), früchte.end());
früchte.sort()
print(f"Sortierte Liste: {früchte}")

# reverse() - Liste umkehren
# In C++: std::reverse(früchte.begin(), früchte.end());
früchte.reverse()
print(f"Umgekehrte Liste: {früchte}")
print()

# ===== Listen und Operatoren =====
print("=== Listen und Operatoren ===")

liste1 = [1, 2, 3]
liste2 = [4, 5, 6]

# Konkatenation mit +
# In C++: std::vector<int> ergebnis(liste1); ergebnis.insert(ergebnis.end(), liste2.begin(), liste2.end());
ergebnis = liste1 + liste2
print(f"liste1 + liste2: {ergebnis}")

# Wiederholung mit *
# In C++ nicht direkt möglich
wiederholung = liste1 * 3
print(f"liste1 * 3: {wiederholung}")

# in-Operator zum Prüfen der Mitgliedschaft
# In C++: bool enthalten = std::find(liste1.begin(), liste1.end(), 2) != liste1.end();
enthalten = 2 in liste1
print(f"Ist 2 in liste1 enthalten? {enthalten}")
print()

# ===== Listen-Comprehensions =====
print("=== Listen-Comprehensions ===")

# In C++ nicht direkt möglich, erfordert Algorithmen oder Schleifen

# Einfache Liste mit Quadratzahlen
quadrate = [x**2 for x in range(1, 6)]
print(f"Quadratzahlen: {quadrate}")

# Mit Bedingung
gerade_quadrate = [x**2 for x in range(1, 11) if x % 2 == 0]
print(f"Quadrate gerader Zahlen: {gerade_quadrate}")

# Verschachtelte Schleifen
paare = [(x, y) for x in range(1, 3) for y in range(1, 3)]
print(f"Alle Paare: {paare}")
print()

# ===== Nützliche Funktionen für Listen =====
print("=== Nützliche Funktionen für Listen ===")

zahlen = [5, 2, 8, 1, 9]

# len() - Länge der Liste
# In C++: zahlen.size()
print(f"Länge: {len(zahlen)}")

# min() und max() - Minimum und Maximum
# In C++: auto min_wert = *std::min_element(zahlen.begin(), zahlen.end());
print(f"Minimum: {min(zahlen)}")
print(f"Maximum: {max(zahlen)}")

# sum() - Summe aller Elemente
# In C++: auto summe = std::accumulate(zahlen.begin(), zahlen.end(), 0);
print(f"Summe: {sum(zahlen)}")

# sorted() - Sortierte Kopie erstellen (Original bleibt unverändert)
# In C++: std::vector<int> sortiert(zahlen); std::sort(sortiert.begin(), sortiert.end());
sortiert = sorted(zahlen)
print(f"Original: {zahlen}")
print(f"Sortiert: {sortiert}")

# reversed() - Umgekehrter Iterator (nicht direkt eine Liste)
# In C++: std::vector<int> umgekehrt(zahlen.rbegin(), zahlen.rend());
umgekehrt = list(reversed(zahlen))
print(f"Umgekehrt: {umgekehrt}")
print()

# ===== Verschachtelte Listen (Matrizen) =====
print("=== Verschachtelte Listen (Matrizen) ===")

# In C++:
# std::vector<std::vector<int>> matrix = {
#     {1, 2, 3},
#     {4, 5, 6},
#     {7, 8, 9}
# };

# In Python:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(f"Matrix: {matrix}")

# Zugriff auf Elemente
print(f"Element in Zeile 1, Spalte 2: {matrix[1][2]}")  # Zeile 1, Spalte 2 = 6

# Zeile ändern
matrix[0] = [10, 20, 30]
print(f"Nach Änderung der ersten Zeile: {matrix}")

# Element ändern
matrix[1][1] = 50
print(f"Nach Änderung eines Elements: {matrix}")

# Zeilen durchlaufen
print("Zeilen der Matrix:")
for zeile in matrix:
    print(zeile)

# Matrix mit List Comprehension erstellen
# 3x3-Matrix mit Nullen
nullmatrix = [[0 for _ in range(3)] for _ in range(3)]
print(f"Nullmatrix: {nullmatrix}")

# Identitätsmatrix
identität = [[1 if i == j else 0 for j in range(3)] for i in range(3)]
print(f"Identitätsmatrix: {identität}")
print()

# ===== Listen kopieren =====
print("=== Listen kopieren ===")

# Flache Kopie
original = [1, 2, [3, 4]]
kopie1 = original.copy()  # Äquivalent zu kopie1 = list(original) oder kopie1 = original[:]
print(f"Original: {original}")
print(f"Kopie: {kopie1}")

# Änderung am Original
original[0] = 10
print(f"Original nach Änderung: {original}")
print(f"Kopie nach Änderung am Original: {kopie1}")  # Kopie bleibt unverändert

# Änderung an verschachtelter Liste
original[2][0] = 30
print(f"Original nach Änderung der verschachtelten Liste: {original}")
print(f"Kopie nach Änderung der verschachtelten Liste: {kopie1}")  # Verschachtelte Liste wird geändert!

# Tiefe Kopie
import copy
original = [1, 2, [3, 4]]
tiefe_kopie = copy.deepcopy(original)

original[2][0] = 30
print(f"Original nach Änderung: {original}")
print(f"Tiefe Kopie nach Änderung: {tiefe_kopie}")  # Bleibt vollständig unverändert
print()

# ===== Listen als Stacks und Queues =====
print("=== Listen als Stacks und Queues ===")

# Stack (LIFO - Last In, First Out)
stack = []
stack.append(1)  # push
stack.append(2)
stack.append(3)
print(f"Stack: {stack}")

element = stack.pop()  # pop
print(f"Entferntes Element: {element}")
print(f"Stack nach pop(): {stack}")

# Queue (FIFO - First In, First Out)
# Listen sind nicht effizient für Queues, besser: collections.deque
from collections import deque
queue = deque([1, 2, 3])
print(f"Queue: {queue}")

queue.append(4)  # Hinzufügen am Ende
print(f"Queue nach append(): {queue}")

element = queue.popleft()  # Entfernen vom Anfang
print(f"Entferntes Element: {element}")
print(f"Queue nach popleft(): {queue}")
print()

# ===== Leistungsvergleich =====
print("=== Leistungsvergleich ===")

# Listen sind effizient für:
# - Zugriff auf Elemente mit Index: O(1)
# - Anhängen am Ende: O(1) (amortisiert)
# - Entfernen vom Ende: O(1)

# Listen sind weniger effizient für:
# - Einfügen/Entfernen am Anfang oder in der Mitte: O(n)
# - Suchen nach Werten: O(n)

import time

# Beispiel: Einfügen am Anfang vs. am Ende
n = 10000
start_time = time.time()
liste_anfang = []
for i in range(n):
    liste_anfang.insert(0, i)  # Einfügen am Anfang
end_time = time.time()
print(f"Zeit für Einfügen am Anfang: {end_time - start_time:.6f} Sekunden")

start_time = time.time()
liste_ende = []
for i in range(n):
    liste_ende.append(i)  # Einfügen am Ende
end_time = time.time()
print(f"Zeit für Einfügen am Ende: {end_time - start_time:.6f} Sekunden")
print()

# ===== ÜBUNG =====
print("=== ÜBUNG ===")
print("1. Erstelle eine Liste mit den Quadratzahlen von 1 bis 10")
print("2. Schreibe eine Funktion, die das Produkt aller Elemente einer Liste berechnet")
print("3. Erstelle eine 3x3-Matrix und berechne die Summe aller Elemente")

# TODO: Schreibe deinen Code hier
# aufgabe1 = ...

# Beispiellösung (auskommentiert)
"""
# 1. Liste mit Quadratzahlen
aufgabe1 = [x**2 for x in range(1, 11)]
print(f"Quadratzahlen von 1 bis 10: {aufgabe1}")

# 2. Produkt aller Elemente
def produkt(liste):
    # Berechnet das Produkt aller Elemente in der Liste
    ergebnis = 1
    for element in liste:
        ergebnis *= element
    return ergebnis

zahlen = [1, 2, 3, 4, 5]
print(f"Produkt von {zahlen}: {produkt(zahlen)}")

# 3. Summe aller Elemente einer Matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Variante 1: Verschachtelte Schleifen
summe = 0
for zeile in matrix:
    for element in zeile:
        summe += element
print(f"Summe aller Elemente: {summe}")

# Variante 2: List Comprehension und sum
summe2 = sum([element for zeile in matrix for element in zeile])
print(f"Summe aller Elemente (mit List Comprehension): {summe2}")
"""