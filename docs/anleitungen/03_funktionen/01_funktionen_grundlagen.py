#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Grundlagen der Funktionen in Python
Vergleich mit C++
"""

# ===== Einfache Funktionsdefinition =====
print("=== Einfache Funktionsdefinition ===")

# In C++:
# void grüße() {
#     std::cout << "Hallo Welt!" << std::endl;
# }

# In Python:
def grüße():
    """Diese Funktion gibt einen Gruß aus."""
    print("Hallo Welt!")

# Funktionsaufruf
grüße()

# Docstring anzeigen
print(f"Docstring der Funktion: {grüße.__doc__}")
print()

# ===== Funktionen mit Parametern =====
print("=== Funktionen mit Parametern ===")

# In C++:
# void grüße_person(std::string name) {
#     std::cout << "Hallo, " << name << "!" << std::endl;
# }

# In Python:
def grüße_person(name):
    """Diese Funktion begrüßt eine Person mit Namen."""
    print(f"Hallo, {name}!")

# Funktionsaufruf mit Argument
grüße_person("Max")

# In Python müssen wir keine Typen angeben
# Die Funktion kann mit verschiedenen Typen aufgerufen werden
grüße_person(42)  # Funktioniert, aber semantisch nicht sinnvoll
print()

# ===== Funktionen mit Rückgabewerten =====
print("=== Funktionen mit Rückgabewerten ===")

# In C++:
# int addiere(int a, int b) {
#     return a + b;
# }

# In Python:
def addiere(a, b):
    """Addiert zwei Zahlen und gibt das Ergebnis zurück."""
    return a + b

# Funktionsaufruf und Verwendung des Rückgabewerts
ergebnis = addiere(5, 3)
print(f"5 + 3 = {ergebnis}")

# Mehrere Werte zurückgeben
def berechne_statistik(zahlen):
    """Berechnet Minimum, Maximum und Durchschnitt einer Zahlenliste."""
    minimum = min(zahlen)
    maximum = max(zahlen)
    durchschnitt = sum(zahlen) / len(zahlen)
    return minimum, maximum, durchschnitt

# Mehrere Rückgabewerte empfangen
zahlen = [4, 7, 2, 9, 5]
min_wert, max_wert, avg_wert = berechne_statistik(zahlen)
print(f"Zahlen: {zahlen}")
print(f"Minimum: {min_wert}, Maximum: {max_wert}, Durchschnitt: {avg_wert}")

# Alternativ als Tupel empfangen
statistik = berechne_statistik(zahlen)
print(f"Statistik als Tupel: {statistik}")
print(f"Erster Wert (Minimum): {statistik[0]}")
print()

# ===== Funktionen als Objekte =====
print("=== Funktionen als Objekte ===")

# In Python sind Funktionen Objekte erster Klasse
# Sie können Variablen zugewiesen, als Argumente übergeben und
# von anderen Funktionen zurückgegeben werden

# Funktion einer Variablen zuweisen
meine_funktion = grüße_person
meine_funktion("Anna")

# Funktion als Parameter übergeben
def führe_aus(funktion, argument):
    """Führt die übergebene Funktion mit dem Argument aus."""
    print(f"Führe Funktion '{funktion.__name__}' aus:")
    funktion(argument)

führe_aus(grüße_person, "Tim")

# Funktion zurückgeben
def erstelle_multiplizierer(faktor):
    """Erstellt eine Funktion, die mit einem bestimmten Faktor multipliziert."""
    def multiplizierer(x):
        return x * faktor
    return multiplizierer

verdopple = erstelle_multiplizierer(2)
verdreifache = erstelle_multiplizierer(3)

print(f"10 verdoppelt: {verdopple(10)}")
print(f"10 verdreifacht: {verdreifache(10)}")
print()

# ===== Lokale und globale Variablen =====
print("=== Lokale und globale Variablen ===")

# Globale Variable
zähler = 0

def erhöhe_zähler():
    """Erhöht den globalen Zähler."""
    global zähler  # Deklariert zähler als global
    zähler += 1
    print(f"Zähler innerhalb der Funktion: {zähler}")

print(f"Zähler vor Funktionsaufruf: {zähler}")
erhöhe_zähler()
print(f"Zähler nach Funktionsaufruf: {zähler}")

# Lokale Variable mit gleichem Namen wie globale Variable
def lokaler_zähler():
    """Verwendet eine lokale Variable mit gleichem Namen."""
    zähler = 100  # Lokale Variable, überschattet die globale
    zähler += 1
    print(f"Lokaler Zähler: {zähler}")

lokaler_zähler()
print(f"Globaler Zähler unverändert: {zähler}")
print()

# ===== Verschachtelte Funktionen =====
print("=== Verschachtelte Funktionen ===")

def äußere_funktion(x):
    """Eine Funktion, die eine innere Funktion definiert."""
    
    def innere_funktion(y):
        """Eine verschachtelte Funktion."""
        return x + y
    
    # Verwendung der inneren Funktion
    return innere_funktion(5)

print(f"Ergebnis der verschachtelten Funktion: {äußere_funktion(10)}")

# Closures - Innere Funktionen, die Variablen aus dem äußeren Bereich "einfangen"
def erstelle_begrüßung(gruß):
    """Erstellt eine Begrüßungsfunktion mit einem bestimmten Gruß."""
    
    def begrüße(name):
        """Begrüßt eine Person mit dem festgelegten Gruß."""
        return f"{gruß}, {name}!"
    
    return begrüße

hallo_funktion = erstelle_begrüßung("Hallo")
guten_tag_funktion = erstelle_begrüßung("Guten Tag")

print(hallo_funktion("Max"))
print(guten_tag_funktion("Anna"))
print()

# ===== Lambda-Funktionen =====
print("=== Lambda-Funktionen ===")

# In C++:
# auto quadrat = [](int x) { return x * x; };

# In Python:
quadrat = lambda x: x * x
print(f"Quadrat von 5: {quadrat(5)}")

# Lambda-Funktionen in Kombination mit map()
zahlen = [1, 2, 3, 4, 5]
quadrate = list(map(lambda x: x * x, zahlen))
print(f"Quadrate von {zahlen}: {quadrate}")

# Lambda-Funktionen in Kombination mit filter()
gerade_zahlen = list(filter(lambda x: x % 2 == 0, zahlen))
print(f"Gerade Zahlen aus {zahlen}: {gerade_zahlen}")

# Lambda-Funktionen in Kombination mit sorted()
personen = [("Max", 30), ("Anna", 25), ("Tim", 35)]
# Sortieren nach Alter (zweites Element des Tupels)
sortiert_nach_alter = sorted(personen, key=lambda person: person[1])
print(f"Nach Alter sortiert: {sortiert_nach_alter}")
print()

# ===== Funktionsdekoratoren =====
print("=== Funktionsdekoratoren ===")

# Dekoratoren sind eine fortgeschrittene Technik, um das Verhalten
# von Funktionen zu modifizieren, ohne ihren Code zu ändern

def mein_dekorator(funktion):
    """Ein einfacher Dekorator, der vor und nach der Funktion etwas ausgibt."""
    
    def wrapper(*args, **kwargs):
        print("Vor dem Funktionsaufruf")
        ergebnis = funktion(*args, **kwargs)
        print("Nach dem Funktionsaufruf")
        return ergebnis
    
    return wrapper

# Manuelle Anwendung des Dekorators
def sage_hallo():
    """Gibt einen Gruß aus."""
    print("Hallo!")

dekorierte_funktion = mein_dekorator(sage_hallo)
dekorierte_funktion()

# Mit Dekorator-Syntax
@mein_dekorator
def sage_tschüss():
    """Gibt einen Abschiedsgruß aus."""
    print("Tschüss!")

sage_tschüss()
print()

# ===== Typhinweise (Type Hints) =====
print("=== Typhinweise (Type Hints) ===")

# Ab Python 3.5 können Typhinweise verwendet werden
# Sie dienen der Dokumentation und können von Tools wie mypy geprüft werden,
# haben aber keine Auswirkung auf die Laufzeit

def addiere_mit_typen(a: int, b: int) -> int:
    """Addiert zwei Zahlen und gibt das Ergebnis zurück."""
    return a + b

print(f"5 + 3 = {addiere_mit_typen(5, 3)}")

# Typhinweise für komplexere Typen
from typing import List, Dict, Tuple, Optional

def verarbeite_daten(zahlen: List[int], 
                     optionen: Dict[str, bool] = None) -> Tuple[int, float]:
    """Verarbeitet eine Liste von Zahlen mit optionalen Einstellungen."""
    if optionen is None:
        optionen = {"summieren": True, "durchschnitt": True}
    
    summe = sum(zahlen) if optionen.get("summieren", True) else 0
    avg = summe / len(zahlen) if optionen.get("durchschnitt", True) else 0
    
    return summe, avg

zahlen = [1, 2, 3, 4, 5]
summe, durchschnitt = verarbeite_daten(zahlen)
print(f"Summe: {summe}, Durchschnitt: {durchschnitt}")
print()

# ===== ÜBUNG =====
print("=== ÜBUNG ===")
print("1. Schreibe eine Funktion, die prüft, ob eine Zahl eine Primzahl ist")
print("2. Schreibe eine Funktion, die eine Liste von Zahlen als Parameter nimmt und die Summe aller geraden Zahlen zurückgibt")
print("3. Schreibe eine Funktion, die eine andere Funktion als Parameter nimmt und diese dreimal ausführt")

# TODO: Schreibe deinen Code hier
# def ist_primzahl(zahl):
#     ...

# Beispiellösung (auskommentiert)
"""
# 1. Primzahlprüfung
def ist_primzahl(zahl):
    # Prüft, ob eine Zahl eine Primzahl ist.
    if zahl <= 1:
        return False
    if zahl <= 3:
        return True
    if zahl % 2 == 0 or zahl % 3 == 0:
        return False
    i = 5
    while i * i <= zahl:
        if zahl % i == 0 or zahl % (i + 2) == 0:
            return False
        i += 6
    return True

print(f"Ist 7 eine Primzahl? {ist_primzahl(7)}")
print(f"Ist 12 eine Primzahl? {ist_primzahl(12)}")

# 2. Summe gerader Zahlen
def summe_gerader_zahlen(zahlen):
    # Berechnet die Summe aller geraden Zahlen in der Liste.
    return sum(zahl for zahl in zahlen if zahl % 2 == 0)

zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Summe der geraden Zahlen in {zahlen}: {summe_gerader_zahlen(zahlen)}")

# 3. Funktion dreimal ausführen
def dreimal_ausführen(funktion, *args, **kwargs):
    # Führt die übergebene Funktion dreimal aus.
    for _ in range(3):
        funktion(*args, **kwargs)

def sage_name(name):
    # Gibt einen Namen aus.
    print(f"Hallo, {name}!")

dreimal_ausführen(sage_name, "Python")
"""