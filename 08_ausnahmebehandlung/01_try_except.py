#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ausnahmebehandlung in Python
Vergleich mit C++
"""

# ===== Grundlagen der Ausnahmebehandlung =====
print("=== Grundlagen der Ausnahmebehandlung ===")

# In C++:
# #include <iostream>
# #include <stdexcept>
# 
# try {
#     int result = 10 / 0;  // Löst eine Ausnahme aus
#     std::cout << "Ergebnis: " << result << std::endl;
# } catch (const std::exception& e) {
#     std::cerr << "Fehler: " << e.what() << std::endl;
# }

# In Python:
print("Einfaches try-except Beispiel:")
try:
    result = 10 / 0  # Löst eine ZeroDivisionError-Ausnahme aus
    print(f"Ergebnis: {result}")  # Diese Zeile wird nicht ausgeführt
except ZeroDivisionError:
    print("Fehler: Division durch Null")

# Ausnahme mit Fehlermeldung
print("\nAusnahme mit Fehlermeldung:")
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Fehler: {e}")

# Ausnahme ohne spezifischen Typ
print("\nAusnahme ohne spezifischen Typ:")
try:
    result = 10 / 0
except Exception as e:
    print(f"Ein Fehler ist aufgetreten: {e}")
print()

# ===== Verschiedene Ausnahmetypen =====
print("=== Verschiedene Ausnahmetypen ===")

print("Häufige Ausnahmetypen in Python:")
print("- ZeroDivisionError: Division durch Null")
print("- TypeError: Falscher Datentyp")
print("- ValueError: Falscher Wert")
print("- NameError: Unbekannter Variablenname")
print("- IndexError: Index außerhalb des gültigen Bereichs")
print("- KeyError: Schlüssel nicht im Dictionary")
print("- FileNotFoundError: Datei nicht gefunden")
print("- IOError: Ein-/Ausgabefehler")
print("- ImportError: Modul konnte nicht importiert werden")
print("- AttributeError: Attribut nicht gefunden")
print("- SyntaxError: Syntaxfehler im Code")
print("- RuntimeError: Allgemeiner Laufzeitfehler")
print("- Exception: Basisklasse für alle Ausnahmen")

# Beispiele für verschiedene Ausnahmetypen
print("\nBeispiele für verschiedene Ausnahmetypen:")

# TypeError
try:
    result = "10" + 5  # String + Zahl
except TypeError as e:
    print(f"TypeError: {e}")

# ValueError
try:
    number = int("abc")  # Keine gültige Zahl
except ValueError as e:
    print(f"ValueError: {e}")

# IndexError
try:
    my_list = [1, 2, 3]
    element = my_list[10]  # Index außerhalb des Bereichs
except IndexError as e:
    print(f"IndexError: {e}")

# KeyError
try:
    my_dict = {"a": 1, "b": 2}
    value = my_dict["c"]  # Schlüssel nicht vorhanden
except KeyError as e:
    print(f"KeyError: {e}")

# FileNotFoundError
try:
    with open("nicht_vorhanden.txt", "r") as file:
        content = file.read()
except FileNotFoundError as e:
    print(f"FileNotFoundError: {e}")
print()

# ===== Mehrere Except-Blöcke =====
print("=== Mehrere Except-Blöcke ===")

# In C++:
# try {
#     // Code, der Ausnahmen auslösen kann
# } catch (const std::invalid_argument& e) {
#     // Behandlung für invalid_argument
# } catch (const std::runtime_error& e) {
#     // Behandlung für runtime_error
# } catch (const std::exception& e) {
#     // Behandlung für alle anderen Ausnahmen
# }

# In Python:
print("Mehrere except-Blöcke:")
try:
    # Code, der verschiedene Ausnahmen auslösen kann
    user_input = input("Gib eine Zahl ein (oder drücke Enter für einen Fehler): ")
    if not user_input:
        # Absichtlich einen KeyError auslösen
        my_dict = {}
        value = my_dict["key"]
    else:
        # Könnte ValueError oder ZeroDivisionError auslösen
        number = int(user_input)
        result = 10 / number
        print(f"Ergebnis: {result}")
except ValueError:
    print("Fehler: Keine gültige Zahl")
except ZeroDivisionError:
    print("Fehler: Division durch Null")
except KeyError:
    print("Fehler: Schlüssel nicht gefunden")
except Exception as e:
    print(f"Unerwarteter Fehler: {e}")

# Mehrere Ausnahmetypen in einem except-Block
print("\nMehrere Ausnahmetypen in einem except-Block:")
try:
    # Code, der verschiedene Ausnahmen auslösen kann
    number = int(input("Gib eine Zahl ein (oder drücke Enter für einen Fehler): "))
    result = 10 / number
    print(f"Ergebnis: {result}")
except (ValueError, ZeroDivisionError) as e:
    print(f"Fehler bei der Berechnung: {e}")
print()

# ===== Else und Finally =====
print("=== Else und Finally ===")

# In C++:
# try {
#     // Code, der Ausnahmen auslösen kann
# } catch (const std::exception& e) {
#     // Fehlerbehandlung
# }
# // Code, der immer ausgeführt wird (kein direktes Äquivalent zu finally)

# In Python:
print("try-except-else-finally:")
try:
    # Code, der Ausnahmen auslösen kann
    number = int(input("Gib eine Zahl ein (oder drücke Enter für einen Fehler): "))
    result = 10 / number
except (ValueError, ZeroDivisionError) as e:
    # Wird ausgeführt, wenn eine Ausnahme auftritt
    print(f"Fehler: {e}")
else:
    # Wird nur ausgeführt, wenn KEINE Ausnahme auftritt
    print(f"Ergebnis: {result}")
finally:
    # Wird IMMER ausgeführt, unabhängig davon, ob eine Ausnahme auftritt oder nicht
    print("Dieser Code wird immer ausgeführt")

# Beispiel mit Dateioperationen
print("\nBeispiel mit Dateioperationen:")
try:
    file = open("beispiel.txt", "w")
    try:
        file.write("Hallo Welt!\n")
        # Hier könnte ein Fehler auftreten
    finally:
        # Wird immer ausgeführt, um die Datei zu schließen
        file.close()
        print("Datei wurde geschlossen")
except IOError as e:
    print(f"Fehler bei Dateioperationen: {e}")
print()

# ===== Eigene Ausnahmen definieren =====
print("=== Eigene Ausnahmen definieren ===")

# In C++:
# class MyCustomException : public std::exception {
# public:
#     const char* what() const noexcept override {
#         return "Dies ist eine benutzerdefinierte Ausnahme";
#     }
# };
# 
# try {
#     throw MyCustomException();
# } catch (const MyCustomException& e) {
#     std::cerr << e.what() << std::endl;
# }

# In Python:
# Eigene Ausnahmeklasse definieren
class MeineAusnahme(Exception):
    """Eine benutzerdefinierte Ausnahme."""
    
    def __init__(self, message="Dies ist eine benutzerdefinierte Ausnahme", code=None):
        self.message = message
        self.code = code
        super().__init__(self.message)
    
    def __str__(self):
        if self.code:
            return f"{self.message} (Fehlercode: {self.code})"
        return self.message

# Eigene Ausnahme verwenden
print("Eigene Ausnahme verwenden:")
try:
    raise MeineAusnahme("Ein benutzerdefinierter Fehler ist aufgetreten", 42)
except MeineAusnahme as e:
    print(f"Abgefangene Ausnahme: {e}")
    if hasattr(e, 'code'):
        print(f"Fehlercode: {e.code}")

# Ausnahmehierarchie
print("\nAusnahmehierarchie:")
class BerechnungsFehler(Exception):
    """Basisklasse für Berechnungsfehler."""
    pass

class UngültigeEingabe(BerechnungsFehler):
    """Ausnahme für ungültige Eingaben."""
    pass

class NegativeZahl(UngültigeEingabe):
    """Ausnahme für negative Zahlen."""
    pass

# Ausnahmehierarchie verwenden
try:
    zahl = -5
    if zahl < 0:
        raise NegativeZahl("Negative Zahlen sind nicht erlaubt")
except NegativeZahl as e:
    print(f"NegativeZahl: {e}")
except UngültigeEingabe as e:
    print(f"UngültigeEingabe: {e}")
except BerechnungsFehler as e:
    print(f"BerechnungsFehler: {e}")
except Exception as e:
    print(f"Allgemeiner Fehler: {e}")
print()

# ===== Ausnahmen auslösen =====
print("=== Ausnahmen auslösen ===")

# In C++:
# if (value < 0) {
#     throw std::invalid_argument("Wert darf nicht negativ sein");
# }

# In Python:
def quadratwurzel(x):
    """Berechnet die Quadratwurzel einer Zahl."""
    if x < 0:
        raise ValueError("Quadratwurzel von negativen Zahlen nicht definiert")
    return x ** 0.5

# Ausnahme auslösen
print("Ausnahme auslösen:")
try:
    result = quadratwurzel(-4)
    print(f"Ergebnis: {result}")
except ValueError as e:
    print(f"Fehler: {e}")

# assert-Anweisung
print("\nassert-Anweisung:")
try:
    x = -5
    assert x >= 0, "x muss positiv sein"
    print(f"Quadratwurzel von {x}: {x ** 0.5}")
except AssertionError as e:
    print(f"Assertion fehlgeschlagen: {e}")
print()

# ===== Ausnahmen verketten =====
print("=== Ausnahmen verketten ===")

# In C++:
# try {
#     try {
#         // Code, der eine Ausnahme auslöst
#     } catch (const std::exception& e) {
#         // Ausnahme behandeln und eine neue auslösen
#         throw std::runtime_error(std::string("Fehler aufgetreten: ") + e.what());
#     }
# } catch (const std::exception& e) {
#     std::cerr << e.what() << std::endl;
# }

# In Python 3:
print("Ausnahmen verketten mit from:")
try:
    try:
        # Ursprüngliche Ausnahme
        1 / 0
    except ZeroDivisionError as e:
        # Neue Ausnahme mit Verweis auf die ursprüngliche
        raise ValueError("Ungültige Operation") from e
except ValueError as e:
    print(f"Fehler: {e}")
    # Zugriff auf die ursprüngliche Ausnahme
    if e.__cause__:
        print(f"Verursacht durch: {e.__cause__}")

# Implizite Verkettung
print("\nImplizite Verkettung:")
try:
    try:
        # Ursprüngliche Ausnahme
        1 / 0
    except ZeroDivisionError:
        # Neue Ausnahme ohne expliziten Verweis
        raise ValueError("Ungültige Operation")
except ValueError as e:
    print(f"Fehler: {e}")
    # Zugriff auf die implizite Ursache
    if e.__context__:
        print(f"Im Kontext von: {e.__context__}")

# Unterdrücken der Verkettung
print("\nUnterdrücken der Verkettung:")
try:
    try:
        # Ursprüngliche Ausnahme
        1 / 0
    except ZeroDivisionError:
        # Neue Ausnahme ohne Verkettung
        raise ValueError("Ungültige Operation") from None
except ValueError as e:
    print(f"Fehler: {e}")
    if e.__cause__:
        print(f"Verursacht durch: {e.__cause__}")
    if e.__context__:
        print(f"Im Kontext von: {e.__context__}")
print()

# ===== Context Manager und with-Statement =====
print("=== Context Manager und with-Statement ===")

# In C++ gibt es kein direktes Äquivalent zum with-Statement
# RAII (Resource Acquisition Is Initialization) wird verwendet

# In Python:
print("with-Statement für Dateien:")
try:
    with open("beispiel.txt", "w") as file:
        file.write("Hallo Welt!\n")
        # Datei wird automatisch geschlossen, auch bei Ausnahmen
    print("Datei wurde geschrieben und geschlossen")
except IOError as e:
    print(f"Fehler: {e}")

# Eigener Context Manager
print("\nEigener Context Manager:")
class MeinContextManager:
    def __init__(self, name):
        self.name = name
    
    def __enter__(self):
        print(f"{self.name}: __enter__ wird aufgerufen")
        return self  # Rückgabewert wird der Variable nach 'as' zugewiesen
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"{self.name}: __exit__ wird aufgerufen")
        if exc_type:
            print(f"Ausnahme aufgetreten: {exc_val}")
            # True zurückgeben, um die Ausnahme zu unterdrücken
            return True
        return False  # Ausnahme nicht unterdrücken

# Context Manager verwenden
try:
    with MeinContextManager("Test") as cm:
        print("Code innerhalb des with-Blocks")
        # Ausnahme auslösen
        # 1 / 0  # Auskommentiert, um die Ausführung fortzusetzen
    print("Nach dem with-Block")
except ZeroDivisionError:
    print("Diese Nachricht sollte nicht erscheinen, da die Ausnahme unterdrückt wird")

# Context Manager aus contextlib
print("\nContext Manager aus contextlib:")
from contextlib import contextmanager

@contextmanager
def temporäre_datei(name):
    try:
        file = open(name, "w")
        print(f"Datei {name} geöffnet")
        yield file  # Gibt die Ressource zurück
    finally:
        file.close()
        print(f"Datei {name} geschlossen")

# Verwenden des Decorator-basierten Context Managers
try:
    with temporäre_datei("temp.txt") as file:
        file.write("Temporärer Inhalt\n")
        print("In die temporäre Datei geschrieben")
except IOError as e:
    print(f"Fehler: {e}")
print()

# ===== Best Practices =====
print("=== Best Practices ===")

print("1. Spezifische Ausnahmen abfangen:")
print("""
# Gut
try:
    # Code
