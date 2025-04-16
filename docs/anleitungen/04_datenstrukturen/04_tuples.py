#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Tuples in Python
Vergleich mit C++
"""

# ===== Grundlagen von Tuples =====
print("=== Grundlagen von Tuples ===")

# In C++:
# std::tuple<int, std::string, double> person(25, "Max", 1.78);
# std::pair<std::string, int> name_alter("Max", 25);

# In Python:
person = (25, "Max", 1.78)
name_alter = ("Max", 25)

print(f"person: {person}")
print(f"name_alter: {name_alter}")

# Tuple mit einem Element
# Beachte das Komma, sonst ist es kein Tuple!
einzelwert = (42,)  # Mit Komma: Tuple
nicht_tuple = (42)  # Ohne Komma: Einfacher Integer
print(f"einzelwert (Tuple): {einzelwert}, Typ: {type(einzelwert)}")
print(f"nicht_tuple (kein Tuple): {nicht_tuple}, Typ: {type(nicht_tuple)}")

# Tuple ohne Klammern (Packing)
koordinaten = 10, 20, 30
print(f"koordinaten: {koordinaten}, Typ: {type(koordinaten)}")

# Leeres Tuple
leeres_tuple = ()
print(f"leeres_tuple: {leeres_tuple}")
print()

# ===== Zugriff auf Tuple-Elemente =====
print("=== Zugriff auf Tuple-Elemente ===")

# Indexierung (beginnt bei 0)
# In C++: std::get<0>(person), std::get<1>(person), ...
print(f"Alter: {person[0]}")
print(f"Name: {person[1]}")
print(f"Größe: {person[2]}")

# Negativer Index (von hinten zählen)
print(f"Letztes Element: {person[-1]}")
print(f"Vorletztes Element: {person[-2]}")

# Slicing (wie bei Listen)
zahlen = (0, 1, 2, 3, 4, 5)
print(f"Elemente 1-3: {zahlen[1:4]}")  # Indizes 1, 2, 3
print(f"Elemente bis 3: {zahlen[:3]}")  # Indizes 0, 1, 2
print(f"Elemente ab 2: {zahlen[2:]}")  # Indizes 2, 3, 4, 5
print()

# ===== Tuple-Eigenschaften =====
print("=== Tuple-Eigenschaften ===")

# Tuples sind unveränderbar (immutable)
# person[0] = 26  # TypeError: 'tuple' object does not support item assignment

# Aber: Wenn ein Tuple veränderbare Objekte enthält, können diese geändert werden
liste_in_tuple = ([1, 2, 3], "Text")
print(f"Original: {liste_in_tuple}")
liste_in_tuple[0].append(4)  # Die Liste innerhalb des Tuples kann geändert werden
print(f"Nach Änderung der inneren Liste: {liste_in_tuple}")

# Tuples sind hashable (wenn alle Elemente hashable sind)
# Daher können sie als Dictionary-Schlüssel oder Set-Elemente verwendet werden
punkt = (10, 20)
werte = {punkt: "Koordinaten"}
print(f"Dictionary mit Tuple als Schlüssel: {werte}")

# Tuples mit veränderbaren Objekten sind nicht hashable
# Folgendes würde einen Fehler verursachen:
# nicht_hashable = {([1, 2], 3): "Wert"}  # TypeError: unhashable type: 'list'
print()

# ===== Tuple-Operationen =====
print("=== Tuple-Operationen ===")

# Länge eines Tuples
print(f"Länge von person: {len(person)}")

# Konkatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
kombiniert = tuple1 + tuple2
print(f"tuple1 + tuple2: {kombiniert}")

# Wiederholung
wiederholt = tuple1 * 3
print(f"tuple1 * 3: {wiederholt}")

# Mitgliedschaftsprüfung mit in
enthält_max = "Max" in person
print(f"Enthält 'Max': {enthält_max}")

# Zählen von Elementen
zahlen = (1, 2, 2, 3, 3, 3, 4)
anzahl_2 = zahlen.count(2)
print(f"Anzahl von 2 in {zahlen}: {anzahl_2}")

# Index eines Elements finden
position = zahlen.index(3)  # Gibt den Index des ersten Vorkommens zurück
print(f"Position von 3 in {zahlen}: {position}")
print()

# ===== Tuple Unpacking =====
print("=== Tuple Unpacking ===")

# In C++:
# auto [name, alter] = name_alter;  // C++17 structured binding
# std::string name; int alter; std::tie(name, alter) = name_alter;  // vor C++17

# In Python:
name, alter = name_alter  # Unpacking
print(f"Name: {name}")
print(f"Alter: {alter}")

# Unpacking mit mehr Variablen
x, y, z = koordinaten
print(f"x: {x}, y: {y}, z: {z}")

# Unpacking mit * (Rest-Operator)
erste, *mitte, letzte = (1, 2, 3, 4, 5)
print(f"Erste: {erste}")
print(f"Mitte: {mitte}")  # Liste mit den mittleren Elementen
print(f"Letzte: {letzte}")

# Ignorieren von Werten mit _
a, _, c = (10, 20, 30)  # _ ist eine Konvention für ungenutzte Werte
print(f"a: {a}, c: {c}")

# Werte tauschen
a, b = 1, 2
print(f"Vor dem Tausch: a = {a}, b = {b}")
a, b = b, a  # Tuple-Unpacking zum Tauschen von Werten
print(f"Nach dem Tausch: a = {a}, b = {b}")
print()

# ===== Rückgabewerte von Funktionen =====
print("=== Rückgabewerte von Funktionen ===")

# Funktionen können Tuples zurückgeben
def get_person():
    return "Anna", 30, 1.65

# Unpacking des Rückgabewerts
name, alter, größe = get_person()
print(f"Name: {name}, Alter: {alter}, Größe: {größe}")

# Oder als Tuple speichern
person = get_person()
print(f"Person: {person}")
print()

# ===== Named Tuples =====
print("=== Named Tuples ===")

# In C++ gibt es kein direktes Äquivalent (außer eigene Strukturen)

from collections import namedtuple

# Definition eines Named Tuple
Person = namedtuple('Person', ['name', 'alter', 'größe'])

# Erstellen einer Instanz
max_person = Person(name="Max", alter=25, größe=1.78)
print(f"max_person: {max_person}")

# Zugriff über Namen
print(f"Name: {max_person.name}")
print(f"Alter: {max_person.alter}")
print(f"Größe: {max_person.größe}")

# Zugriff über Index (wie bei normalen Tuples)
print(f"Erstes Element: {max_person[0]}")

# Unpacking funktioniert auch
name, alter, größe = max_person
print(f"Unpacked: Name={name}, Alter={alter}, Größe={größe}")

# Named Tuples sind immutable
# max_person.alter = 26  # AttributeError: can't set attribute

# Aber man kann eine neue Instanz mit geänderten Werten erstellen
max_älter = max_person._replace(alter=26)
print(f"Geänderte Person: {max_älter}")
print()

# ===== Anwendungsbeispiele =====
print("=== Anwendungsbeispiele ===")

# 1. Koordinaten
punkt_2d = (10, 20)
punkt_3d = (10, 20, 30)

# 2. Datensätze mit fester Struktur
student = ("Max Mustermann", "Informatik", 2, 1.7)  # Name, Fach, Semester, Note

# 3. Mehrere Rückgabewerte
def minmax(zahlen):
    return min(zahlen), max(zahlen)

minimum, maximum = minmax([5, 3, 8, 1, 9])
print(f"Minimum: {minimum}, Maximum: {maximum}")

# 4. Dictionary-Elemente
wörterbuch = {"a": 1, "b": 2, "c": 3}
for item in wörterbuch.items():
    print(f"Schlüssel-Wert-Paar: {item}")

# Mit Unpacking
for schlüssel, wert in wörterbuch.items():
    print(f"Schlüssel: {schlüssel}, Wert: {wert}")
print()

# ===== Vergleich: Tuple vs. Liste vs. Set =====
print("=== Vergleich: Tuple vs. Liste vs. Set ===")

print("Tuple:")
print("- Unveränderbar (immutable)")
print("- Geordnet (Reihenfolge bleibt erhalten)")
print("- Erlaubt Duplikate")
print("- Kann als Dictionary-Schlüssel oder Set-Element verwendet werden")
print("- Gut für Daten, die sich nicht ändern sollen")
print("- Etwas schneller als Listen")

print("\nListe:")
print("- Veränderbar (mutable)")
print("- Geordnet (Reihenfolge bleibt erhalten)")
print("- Erlaubt Duplikate")
print("- Kann nicht als Dictionary-Schlüssel oder Set-Element verwendet werden")
print("- Gut für Sammlungen, die sich ändern können")

print("\nSet:")
print("- Veränderbar (mutable)")
print("- Ungeordnet (keine garantierte Reihenfolge)")
print("- Keine Duplikate")
print("- Kann nicht als Dictionary-Schlüssel verwendet werden")
print("- Gut für Mengenoperationen und Entfernen von Duplikaten")
print()

# ===== ÜBUNG =====
print("=== ÜBUNG ===")
print("1. Erstelle ein Tuple mit deinen Lieblingsfächern")
print("2. Schreibe eine Funktion, die zwei Werte entgegennimmt und sie als Tuple zurückgibt")
print("3. Erstelle ein Named Tuple für ein Buch mit Titel, Autor und Erscheinungsjahr")
print("4. Schreibe eine Funktion, die eine Liste von Zahlenpaaren (als Tuples) sortiert, basierend auf dem zweiten Element jedes Paares")

# TODO: Schreibe deinen Code hier
# aufgabe1 = ...

# Beispiellösung (auskommentiert)
"""
# 1. Lieblingsfächer
lieblingsfächer = ("Informatik", "Mathematik", "Physik")
print(f"Meine Lieblingsfächer: {lieblingsfächer}")

# 2. Funktion mit Tuple-Rückgabe
def addiere_und_multipliziere(a, b):
    summe = a + b
    produkt = a * b
    return summe, produkt

ergebnis = addiere_und_multipliziere(3, 4)
print(f"Ergebnis als Tuple: {ergebnis}")

# Mit Unpacking
summe, produkt = addiere_und_multipliziere(3, 4)
print(f"Summe: {summe}, Produkt: {produkt}")

# 3. Named Tuple für Buch
from collections import namedtuple

Buch = namedtuple('Buch', ['titel', 'autor', 'jahr'])
mein_buch = Buch(titel="Der Herr der Ringe", autor="J.R.R. Tolkien", jahr=1954)
print(f"Mein Buch: {mein_buch}")
print(f"Titel: {mein_buch.titel}")

# 4. Sortieren nach zweitem Element
def sortiere_nach_zweitem(paare):
    return sorted(paare, key=lambda paar: paar[1])

zahlenpaare = [(1, 5), (3, 2), (2, 8), (4, 1)]
sortiert = sortiere_nach_zweitem(zahlenpaare)
print(f"Original: {zahlenpaare}")
print(f"Sortiert nach zweitem Element: {sortiert}")
"""