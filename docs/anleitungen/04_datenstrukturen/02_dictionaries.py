#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Dictionaries in Python
Vergleich mit C++
"""

# ===== Grundlagen von Dictionaries =====
print("=== Grundlagen von Dictionaries ===")

# In C++:
# std::map<std::string, int> alter = {{"Max", 25}, {"Anna", 30}, {"Tim", 22}};
# std::unordered_map<std::string, int> alter_unordered = {{"Max", 25}, {"Anna", 30}, {"Tim", 22}};

# In Python:
alter = {"Max": 25, "Anna": 30, "Tim": 22}
print(f"alter: {alter}")

# Verschiedene Datentypen als Schlüssel und Werte
# In C++ sind komplexe Schlüssel schwieriger zu implementieren
gemischt = {
    "name": "Max",
    42: "Antwort",
    3.14: "Pi",
    True: "Wahr",
    (1, 2): "Tupel"  # Tupel können Schlüssel sein, Listen nicht!
}
print(f"gemischt: {gemischt}")
print()

# ===== Zugriff auf Dictionary-Elemente =====
print("=== Zugriff auf Dictionary-Elemente ===")

# Zugriff über Schlüssel
# In C++: alter["Max"], alter.at("Max")
print(f"Alter von Max: {alter['Max']}")

# get() - Sicherer Zugriff mit Standardwert
# In C++: alter.count("Lisa") ? alter["Lisa"] : 0;
print(f"Alter von Lisa (mit get): {alter.get('Lisa', 0)}")

# Schlüssel prüfen mit in
# In C++: alter.count("Max") > 0
if "Max" in alter:
    print("Max ist im Dictionary enthalten")

# Werte ändern
alter["Max"] = 26
print(f"Neues Alter von Max: {alter['Max']}")

# Neuen Eintrag hinzufügen
alter["Lisa"] = 28
print(f"Nach Hinzufügen von Lisa: {alter}")
print()

# ===== Dictionary-Methoden =====
print("=== Dictionary-Methoden ===")

# Kopie erstellen
personen = alter.copy()
print(f"Kopie des Dictionaries: {personen}")

# keys() - Alle Schlüssel
# In C++: Iteration über die Schlüssel erfordert mehr Code
schlüssel = list(personen.keys())
print(f"Alle Schlüssel: {schlüssel}")

# values() - Alle Werte
werte = list(personen.values())
print(f"Alle Werte: {werte}")

# items() - Alle Schlüssel-Wert-Paare
paare = list(personen.items())
print(f"Alle Paare: {paare}")

# pop() - Element entfernen und zurückgeben
entfernt = personen.pop("Tim")
print(f"Entfernter Wert: {entfernt}")
print(f"Nach Entfernen von Tim: {personen}")

# popitem() - Letztes Element entfernen und zurückgeben
letztes_paar = personen.popitem()
print(f"Letztes entferntes Paar: {letztes_paar}")
print(f"Nach popitem(): {personen}")

# update() - Dictionary mit anderem Dictionary aktualisieren
personen.update({"Max": 27, "Sarah": 31})
print(f"Nach update(): {personen}")

# clear() - Alle Elemente entfernen
personen_kopie = personen.copy()
personen_kopie.clear()
print(f"Nach clear(): {personen_kopie}")
print()

# ===== Dictionary Comprehensions =====
print("=== Dictionary Comprehensions ===")

# In C++ nicht direkt möglich

# Quadratzahlen als Dictionary
zahlen = [1, 2, 3, 4, 5]
quadrate = {x: x**2 for x in zahlen}
print(f"Quadratzahlen: {quadrate}")

# Mit Bedingung
gerade_quadrate = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(f"Quadrate gerader Zahlen: {gerade_quadrate}")

# Umwandlung von Listen in Dictionaries
namen = ["Max", "Anna", "Tim"]
längen = {name: len(name) for name in namen}
print(f"Namenlängen: {längen}")
print()

# ===== Verschachtelte Dictionaries =====
print("=== Verschachtelte Dictionaries ===")

# In C++:
# std::map<std::string, std::map<std::string, std::string>> studenten = {
#     {"Max", {{"Fach", "Informatik"}, {"Note", "1.3"}}},
#     {"Anna", {{"Fach", "Physik"}, {"Note", "1.7"}}}
# };

# In Python:
studenten = {
    "Max": {"Fach": "Informatik", "Note": 1.3},
    "Anna": {"Fach": "Physik", "Note": 1.7}
}

print(f"Studenten: {studenten}")
print(f"Fach von Max: {studenten['Max']['Fach']}")

# Neuen verschachtelten Eintrag hinzufügen
studenten["Tim"] = {"Fach": "Mathematik", "Note": 1.0}
print(f"Nach Hinzufügen von Tim: {studenten}")

# Wert in verschachteltem Dictionary ändern
studenten["Max"]["Note"] = 1.0
print(f"Nach Änderung der Note von Max: {studenten}")
print()

# ===== Anwendungsbeispiele =====
print("=== Anwendungsbeispiele ===")

# Häufigkeitszählung
text = "Python ist eine großartige Programmiersprache. Python ist einfach zu lernen."
wörter = text.lower().replace(".", "").split()

# Variante 1: Mit Counter
from collections import Counter
häufigkeit = Counter(wörter)
print(f"Worthäufigkeit mit Counter: {häufigkeit}")
print(f"Häufigste Wörter: {häufigkeit.most_common(2)}")

# Variante 2: Manuell mit Dictionary
häufigkeit_manuell = {}
for wort in wörter:
    if wort in häufigkeit_manuell:
        häufigkeit_manuell[wort] += 1
    else:
        häufigkeit_manuell[wort] = 1
print(f"Worthäufigkeit manuell: {häufigkeit_manuell}")

# Variante 3: Mit get()
häufigkeit_get = {}
for wort in wörter:
    häufigkeit_get[wort] = häufigkeit_get.get(wort, 0) + 1
print(f"Worthäufigkeit mit get(): {häufigkeit_get}")
print()

# ===== Leistungsvergleich =====
print("=== Leistungsvergleich ===")

# Dictionaries sind effizient für:
# - Zugriff auf Elemente mit Schlüssel: O(1) im Durchschnitt
# - Einfügen/Entfernen von Elementen: O(1) im Durchschnitt

# Dictionaries vs. Listen für Lookups
import time

# Liste mit Namen und Alter
namen_liste = ["Person1", "Person2", "Person3", "Person4", "Person5", "Person6", "Person7", "Person8", "Person9", "Person10"]
alter_liste = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65]  # Entsprechende Alter

# Dictionary mit Namen und Alter
namen_dict = {"Person1": 20, "Person2": 25, "Person3": 30, "Person4": 35, "Person5": 40,
              "Person6": 45, "Person7": 50, "Person8": 55, "Person9": 60, "Person10": 65}

# Suche in Liste (langsam für große Listen)
def finde_alter_liste(name):
    for i, n in enumerate(namen_liste):
        if n == name:
            return alter_liste[i]
    return None

# Suche in Dictionary (schnell)
def finde_alter_dict(name):
    return namen_dict.get(name)

print("Dictionaries sind viel schneller für Lookups als Listen, besonders bei großen Datenmengen.")
print("Für 1000 Einträge kann der Unterschied mehrere Größenordnungen betragen.")
print()

# ===== ÜBUNG =====
print("=== ÜBUNG ===")
print("1. Erstelle ein Dictionary mit deinen Lieblingsbüchern und ihren Autoren")
print("2. Schreibe eine Funktion, die ein Dictionary invertiert (Werte werden zu Schlüsseln und umgekehrt)")
print("3. Zähle die Häufigkeit der Buchstaben in einem Text mit einem Dictionary")

# TODO: Schreibe deinen Code hier
# aufgabe1 = ...

# Beispiellösung (auskommentiert)
"""
# 1. Lieblingsbücher
bücher = {
    "Der Herr der Ringe": "J.R.R. Tolkien",
    "Harry Potter": "J.K. Rowling",
    "Die Verwandlung": "Franz Kafka"
}
print(f"Meine Lieblingsbücher: {bücher}")

# 2. Dictionary invertieren
def invertiere_dict(d):
    # Beachte: Bei doppelten Werten gehen Informationen verloren!
    return {wert: schlüssel for schlüssel, wert in d.items()}

invertiert = invertiere_dict(bücher)
print(f"Invertiertes Dictionary: {invertiert}")

# 3. Buchstabenhäufigkeit
def zähle_buchstaben(text):
    text = text.lower()
    häufigkeit = {}
    for buchstabe in text:
        if buchstabe.isalpha():  # Nur Buchstaben zählen
            häufigkeit[buchstabe] = häufigkeit.get(buchstabe, 0) + 1
    return häufigkeit

text = "Python ist eine großartige Programmiersprache!"
buchstaben = zähle_buchstaben(text)
print(f"Buchstabenhäufigkeit: {buchstaben}")
"""