except ValueError as e:
    # Behandlung für ValueError

# Schlecht
try:
    # Code
except Exception as e:
    # Zu allgemein
""")

print("\n2. Nur erwartete Ausnahmen abfangen:")
print("""
# Gut
try:
    zahl = int(user_input)
except ValueError:
    print("Bitte eine gültige Zahl eingeben")

# Schlecht
try:
    # Viel Code mit verschiedenen möglichen Ausnahmen
except Exception:
    # Zu viel abgefangen
""")

print("\n3. Kurze try-Blöcke verwenden:")
print("""
# Gut
try:
    zahl = int(user_input)
except ValueError:
    zahl = 0

# Schlecht
try:
    # Viele Zeilen Code
    # ...
    zahl = int(user_input)
    # Noch mehr Code
    # ...
except ValueError:
    # Unklar, welcher Teil die Ausnahme ausgelöst hat
""")

print("\n4. Ausnahmen nicht für den Kontrollfluss verwenden:")
print("""
# Gut
if os.path.exists(filename):
    with open(filename) as f:
        # Datei verarbeiten

# Schlecht
try:
    with open(filename) as f:
        # Datei verarbeiten
except FileNotFoundError:
    # Datei existiert nicht
""")

print("\n5. Ausnahmen dokumentieren:")
print("""
def divide(a, b):
    \"\"\"Teilt a durch b.
    
    Args:
        a: Zähler
        b: Nenner
        
    Returns:
        Das Ergebnis der Division
        
    Raises:
        ZeroDivisionError: Wenn b gleich 0 ist
    \"\"\"
    return a / b
