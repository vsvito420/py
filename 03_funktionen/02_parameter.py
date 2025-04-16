#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Verschiedene Arten von Parametern und Argumenten in Python
Vergleich mit C++
"""

# ===== Positionsparameter =====
print("=== Positionsparameter ===")

# In C++:
# void grüße(std::string vorname, std::string nachname) {
#     std::cout << "Hallo, " << vorname << " " << nachname << "!" << std::endl;
# }

# In Python:
def grüße(vorname, nachname):
    """Begrüßt eine Person mit Vor- und Nachnamen."""
    print(f"Hallo, {vorname} {nachname}!")

# Aufruf mit Positionsargumenten
grüße("Max", "Mustermann")
print()

# ===== Default-Parameter =====
print("=== Default-Parameter ===")

# In C++:
# void grüße(std::string name, std::string gruß = "Hallo") {
#     std::cout << gruß << ", " << name << "!" << std::endl;
# }

# In Python:
def grüße_mit_default(name, gruß="Hallo"):
    """Begrüßt eine Person mit einem anpassbaren Gruß."""
    print(f"{gruß}, {name}!")

# Aufruf ohne optionales Argument
grüße_mit_default("Anna")

# Aufruf mit optionalem Argument
grüße_mit_default("Tim", "Guten Tag")

# In Python können Default-Parameter an beliebiger Stelle stehen
def erstelle_person(name, alter=30, stadt="Berlin"):
    """Erstellt ein Dictionary mit Personendaten."""
    return {"name": name, "alter": alter, "stadt": stadt}

# Verschiedene Aufrufe
person1 = erstelle_person("Max")
person2 = erstelle_person("Anna", 25)
person3 = erstelle_person("Tim", 35, "München")

print(f"Person 1: {person1}")
print(f"Person 2: {person2}")
print(f"Person 3: {person3}")
print()

# ===== Schlüsselwortargumente (Keyword Arguments) =====
print("=== Schlüsselwortargumente ===")

# In C++ nicht direkt vorhanden

# In Python:
def beschreibe_person(name, alter, stadt):
    """Beschreibt eine Person mit Name, Alter und Stadt."""
    print(f"{name} ist {alter} Jahre alt und wohnt in {stadt}.")

# Aufruf mit Positionsargumenten
beschreibe_person("Max", 30, "Berlin")

# Aufruf mit Schlüsselwortargumenten
beschreibe_person(name="Anna", alter=25, stadt="München")

# Aufruf mit gemischten Argumenten
# Positionsargumente müssen vor Schlüsselwortargumenten stehen
beschreibe_person("Tim", stadt="Hamburg", alter=35)

# Reihenfolge der Schlüsselwortargumente ist egal
beschreibe_person(stadt="Köln", name="Lisa", alter=28)
print()

# ===== Variable Anzahl von Positionsargumenten (*args) =====
print("=== Variable Anzahl von Positionsargumenten (*args) ===")

# In C++: Funktionsüberladung oder Variadic Templates

# In Python:
def summe(*zahlen):
    """Berechnet die Summe einer variablen Anzahl von Zahlen."""
    ergebnis = 0
    for zahl in zahlen:
        ergebnis += zahl
    return ergebnis

# Aufruf mit verschiedener Anzahl von Argumenten
print(f"Summe von 1, 2: {summe(1, 2)}")
print(f"Summe von 1, 2, 3, 4, 5: {summe(1, 2, 3, 4, 5)}")
print(f"Summe ohne Argumente: {summe()}")

# Kombination mit normalen Parametern
def begrüße_gruppe(gruß, *namen):
    """Begrüßt mehrere Personen mit demselben Gruß."""
    for name in namen:
        print(f"{gruß}, {name}!")

begrüße_gruppe("Hallo", "Max", "Anna", "Tim")
print()

# ===== Variable Anzahl von Schlüsselwortargumenten (**kwargs) =====
print("=== Variable Anzahl von Schlüsselwortargumenten (**kwargs) ===")

# In C++ nicht direkt vorhanden

# In Python:
def erstelle_benutzer(**eigenschaften):
    """Erstellt ein Benutzerprofil mit beliebigen Eigenschaften."""
    print("Benutzerprofil erstellt:")
    for schlüssel, wert in eigenschaften.items():
        print(f"  {schlüssel}: {wert}")

# Aufruf mit verschiedenen Schlüsselwortargumenten
erstelle_benutzer(name="Max", alter=30, beruf="Entwickler", hobby="Programmieren")
erstelle_benutzer(name="Anna", email="anna@example.com")

# Kombination mit normalen Parametern und *args
def komplexe_funktion(param1, param2, *args, **kwargs):
    """Demonstriert die Kombination verschiedener Parametertypen."""
    print(f"Normale Parameter: {param1}, {param2}")
    print(f"Positionsargumente (*args): {args}")
    print(f"Schlüsselwortargumente (**kwargs): {kwargs}")

komplexe_funktion(1, 2, 3, 4, 5, name="Max", alter=30)
print()

# ===== Entpacken von Argumenten =====
print("=== Entpacken von Argumenten ===")

# Liste als Positionsargumente entpacken
def addiere(a, b, c):
    """Addiert drei Zahlen."""
    return a + b + c

zahlen = [1, 2, 3]
print(f"Summe von {zahlen}: {addiere(*zahlen)}")

# Dictionary als Schlüsselwortargumente entpacken
def erstelle_person(name, alter, stadt):
    """Erstellt ein Dictionary mit Personendaten."""
    return {"name": name, "alter": alter, "stadt": stadt}

person_daten = {"name": "Max", "alter": 30, "stadt": "Berlin"}
person = erstelle_person(**person_daten)
print(f"Person: {person}")
print()

# ===== Nur-Positions-Parameter (Python 3.8+) =====
print("=== Nur-Positions-Parameter (Python 3.8+) ===")

# Parameter vor / können nur als Positionsargumente übergeben werden
def nur_position(a, b, /, c, d):
    """a und b sind Nur-Positions-Parameter, c und d können beides sein."""
    print(f"a={a}, b={b}, c={c}, d={d}")

# Gültige Aufrufe
nur_position(1, 2, 3, 4)  # Alle als Position
nur_position(1, 2, c=3, d=4)  # a, b als Position, c, d als Schlüsselwort
nur_position(1, 2, 3, d=4)  # a, b, c als Position, d als Schlüsselwort

# Ungültige Aufrufe (auskommentiert)
# nur_position(a=1, b=2, c=3, d=4)  # Fehler: a, b können nicht als Schlüsselwort übergeben werden
print()

# ===== Nur-Schlüsselwort-Parameter =====
print("=== Nur-Schlüsselwort-Parameter ===")

# Parameter nach * können nur als Schlüsselwortargumente übergeben werden
def nur_schlüsselwort(a, b, *, c, d):
    """c und d sind Nur-Schlüsselwort-Parameter."""
    print(f"a={a}, b={b}, c={c}, d={d}")

# Gültige Aufrufe
nur_schlüsselwort(1, 2, c=3, d=4)  # a, b als Position, c, d als Schlüsselwort
nur_schlüsselwort(a=1, b=2, c=3, d=4)  # Alle als Schlüsselwort

# Ungültige Aufrufe (auskommentiert)
# nur_schlüsselwort(1, 2, 3, 4)  # Fehler: c, d müssen als Schlüsselwort übergeben werden
print()

# ===== Kombination aller Parametertypen =====
print("=== Kombination aller Parametertypen ===")

def komplette_funktion(a, b, /, c, d, *, e, f, **kwargs):
    """
    a, b: Nur-Positions-Parameter
    c, d: Positions- oder Schlüsselwort-Parameter
    e, f: Nur-Schlüsselwort-Parameter
    **kwargs: Variable Anzahl von Schlüsselwortargumenten
    """
    print(f"a={a}, b={b}, c={c}, d={d}, e={e}, f={f}, kwargs={kwargs}")

# Gültiger Aufruf
komplette_funktion(1, 2, 3, d=4, e=5, f=6, extra1=7, extra2=8)
print()

# ===== Typhinweise für Parameter =====
print("=== Typhinweise für Parameter ===")

from typing import List, Dict, Optional, Union, Any

def verarbeite_daten(
    zahlen: List[int],
    name: str,
    aktiv: bool = True,
    optionen: Optional[Dict[str, Any]] = None,
    *args: str,
    **kwargs: Any
) -> Union[int, float]:
    """Demonstriert Typhinweise für verschiedene Parametertypen."""
    print(f"zahlen: {zahlen}, Typ: {type(zahlen)}")
    print(f"name: {name}, Typ: {type(name)}")
    print(f"aktiv: {aktiv}, Typ: {type(aktiv)}")
    print(f"optionen: {optionen}, Typ: {type(optionen)}")
    print(f"args: {args}, Typ: {type(args)}")
    print(f"kwargs: {kwargs}, Typ: {type(kwargs)}")
    
    return sum(zahlen)

ergebnis = verarbeite_daten(
    [1, 2, 3, 4, 5],
    "Test",
    False,
    {"sortieren": True},
    "extra1", "extra2",
    param1=10, param2="Wert"
)
print(f"Ergebnis: {ergebnis}")
print()

# ===== ÜBUNG =====
print("=== ÜBUNG ===")
print("1. Schreibe eine Funktion, die eine beliebige Anzahl von Zahlen multipliziert")
print("2. Schreibe eine Funktion, die einen Namen und optionale Kontaktdaten (Email, Telefon, etc.) entgegennimmt")
print("3. Schreibe eine Funktion mit Nur-Positions- und Nur-Schlüsselwort-Parametern")

# TODO: Schreibe deinen Code hier
# def multipliziere(*zahlen):
#     ...

# Beispiellösung (auskommentiert)
"""
# 1. Multiplikation beliebig vieler Zahlen
def multipliziere(*zahlen):
    # Multipliziert eine beliebige Anzahl von Zahlen
    if not zahlen:
        return 0
    ergebnis = 1
    for zahl in zahlen:
        ergebnis *= zahl
    return ergebnis

