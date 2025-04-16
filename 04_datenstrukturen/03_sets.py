#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Sets in Python
Vergleich mit C++
"""

# ===== Grundlagen von Sets =====
print("=== Grundlagen von Sets ===")

# In C++:
# std::set<int> zahlen = {1, 2, 3, 4, 5};
# std::unordered_set<int> zahlen_unordered = {1, 2, 3, 4, 5};

# In Python:
zahlen = {1, 2, 3, 4, 5}
print(f"zahlen: {zahlen}")

# Leeres Set erstellen
# Achtung: {} erstellt ein leeres Dictionary, nicht ein leeres Set!
leeres_set = set()
print(f"Leeres Set: {leeres_set}")

# Set aus einer Liste erstellen
namen_liste = ["Max", "Anna", "Tim", "Max", "Anna"]
namen_set = set(namen_liste)
print(f"Original-Liste: {namen_liste}")
print(f"Set aus Liste: {namen_set}")  # Duplikate werden entfernt

# Sets können nur unveränderbare (hashable) Elemente enthalten
# Erlaubt: Zahlen, Strings, Tupel
gemischt = {1, "Text", 3.14, True, (1, 2)}
print(f"Gemischtes Set: {gemischt}")

# Nicht erlaubt: Listen, Dictionaries, Sets
# Folgendes würde einen Fehler verursachen:
# fehlerhaft = {1, [2, 3]}  # TypeError: unhashable type: 'list'
print()

# ===== Set-Operationen =====
print("=== Set-Operationen ===")

# Element hinzufügen
# In C++: zahlen.insert(6);
zahlen.add(6)
print(f"Nach add(6): {zahlen}")

# Mehrere Elemente hinzufügen
# In C++: zahlen.insert({7, 8, 9});
zahlen.update([7, 8, 9])
print(f"Nach update([7, 8, 9]): {zahlen}")

# Element entfernen
# In C++: zahlen.erase(1);
zahlen.remove(1)  # Wirft einen Fehler, wenn das Element nicht existiert
print(f"Nach remove(1): {zahlen}")

# Element sicher entfernen
# In C++: zahlen.erase(zahlen.find(2));
zahlen.discard(2)  # Kein Fehler, wenn das Element nicht existiert
print(f"Nach discard(2): {zahlen}")

# Ein beliebiges Element entfernen und zurückgeben
element = zahlen.pop()
print(f"Entferntes Element: {element}")
print(f"Nach pop(): {zahlen}")

# Alle Elemente entfernen
zahlen_kopie = zahlen.copy()
zahlen_kopie.clear()
print(f"Nach clear(): {zahlen_kopie}")
print()

# ===== Mengenoperationen =====
print("=== Mengenoperationen ===")

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(f"A: {A}")
print(f"B: {B}")

# Vereinigung (Union)
# In C++: std::set_union()
vereinigung = A | B  # Alternativ: A.union(B)
print(f"A | B (Vereinigung): {vereinigung}")

# Schnittmenge (Intersection)
# In C++: std::set_intersection()
schnittmenge = A & B  # Alternativ: A.intersection(B)
print(f"A & B (Schnittmenge): {schnittmenge}")

# Differenz
# In C++: std::set_difference()
differenz = A - B  # Alternativ: A.difference(B)
print(f"A - B (Differenz): {differenz}")

# Symmetrische Differenz
# In C++: std::set_symmetric_difference()
sym_differenz = A ^ B  # Alternativ: A.symmetric_difference(B)
print(f"A ^ B (Symmetrische Differenz): {sym_differenz}")
print()

# ===== Set-Vergleiche =====
print("=== Set-Vergleiche ===")

C = {1, 2, 3}
D = {1, 2, 3, 4, 5}
print(f"C: {C}")
print(f"D: {D}")

# Teilmenge (Subset)
# In C++: std::includes(D.begin(), D.end(), C.begin(), C.end())
ist_teilmenge = C.issubset(D)  # Alternativ: C <= D
print(f"C ist Teilmenge von D: {ist_teilmenge}")

# Echte Teilmenge
ist_echte_teilmenge = C < D
print(f"C ist echte Teilmenge von D: {ist_echte_teilmenge}")

# Obermenge (Superset)
# In C++: std::includes(C.begin(), C.end(), D.begin(), D.end())
ist_obermenge = D.issuperset(C)  # Alternativ: D >= C
print(f"D ist Obermenge von C: {ist_obermenge}")

# Echte Obermenge
ist_echte_obermenge = D > C
print(f"D ist echte Obermenge von C: {ist_echte_obermenge}")

# Disjunkt (keine gemeinsamen Elemente)
E = {6, 7, 8}
print(f"E: {E}")
sind_disjunkt = C.isdisjoint(E)
print(f"C und E sind disjunkt: {sind_disjunkt}")
print()

# ===== Set Comprehensions =====
print("=== Set Comprehensions ===")

# In C++ nicht direkt möglich

# Einfaches Set mit Quadratzahlen
quadrate = {x**2 for x in range(1, 6)}
print(f"Quadratzahlen: {quadrate}")

# Mit Bedingung
gerade_quadrate = {x**2 for x in range(1, 11) if x % 2 == 0}
print(f"Quadrate gerader Zahlen: {gerade_quadrate}")
print()

# ===== Anwendungsbeispiele =====
print("=== Anwendungsbeispiele ===")

# 1. Duplikate entfernen
liste_mit_duplikaten = [1, 2, 2, 3, 3, 3, 4, 4, 5]
liste_ohne_duplikate = list(set(liste_mit_duplikaten))
print(f"Original: {liste_mit_duplikaten}")
print(f"Ohne Duplikate: {liste_ohne_duplikate}")

# 2. Eindeutige Wörter in einem Text zählen
text = "Python ist eine großartige Programmiersprache. Python ist einfach zu lernen."
wörter = text.lower().replace(".", "").split()
eindeutige_wörter = set(wörter)
print(f"Text: {text}")
print(f"Anzahl eindeutiger Wörter: {len(eindeutige_wörter)}")
print(f"Eindeutige Wörter: {eindeutige_wörter}")

# 3. Gemeinsame Elemente finden
liste1 = [1, 2, 3, 4, 5]
liste2 = [4, 5, 6, 7, 8]
gemeinsame_elemente = set(liste1) & set(liste2)
print(f"Liste 1: {liste1}")
print(f"Liste 2: {liste2}")
print(f"Gemeinsame Elemente: {gemeinsame_elemente}")
print()

# ===== Frozen Sets =====
print("=== Frozen Sets ===")

# Unveränderbare Sets (immutable)
# In C++ gibt es kein direktes Äquivalent

# Erstellen eines Frozen Sets
unveränderbar = frozenset([1, 2, 3, 4, 5])
print(f"Frozen Set: {unveränderbar}")

# Frozen Sets können als Dictionary-Schlüssel oder als Elemente in anderen Sets verwendet werden
set_von_sets = {frozenset([1, 2]), frozenset([3, 4])}
print(f"Set von Frozen Sets: {set_von_sets}")

# Frozen Sets unterstützen die gleichen Mengenoperationen wie normale Sets
anderes_set = frozenset([4, 5, 6])
print(f"Vereinigung: {unveränderbar | anderes_set}")
print(f"Schnittmenge: {unveränderbar & anderes_set}")
print()

# ===== Leistungsvergleich =====
print("=== Leistungsvergleich ===")

# Sets sind effizient für:
# - Prüfen der Mitgliedschaft: O(1) im Durchschnitt
# - Hinzufügen/Entfernen von Elementen: O(1) im Durchschnitt
# - Mengenoperationen: Schneller als manuelle Implementierung mit Listen

# Beispiel: Mitgliedschaftsprüfung in Set vs. Liste
import time

# Große Datenmenge
n = 10000
große_liste = list(range(n))
großes_set = set(range(n))

print("Mitgliedschaftsprüfung in großen Datenstrukturen:")
print("Sets sind viel schneller für Mitgliedschaftsprüfungen als Listen,")
print("besonders bei großen Datenmengen. Für 10.000 Elemente kann der")
print("Unterschied mehrere Größenordnungen betragen.")
print()

# ===== ÜBUNG =====
print("=== ÜBUNG ===")
print("1. Erstelle zwei Sets mit deinen Lieblingssportarten und denen eines Freundes")
print("2. Finde heraus, welche Sportarten ihr beide mögt (Schnittmenge)")
print("3. Finde heraus, welche Sportarten nur du magst (Differenz)")
print("4. Schreibe eine Funktion, die prüft, ob ein Wort ein Anagramm eines anderen Wortes ist (Tipp: Verwende Sets)")

# TODO: Schreibe deinen Code hier
# aufgabe1 = ...

# Beispiellösung (auskommentiert)
"""
# 1. Lieblingssportarten
meine_sportarten = {"Fußball", "Basketball", "Schwimmen", "Radfahren"}
freund_sportarten = {"Fußball", "Tennis", "Volleyball", "Schwimmen"}