""")

print("\n6. Ausnahmen loggen:")
print("""
import logging

try:
    # Code, der Ausnahmen auslösen kann
except Exception as e:
    logging.error(f"Ein Fehler ist aufgetreten: {e}", exc_info=True)
""")

print("\n7. Cleanup-Code in finally-Blöcken:")
print("""
resource = None
try:
    resource = acquire_resource()
    # Resource verwenden
except SomeException:
    # Fehlerbehandlung
finally:
    if resource:
        resource.release()  # Wird immer ausgeführt
""")

print("\n8. with-Statement für Ressourcenverwaltung:")
print("""
# Gut
with open("datei.txt") as f:
    data = f.read()

# Schlecht
f = open("datei.txt")
try:
    data = f.read()
finally:
    f.close()
""")
print()

# ===== ÜBUNG =====
print("=== ÜBUNG ===")
print("1. Schreibe eine Funktion, die eine Zahl vom Benutzer einliest und sicherstellt, dass eine gültige Zahl eingegeben wird")
print("2. Erstelle eine eigene Ausnahmeklasse für ungültige Eingaben und verwende sie in einer Funktion")
print("3. Implementiere einen Context Manager für eine einfache Datenbank-Verbindung (simuliert)")

# TODO: Schreibe deinen Code hier
# def get_number_from_user():
#     ...

# Beispiellösung (auskommentiert)
"""
# 1. Sichere Eingabe einer Zahl
def get_number_from_user():
    # Liest eine Zahl vom Benutzer ein und stellt sicher, dass eine gültige Zahl eingegeben wird
    while True:
        try:
            user_input = input("Bitte gib eine Zahl ein: ")
            number = float(user_input)
            return number
        except ValueError:
            print("Das ist keine gültige Zahl. Bitte versuche es erneut.")
        except KeyboardInterrupt:
            print("\nEingabe abgebrochen.")
            return None