print(f"2 * 3 * 4 = {multipliziere(2, 3, 4)}")
print(f"Keine Zahlen: {multipliziere()}")

# 2. Funktion mit optionalen Kontaktdaten
def erstelle_kontakt(name, **kontaktdaten):
    # Erstellt ein Kontaktprofil mit Namen und optionalen Kontaktdaten
    kontakt = {"name": name}
    kontakt.update(kontaktdaten)
    return kontakt

kontakt1 = erstelle_kontakt("Max Mustermann", email="max@example.com", telefon="0123456789")
kontakt2 = erstelle_kontakt("Anna Schmidt", email="anna@example.com")
print(f"Kontakt 1: {kontakt1}")
print(f"Kontakt 2: {kontakt2}")

# 3. Funktion mit Nur-Positions- und Nur-Schlüsselwort-Parametern
def formatiere_adresse(straße, hausnummer, /, stadt, land, *, plz, zusatz=None):
    # straße, hausnummer: Nur-Positions-Parameter
    # stadt, land: Positions- oder Schlüsselwort-Parameter
    # plz, zusatz: Nur-Schlüsselwort-Parameter
    adresse = f"{straße} {hausnummer}, {plz} {stadt}, {land}"
    if zusatz:
        adresse += f" ({zusatz})"
    return adresse

adresse = formatiere_adresse(
    "Hauptstraße", "42",
    "Berlin", "Deutschland",
    plz="10115",
    zusatz="Erdgeschoss"
)
print(f"Formatierte Adresse: {adresse}")
"""