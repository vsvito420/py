#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ein- und Ausgabe in Python
Vergleich mit C++
"""

# ===== Einfache Ausgabe =====
print("=== Einfache Ausgabe ===")

# print() Funktion
# In C++: std::cout << "Hallo Welt" << std::endl;
print("Hallo Welt")

# Mehrere Werte ausgeben
# In C++: std::cout << "Zahl: " << 42 << ", Text: " << "Python" << std::endl;
print("Zahl:", 42, ", Text:", "Python")

# Zeilenumbruch am Ende unterdrücken
print("Diese Zeile hat keinen Umbruch am Ende...", end=" ")
print("und wird fortgesetzt.")

# Trennzeichen ändern
print("Werte", "mit", "Komma", "getrennt", sep=", ")
print("Werte", "mit", "Bindestrich", "getrennt", sep="-")
print()

# ===== Formatierte Ausgabe =====
print("=== Formatierte Ausgabe ===")

name = "Max"
alter = 30
größe = 1.80

# 1. Alte Methode: % Operator (ähnlich wie printf in C/C++)
print("Name: %s, Alter: %d, Größe: %.2f" % (name, alter, größe))

# 2. str.format() Methode
print("Name: {}, Alter: {}, Größe: {:.2f}".format(name, alter, größe))

# Mit Positionsindizes
print("Reihenfolge ändern: {1}, {0}, {2:.2f}".format(name, alter, größe))

# Mit benannten Parametern
print("Mit Namen: {n}, {a}, {g:.2f}".format(n=name, a=alter, g=größe))

# 3. f-Strings (ab Python 3.6, empfohlen)
print(f"Name: {name}, Alter: {alter}, Größe: {größe:.2f}")

# Ausdrücke in f-Strings
print(f"Nächstes Jahr: {name}, {alter + 1}, {größe:.2f}")
print(f"Quadrat von {alter} ist {alter ** 2}")
print()

# ===== Ausgabe in Dateien =====
print("=== Ausgabe in Dateien ===")

# In C++: std::ofstream file("datei.txt"); file << "Inhalt" << std::endl;
# In Python:
with open("beispiel_ausgabe.txt", "w") as datei:
    datei.write("Erste Zeile\n")
    datei.write("Zweite Zeile\n")
    datei.write(f"Formatierter Text: {name}, {alter}\n")

print("Datei 'beispiel_ausgabe.txt' wurde erstellt.")

# Alternativ mit print()
with open("beispiel_ausgabe2.txt", "w") as datei:
    print("Erste Zeile", file=datei)
    print("Zweite Zeile", file=datei)
    print(f"Formatierter Text: {name}, {alter}", file=datei)

print("Datei 'beispiel_ausgabe2.txt' wurde erstellt.")
print()

# ===== Eingabe =====
print("=== Eingabe ===")

# input() Funktion
# In C++: std::string input; std::cin >> input;
# oder: std::getline(std::cin, input);

print("Bitte gib deinen Namen ein (oder drücke Enter für Standardwert):")
# Kommentiere die nächste Zeile aus, wenn du interaktive Eingabe testen möchtest
# benutzername = input()
# Für dieses Beispiel verwenden wir einen Standardwert
benutzername = "Standardbenutzer"

print(f"Hallo, {benutzername}!")

# Eingabe mit Umwandlung
print("Bitte gib dein Alter ein (oder drücke Enter für Standardwert):")
# Kommentiere die nächste Zeile aus, wenn du interaktive Eingabe testen möchtest
# benutzeralter_str = input()
# Für dieses Beispiel verwenden wir einen Standardwert
benutzeralter_str = "25"

# Fehlerbehandlung bei der Umwandlung
try:
    benutzeralter = int(benutzeralter_str)
    print(f"In 5 Jahren wirst du {benutzeralter + 5} Jahre alt sein.")
except ValueError:
    print("Das war keine gültige Zahl!")
print()

# ===== Formatierung für verschiedene Anwendungsfälle =====
print("=== Formatierung für verschiedene Anwendungsfälle ===")

# Zahlenformatierung
zahl = 12345.6789
print(f"Standardformat: {zahl}")
print(f"2 Dezimalstellen: {zahl:.2f}")
print(f"Mit Tausendertrennzeichen: {zahl:,.2f}")
print(f"Wissenschaftliche Notation: {zahl:.2e}")
print(f"Prozent: {zahl/100:.2%}")

# Ausrichtung und Breite
for i in range(1, 11):
    print(f"Zahl: {i:2d}, Quadrat: {i**2:3d}, Würfel: {i**3:4d}")

# Binär, Oktal, Hexadezimal
zahl = 42
print(f"Dezimal: {zahl:d}")
print(f"Binär: {zahl:b}")
print(f"Oktal: {zahl:o}")
print(f"Hexadezimal: {zahl:x}")
print(f"Hexadezimal (groß): {zahl:X}")
print()

# ===== String-Methoden für Formatierung =====
print("=== String-Methoden für Formatierung ===")

text = "  Python ist eine großartige Programmiersprache  "

# Leerzeichen entfernen
print(f"Original: '{text}'")
print(f"strip(): '{text.strip()}'")
print(f"lstrip(): '{text.lstrip()}'")
print(f"rstrip(): '{text.rstrip()}'")

# Groß-/Kleinschreibung
print(f"upper(): '{text.upper()}'")
print(f"lower(): '{text.lower()}'")
print(f"title(): '{text.title()}'")
print(f"capitalize(): '{text.capitalize()}'")

# Ersetzen
print(f"replace(): '{text.replace('Python', 'C++')}'")

# Teilen
satz = "Python,C++,Java,JavaScript"
print(f"split(','): {satz.split(',')}")
print()

# ===== ÜBUNG =====
print("=== ÜBUNG ===")
print("1. Erstelle einen formatierten Text mit deinem Namen und Alter")
print("2. Schreibe eine Liste von 5 Programmiersprachen in eine Datei")
print("3. Formatiere die Zahl 123.456789 mit 3 Dezimalstellen und Tausendertrennzeichen")

# TODO: Schreibe deinen Code hier
# aufgabe1 = ...

# Beispiellösung (auskommentiert)
"""
# 1. Formatierter Text
mein_name = "Anna"
mein_alter = 28
aufgabe1 = f"Ich heiße {mein_name} und bin {mein_alter} Jahre alt."
print(aufgabe1)

# 2. Liste in Datei schreiben
programmiersprachen = ["Python", "C++", "Java", "JavaScript", "Go"]
with open("programmiersprachen.txt", "w") as datei:
    for sprache in programmiersprachen:
        datei.write(f"{sprache}\n")
print("Datei 'programmiersprachen.txt' wurde erstellt.")

# 3. Zahlenformatierung
zahl = 123.456789
aufgabe3 = f"{zahl:,.3f}"
print(f"Formatierte Zahl: {aufgabe3}")
"""