# Beispielaufruf
# number = get_number_from_user()
# if number is not None:
#     print(f"Eingegebene Zahl: {number}")

# 2. Eigene Ausnahmeklasse
class UngültigeEingabeError(Exception):
    # Ausnahme für ungültige Benutzereingaben.
    
    def __init__(self, message="Ungültige Eingabe", wert=None):
        self.message = message
        self.wert = wert
        super().__init__(self.message)
    
    def __str__(self):
        if self.wert:
            return f"{self.message}: {self.wert}"
        return self.message

def validate_age(age):
    # Überprüft, ob das Alter gültig ist.
    if not isinstance(age, (int, float)):
        raise UngültigeEingabeError("Alter muss eine Zahl sein", age)
    
    if age < 0:
        raise UngültigeEingabeError("Alter kann nicht negativ sein", age)
    
    if age > 150:
        raise UngültigeEingabeError("Alter scheint unrealistisch hoch zu sein", age)
    
    return age

# Beispielaufruf
# try:
#     alter = validate_age(200)
#     print(f"Gültiges Alter: {alter}")
# except UngültigeEingabeError as e:
#     print(f"Fehler: {e}")

# 3. Context Manager für Datenbankverbindung
class DatabaseConnection:
    # Simulierter Context Manager für eine Datenbankverbindung.
    
    def __init__(self, db_name):
        self.db_name = db_name
        self.connected = False
    
    def __enter__(self):
        # Verbindung herstellen
        print(f"Verbindung zur Datenbank '{self.db_name}' wird hergestellt...")
        self.connected = True
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # Verbindung schließen
        if self.connected:
            print(f"Verbindung zur Datenbank '{self.db_name}' wird geschlossen...")
            self.connected = False
        
        if exc_type:
            print(f"Fehler während der Datenbankoperation: {exc_val}")
            # Fehler nicht unterdrücken
            return False
        
        return True
    
    def execute_query(self, query):
        # Führt eine Abfrage aus.
        if not self.connected:
            raise RuntimeError("Keine Verbindung zur Datenbank")
        
        print(f"Ausführen der Abfrage: {query}")
        
        # Hier würde die eigentliche Abfrage ausgeführt werden
        if "error" in query.lower():
            raise ValueError("Fehlerhafte Abfrage")
        
        return ["Ergebnis 1", "Ergebnis 2", "Ergebnis 3"]

# Beispielaufruf
# try:
#     with DatabaseConnection("meine_db") as db:
#         results = db.execute_query("SELECT * FROM users")
#         print(f"Ergebnisse: {results}")
#         
#         # Fehlerhafte Abfrage
#         # results = db.execute_query("SELECT * FROM error_table")
# except ValueError as e:
#     print(f"Datenbankfehler: {e}")
"""