#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Datentypen in Python
Vergleich mit C++
"""

# ===== Numerische Datentypen =====
print("=== Numerische Datentypen ===")

# Integer (Ganzzahlen)
# In C++: int, short, long, long long
# In Python: unbegrenzte Größe!
a = 42
b = 1000000000000000000000000  # In C++ würde das einen Überlauf verursachen
print(f"Integer a: {a}")
print(f"Großer Integer b: {b}")

# Float (Gleitkommazahlen)
# In C++: float, double
# In Python: entspricht meist double in C++
c = 3.14159
d = 2.5e10  # Wissenschaftliche Notation: 2.5 * 10^10
print(f"Float c: {c}")
print(f"Float mit wissenschaftlicher Notation d: {d}")

# Complex (komplexe Zahlen)
# In C++: benötigt spezielle Bibliothek
# In Python: eingebauter Typ
e = 1 + 2j  # j ist die imaginäre Einheit
print(f"Komplexe Zahl e: {e}")
print(f"Realteil: {e.real}, Imaginärteil: {e.imag}")
print()

# ===== Sequenzen =====
print("=== Sequenzen ===")

# String (Zeichenkette)
# In C++: char[], std::string
# In Python: str (Unicode-Unterstützung)
text1 = "Hallo"
text2 = 'Welt'  # Einfache oder doppelte Anführungszeichen
text3 = """Mehrzeiliger
Text mit
mehreren Zeilen"""  # Dreifache Anführungszeichen für mehrzeilige Strings

print(f"text1: {text1}")
print(f"text2: {text2}")
print(f"text3: {text3}")

# String-Operationen
print(f"Konkatenation: {text1 + ' ' + text2}")
print(f"Wiederholung: {text1 * 3}")
print(f"Länge: {len(text1)}")
print(f"Indexierung: {text1[1]}")  # Zweites Zeichen (Index 1)
print(f"Slicing: {text1[1:4]}")    # Zeichen von Index 1 bis 3

# Listen (veränderbar)
# In C++: std::vector, std::array
# In Python: list
liste = [1, 2, 3, 4, 5]
gemischte_liste = [1, "Text", 3.14, True]  # Verschiedene Typen möglich!

print(f"liste: {liste}")
print(f"gemischte_liste: {gemischte_liste}")
print(f"Indexierung: {liste[0]}")  # Erstes Element (Index 0)
print(f"Slicing: {liste[1:3]}")    # Elemente von Index 1 bis 2

# Listen verändern
liste.append(6)        # Element hinzufügen
liste.insert(0, 0)     # Element an Position einfügen
liste.remove(3)        # Element mit Wert 3 entfernen
popped = liste.pop()   # Letztes Element entfernen und zurückgeben
print(f"Veränderte liste: {liste}")
print(f"Entferntes Element: {popped}")

# Tupel (unveränderbar)
# In C++: std::tuple, aber weniger häufig verwendet
# In Python: tuple
tupel = (1, 2, 3, 4, 5)
einzelwert_tupel = (42,)  # Komma wichtig bei Einzelwert-Tupeln!

print(f"tupel: {tupel}")
print(f"einzelwert_tupel: {einzelwert_tupel}")
print(f"Indexierung: {tupel[0]}")
print(f"Slicing: {tupel[1:3]}")

# Versuch, Tupel zu ändern führt zu Fehler
# tupel[0] = 99  # TypeError: 'tuple' object does not support item assignment
print()

# ===== Mapping-Typen =====
print("=== Mapping-Typen ===")

# Dictionary (Key-Value-Paare)
# In C++: std::map, std::unordered_map
# In Python: dict
wörterbuch = {
    "eins": 1,
    "zwei": 2,
    "drei": 3
}

print(f"wörterbuch: {wörterbuch}")
print(f"Wert für 'zwei': {wörterbuch['zwei']}")

# Dictionary verändern
wörterbuch["vier"] = 4  # Neues Key-Value-Paar hinzufügen
wörterbuch["eins"] = "one"  # Wert ändern
print(f"Verändertes wörterbuch: {wörterbuch}")
print(f"Keys: {list(wörterbuch.keys())}")
print(f"Values: {list(wörterbuch.values())}")
print(f"Items: {list(wörterbuch.items())}")
print()

# ===== Set-Typen =====
print("=== Set-Typen ===")

# Set (ungeordnete Sammlung eindeutiger Elemente)
# In C++: std::set, std::unordered_set
# In Python: set
menge = {1, 2, 3, 4, 5}
menge_mit_duplikaten = {1, 2, 2, 3, 3, 3}  # Duplikate werden entfernt

print(f"menge: {menge}")
print(f"menge_mit_duplikaten: {menge_mit_duplikaten}")

# Set-Operationen
menge1 = {1, 2, 3, 4}
menge2 = {3, 4, 5, 6}
print(f"menge1: {menge1}")
print(f"menge2: {menge2}")
print(f"Vereinigung: {menge1 | menge2}")
print(f"Schnittmenge: {menge1 & menge2}")
print(f"Differenz: {menge1 - menge2}")
print(f"Symmetrische Differenz: {menge1 ^ menge2}")
print()

# ===== Boolesche Werte =====
print("=== Boolesche Werte ===")

# Boolean
# In C++: bool (true, false)
# In Python: bool (True, False)
wahr = True
falsch = False

print(f"wahr: {wahr}")
print(f"falsch: {falsch}")
print(f"not wahr: {not wahr}")
print(f"wahr and falsch: {wahr and falsch}")
print(f"wahr or falsch: {wahr or falsch}")
print()

# ===== None-Typ =====
print("=== None-Typ ===")

# None (Null-Wert)
# In C++: nullptr, NULL
# In Python: None
nichts = None

print(f"nichts: {nichts}")
print(f"Ist nichts None? {nichts is None}")
print()

# ===== Typüberprüfung =====
print("=== Typüberprüfung ===")

# isinstance() und type()
print(f"isinstance(42, int): {isinstance(42, int)}")
print(f"isinstance('Text', str): {isinstance('Text', str)}")
print(f"type(3.14) == float: {type(3.14) == float}")
print()

# ===== Typannotationen (Type Hints) =====
print("=== Typannotationen (Type Hints) ===")

# In C++: Typen sind obligatorisch
# int zahl = 42;
# std::string text = "Hallo";

# In Python: Typen sind optional, aber können mit Annotationen angegeben werden
from typing import List, Dict, Tuple, Set, Optional, Union, Any

# Einfache Typannotationen
name: str = "Max"
alter: int = 30
größe: float = 1.80
ist_aktiv: bool = True

print(f"name: {name} (Typ: {type(name).__name__})")
print(f"alter: {alter} (Typ: {type(alter).__name__})")
print(f"größe: {größe} (Typ: {type(größe).__name__})")
print(f"ist_aktiv: {ist_aktiv} (Typ: {type(ist_aktiv).__name__})")

# Komplexere Typannotationen
zahlen_liste: List[int] = [1, 2, 3, 4, 5]
namen_tuple: Tuple[str, str, str] = ("Max", "Anna", "Tim")
personen_dict: Dict[str, int] = {"Max": 30, "Anna": 25, "Tim": 35}
zahlen_set: Set[int] = {1, 2, 3, 4, 5}

print(f"zahlen_liste: {zahlen_liste} (Typ: List[int])")
print(f"namen_tuple: {namen_tuple} (Typ: Tuple[str, str, str])")
print(f"personen_dict: {personen_dict} (Typ: Dict[str, int])")
print(f"zahlen_set: {zahlen_set} (Typ: Set[int])")

# Optional und Union
optional_wert: Optional[str] = None  # Kann str oder None sein
union_wert: Union[int, str] = "Hallo"  # Kann int oder str sein

print(f"optional_wert: {optional_wert} (Typ: Optional[str])")
print(f"union_wert: {union_wert} (Typ: Union[int, str])")

# Typannotationen in Funktionen
def grüße(name: str) -> str:
    """Gibt einen Gruß zurück."""
    return f"Hallo, {name}!"

def addiere(a: int, b: int) -> int:
    """Addiert zwei Zahlen."""
    return a + b

print(f"grüße('Max'): {grüße('Max')}")
print(f"addiere(5, 3): {addiere(5, 3)}")

# Wichtig: Typannotationen sind nur Hinweise!
# Python überprüft die Typen nicht zur Laufzeit
text_als_zahl: int = "Dies ist kein Integer"  # Funktioniert trotz falscher Annotation
print(f"text_als_zahl: {text_als_zahl} (Deklariert als int, ist aber {type(text_als_zahl).__name__})")

# Typannotationen werden verwendet für:
# 1. Dokumentation (bessere Lesbarkeit)
# 2. IDE-Unterstützung (Autovervollständigung, Fehlerprüfung)
# 3. Statische Typprüfung mit Tools wie mypy

print("Hinweis: Für fortgeschrittene Typannotationen siehe auch 03_funktionen/02_parameter.py")
print()

# ===== ÜBUNG =====
print("=== ÜBUNG ===")
print("1. Erstelle eine Liste mit verschiedenen Datentypen")
print("2. Erstelle ein Dictionary mit mindestens 3 Einträgen")
print("3. Führe Set-Operationen mit eigenen Mengen durch")
print("4. Definiere eine Funktion mit Typannotationen")

# TODO: Schreibe deinen Code hier
# meine_liste = ...

# Beispiellösung (auskommentiert)
"""
# 1. Liste mit verschiedenen Datentypen
meine_liste = [42, "Python", 3.14, True, [1, 2, 3], {"name": "Max"}]
print(f"Meine Liste: {meine_liste}")

# 2. Dictionary mit 3 Einträgen
mein_dict = {
    "name": "Anna",
    "alter": 25,
    "hobbies": ["Programmieren", "Lesen", "Sport"]
}
print(f"Mein Dictionary: {mein_dict}")

# 3. Set-Operationen
set_a = {1, 3, 5, 7, 9}
set_b = {2, 3, 5, 7, 11}
print(f"Vereinigung: {set_a | set_b}")
print(f"Schnittmenge: {set_a & set_b}")
print(f"Nur in set_a: {set_a - set_b}")
"""