print(f"Meine Sportarten: {meine_sportarten}")
print(f"Sportarten meines Freundes: {freund_sportarten}")

# 2. Gemeinsame Sportarten (Schnittmenge)
gemeinsame = meine_sportarten & freund_sportarten
print(f"Gemeinsame Sportarten: {gemeinsame}")

# 3. Nur meine Sportarten (Differenz)
nur_meine = meine_sportarten - freund_sportarten
print(f"Nur meine Sportarten: {nur_meine}")

# 4. Anagramm-Prüfung
def ist_anagramm(wort1, wort2):
    # Entferne Leerzeichen und konvertiere zu Kleinbuchstaben
    wort1 = wort1.lower().replace(" ", "")
    wort2 = wort2.lower().replace(" ", "")
    
    # Prüfe, ob die Buchstabenmengen gleich sind
    return set(wort1) == set(wort2) and len(wort1) == len(wort2)

# Test
print(f"'listen' und 'silent' sind Anagramme: {ist_anagramm('listen', 'silent')}")
print(f"'triangle' und 'integral' sind Anagramme: {ist_anagramm('triangle', 'integral')}")
print(f"'python' und 'typhon' sind Anagramme: {ist_anagramm('python', 'typhon')}")
print(f"'python' und 'java' sind Anagramme: {ist_anagramm('python', 'java')}")
"""