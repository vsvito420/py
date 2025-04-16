#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
List Comprehensions und Generator Expressions in Python
Ein Konzept, das in C++ nicht direkt existiert
"""

# ===== Grundlegende List Comprehension =====
print("=== Grundlegende List Comprehension ===")

# Traditionelle Schleife in C++ und Python:
# C++:
# std::vector<int> squares;
# for (int i = 0; i < 10; i++) {
#     squares.push_back(i * i);
# }

# Python mit traditioneller Schleife:
quadrate_traditionell = []
for i in range(10):
    quadrate_traditionell.append(i * i)
print(f"Traditionelle Schleife: {quadrate_traditionell}")

# Mit List Comprehension:
quadrate = [i * i for i in range(10)]
print(f"List Comprehension: {quadrate}")

# Lesbarkeit: Die List Comprehension ist kürzer und oft lesbarer
print()

# ===== List Comprehension mit Bedingung =====
print("=== List Comprehension mit Bedingung ===")

# Traditionelle Schleife mit if:
gerade_zahlen_traditionell = []
for i in range(20):
    if i % 2 == 0:
        gerade_zahlen_traditionell.append(i)
print(f"Traditionelle Schleife mit if: {gerade_zahlen_traditionell}")

# Mit List Comprehension und if:
gerade_zahlen = [i for i in range(20) if i % 2 == 0]
print(f"List Comprehension mit if: {gerade_zahlen}")
print()

# ===== List Comprehension mit if-else =====
print("=== List Comprehension mit if-else ===")

# Traditionelle Schleife mit if-else:
ergebnis_traditionell = []
for i in range(10):
    if i % 2 == 0:
        ergebnis_traditionell.append("gerade")
    else:
        ergebnis_traditionell.append("ungerade")
print(f"Traditionelle Schleife mit if-else: {ergebnis_traditionell}")

# Mit List Comprehension und if-else:
# Beachte: if-else steht VOR dem for, wenn es Teil des Ausdrucks ist
ergebnis = ["gerade" if i % 2 == 0 else "ungerade" for i in range(10)]
print(f"List Comprehension mit if-else: {ergebnis}")
print()

# ===== Verschachtelte List Comprehensions =====
print("=== Verschachtelte List Comprehensions ===")

# Traditionelle verschachtelte Schleifen:
matrix_traditionell = []
for i in range(3):
    zeile = []
    for j in range(3):
        zeile.append(i * j)
    matrix_traditionell.append(zeile)
print(f"Traditionelle verschachtelte Schleifen: {matrix_traditionell}")

# Mit verschachtelter List Comprehension:
matrix = [[i * j for j in range(3)] for i in range(3)]
print(f"Verschachtelte List Comprehension: {matrix}")
print()

# ===== List Comprehension mit verschiedenen Datentypen =====
print("=== List Comprehension mit verschiedenen Datentypen ===")

# Strings
wörter = ["Python", "ist", "eine", "großartige", "Sprache"]
längen = [len(wort) for wort in wörter]
print(f"Wörter: {wörter}")
print(f"Wortlängen: {längen}")

# Dictionaries
personen = [{"name": "Max", "alter": 30}, {"name": "Anna", "alter": 25}, {"name": "Tim", "alter": 35}]
namen = [person["name"] for person in personen]
print(f"Namen aus Dictionary-Liste: {namen}")

# Umwandlung von Datentypen
zahlen_als_strings = ["1", "2", "3", "4", "5"]
zahlen = [int(num) for num in zahlen_als_strings]
print(f"Strings zu Integers: {zahlen}")
print()

# ===== List Comprehension vs. map() und filter() =====
print("=== List Comprehension vs. map() und filter() ===")

# map() - wendet eine Funktion auf jedes Element an
# In C++: std::transform
zahlen = [1, 2, 3, 4, 5]
quadrate_map = list(map(lambda x: x * x, zahlen))
print(f"map(): {quadrate_map}")

# Äquivalente List Comprehension:
quadrate_comp = [x * x for x in zahlen]
print(f"List Comprehension: {quadrate_comp}")

# filter() - filtert Elemente basierend auf einer Funktion
# In C++: std::copy_if
gerade_filter = list(filter(lambda x: x % 2 == 0, zahlen))
print(f"filter(): {gerade_filter}")

# Äquivalente List Comprehension:
gerade_comp = [x for x in zahlen if x % 2 == 0]
print(f"List Comprehension mit Filter: {gerade_comp}")

# Kombination von map und filter:
ergebnis_funktional = list(map(lambda x: x * x, filter(lambda x: x % 2 == 0, zahlen)))
print(f"map() + filter(): {ergebnis_funktional}")

# Äquivalente List Comprehension:
ergebnis_comp = [x * x for x in zahlen if x % 2 == 0]
print(f"List Comprehension mit Filter: {ergebnis_comp}")
print()

# ===== Dictionary Comprehensions =====
print("=== Dictionary Comprehensions ===")

# Traditionelle Schleife:
quadrat_dict_traditionell = {}
for i in range(5):
    quadrat_dict_traditionell[i] = i * i
print(f"Traditionelles Dictionary: {quadrat_dict_traditionell}")

# Mit Dictionary Comprehension:
quadrat_dict = {i: i * i for i in range(5)}
print(f"Dictionary Comprehension: {quadrat_dict}")

# Mit Bedingung:
gerade_quadrate = {i: i * i for i in range(10) if i % 2 == 0}
print(f"Dictionary Comprehension mit Filter: {gerade_quadrate}")

# Umwandlung einer Liste von Tupeln in ein Dictionary:
paare = [("a", 1), ("b", 2), ("c", 3)]
buchstaben_dict = {k: v for k, v in paare}
print(f"Liste von Tupeln zu Dictionary: {buchstaben_dict}")

# Umwandlung eines Dictionary:
personen = {"Max": 30, "Anna": 25, "Tim": 35}
personen_umgekehrt = {alter: name for name, alter in personen.items()}
print(f"Umgekehrtes Dictionary: {personen_umgekehrt}")
print()

# ===== Set Comprehensions =====
print("=== Set Comprehensions ===")

# Traditionelle Schleife:
quadrat_set_traditionell = set()
for i in range(5):
    quadrat_set_traditionell.add(i * i)
print(f"Traditionelles Set: {quadrat_set_traditionell}")

# Mit Set Comprehension:
quadrat_set = {i * i for i in range(5)}
print(f"Set Comprehension: {quadrat_set}")

# Mit Bedingung:
gerade_quadrate_set = {i * i for i in range(10) if i % 2 == 0}
print(f"Set Comprehension mit Filter: {gerade_quadrate_set}")

# Entfernen von Duplikaten aus einer Liste:
zahlen_mit_duplikaten = [1, 2, 2, 3, 3, 3, 4, 5, 5]
eindeutige_zahlen = {x for x in zahlen_mit_duplikaten}
print(f"Eindeutige Zahlen als Set: {eindeutige_zahlen}")
print()

# ===== Generator Expressions =====
print("=== Generator Expressions ===")

# List Comprehension (erzeugt die gesamte Liste auf einmal):
quadrate_liste = [i * i for i in range(10)]
print(f"List Comprehension: {quadrate_liste}")

# Generator Expression (erzeugt Werte bei Bedarf):
quadrate_generator = (i * i for i in range(10))
print(f"Generator Expression: {quadrate_generator}")

# Iteration über Generator:
print("Iteration über Generator:")
for q in quadrate_generator:
    print(q, end=" ")
print("\n")

# Vorteile von Generator Expressions:
# 1. Speichereffizienz bei großen Datenmengen
# 2. Lazy Evaluation (Werte werden nur bei Bedarf berechnet)

# Beispiel mit großem Bereich:
# Würde viel Speicher verbrauchen als Liste:
# große_liste = [i for i in range(1000000)]

# Als Generator effizient:
großer_generator = (i for i in range(10))
print(f"Erster Wert aus Generator: {next(großer_generator)}")
print(f"Zweiter Wert aus Generator: {next(großer_generator)}")
print()

# ===== Praktische Anwendungen =====
print("=== Praktische Anwendungen ===")

# Dateiverarbeitung:
# Angenommen, wir haben eine Textdatei mit Zahlen
# Mit Generator Expression:
# zahlen_aus_datei = (int(line.strip()) for line in open("zahlen.txt"))

# Datenverarbeitung:
daten = [
    {"name": "Max", "alter": 30, "stadt": "Berlin"},
    {"name": "Anna", "alter": 25, "stadt": "München"},
    {"name": "Tim", "alter": 35, "stadt": "Berlin"},
    {"name": "Lisa", "alter": 28, "stadt": "Hamburg"}
]

# Filtern und Transformieren:
berliner = [person["name"] for person in daten if person["stadt"] == "Berlin"]
print(f"Personen aus Berlin: {berliner}")

# Durchschnittsalter berechnen:
durchschnittsalter = sum(person["alter"] for person in daten) / len(daten)
print(f"Durchschnittsalter: {durchschnittsalter}")
print()

# ===== ÜBUNG =====
print("=== ÜBUNG ===")
print("1. Erstelle eine List Comprehension, die alle Zahlen von 1 bis 20 enthält, die durch 3 teilbar sind")
print("2. Erstelle ein Dictionary mit den Quadraten der Zahlen von 1 bis 5 als Werte und den Zahlen als Schlüssel")
print("3. Erstelle einen Generator für die ersten 10 Fibonacci-Zahlen")

# TODO: Schreibe deinen Code hier
# aufgabe1 = ...

# Beispiellösung (auskommentiert)
"""
# 1. Zahlen teilbar durch 3
aufgabe1 = [i for i in range(1, 21) if i % 3 == 0]
print(f"Zahlen von 1-20, teilbar durch 3: {aufgabe1}")

# 2. Dictionary mit Quadraten
aufgabe2 = {i: i**2 for i in range(1, 6)}
print(f"Dictionary mit Quadraten: {aufgabe2}")

# 3. Fibonacci-Generator
def fibonacci_generator(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

aufgabe3 = list(fibonacci_generator(10))
print(f"Erste 10 Fibonacci-Zahlen: {aufgabe3}")
"""