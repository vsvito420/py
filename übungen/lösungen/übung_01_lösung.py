#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Übung 1: Python-Grundlagen (Lösung)
"""

# ===== Aufgabe 1: Variablen und Datentypen =====
# Erstelle Variablen mit verschiedenen Datentypen (int, float, string, boolean)
# und gib sie mit print() aus.

print("=== Aufgabe 1 ===")
# Variablen mit verschiedenen Datentypen
meine_zahl = 42                # Integer
mein_float = 3.14159           # Float
mein_text = "Hallo Python!"    # String
ist_wahr = True                # Boolean

# Ausgabe der Variablen
print(f"Integer: {meine_zahl}")
print(f"Float: {mein_float}")
print(f"String: {mein_text}")
print(f"Boolean: {ist_wahr}")


# ===== Aufgabe 2: Operatoren =====
# Berechne das Ergebnis der folgenden Ausdrücke und gib sie aus:
# a) 7 + 3 * 2
# b) (7 + 3) * 2
# c) 7 / 2 (Fließkomma-Division)
# d) 7 // 2 (Ganzzahl-Division)
# e) 7 % 3 (Modulo/Rest)
# f) 2 ** 3 (Potenz)

print("\n=== Aufgabe 2 ===")
# Berechnung und Ausgabe der Ausdrücke
print(f"7 + 3 * 2 = {7 + 3 * 2}")           # 13 (Punktrechnung vor Strichrechnung)
print(f"(7 + 3) * 2 = {(7 + 3) * 2}")       # 20 (Klammern haben Vorrang)
print(f"7 / 2 = {7 / 2}")                   # 3.5 (Fließkomma-Division)
print(f"7 // 2 = {7 // 2}")                 # 3 (Ganzzahl-Division)
print(f"7 % 3 = {7 % 3}")                   # 1 (Rest der Division)
print(f"2 ** 3 = {2 ** 3}")                 # 8 (2 hoch 3)


# ===== Aufgabe 3: Strings =====
# a) Erstelle einen String mit deinem Namen
# b) Erstelle einen zweiten String mit deinem Alter
# c) Verbinde beide Strings zu einem Satz: "Mein Name ist ... und ich bin ... Jahre alt."
# d) Gib den Satz aus

print("\n=== Aufgabe 3 ===")
# Strings erstellen
name = "Max Mustermann"
alter = "30"

# Strings verbinden
# Variante 1: Konkatenation mit +
satz1 = "Mein Name ist " + name + " und ich bin " + alter + " Jahre alt."
print(satz1)

# Variante 2: f-String (empfohlen)
satz2 = f"Mein Name ist {name} und ich bin {alter} Jahre alt."
print(satz2)


# ===== Aufgabe 4: Eingabe und Ausgabe =====
# a) Frage den Benutzer nach seinem Namen mit input()
# b) Frage den Benutzer nach seinem Geburtsjahr
# c) Berechne das Alter (aktuelles Jahr - Geburtsjahr)
# d) Gib eine personalisierte Begrüßung aus: "Hallo [Name], du bist ungefähr [Alter] Jahre alt."

print("\n=== Aufgabe 4 ===")
# Für diese Lösung verwenden wir feste Werte, da input() interaktiv ist
# In einer echten Anwendung würde man so vorgehen:
# benutzer_name = input("Wie heißt du? ")
# geburtsjahr_str = input("In welchem Jahr wurdest du geboren? ")

# Simulierte Eingaben
benutzer_name = "Anna"
geburtsjahr_str = "1995"

# Typumwandlung und Berechnung
aktuelles_jahr = 2025
geburtsjahr = int(geburtsjahr_str)
alter = aktuelles_jahr - geburtsjahr

# Ausgabe
begrüßung = f"Hallo {benutzer_name}, du bist ungefähr {alter} Jahre alt."
print(begrüßung)


# ===== Aufgabe 5: Typumwandlung =====
# a) Wandle den String "42" in einen Integer um und speichere ihn in einer Variablen
# b) Wandle den Integer 42 in einen Float um und speichere ihn in einer Variablen
# c) Wandle den Float 3.14 in einen String um und speichere ihn in einer Variablen
# d) Gib alle Variablen und ihre Typen aus (mit type())

print("\n=== Aufgabe 5 ===")
# Typumwandlungen
string_zu_int = int("42")
int_zu_float = float(42)
float_zu_string = str(3.14)

# Ausgabe mit Typen
print(f"string_zu_int: {string_zu_int}, Typ: {type(string_zu_int)}")
print(f"int_zu_float: {int_zu_float}, Typ: {type(int_zu_float)}")
print(f"float_zu_string: {float_zu_string}, Typ: {type(float_zu_string)}")


# ===== BONUS-Aufgabe: F-Strings und Formatierung =====
# a) Erstelle einen f-String, der den Wert von pi (3.14159) mit 2 Dezimalstellen ausgibt
# b) Erstelle einen f-String, der eine Zahl mit Tausendertrennzeichen formatiert (z.B. 1,000,000)
# c) Erstelle einen f-String, der eine Zahl als Prozentsatz formatiert (z.B. 0.15 als 15.00%)

print("\n=== BONUS-Aufgabe ===")
# F-Strings mit Formatierung
pi = 3.14159
große_zahl = 1000000
prozent = 0.15

# a) Pi mit 2 Dezimalstellen
pi_formatiert = f"Pi mit 2 Dezimalstellen: {pi:.2f}"
print(pi_formatiert)

# b) Zahl mit Tausendertrennzeichen
große_zahl_formatiert = f"Große Zahl mit Tausendertrennzeichen: {große_zahl:,}"
print(große_zahl_formatiert)

# c) Zahl als Prozentsatz
prozent_formatiert = f"Prozentsatz: {prozent:.2%}"
print(prozent_formatiert)