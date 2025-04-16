#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Dateien lesen und schreiben in Python
Vergleich mit C++
"""

# ===== Textdateien lesen und schreiben =====
print("=== Textdateien lesen und schreiben ===")

# In C++:
# #include <fstream>
# #include <iostream>
# #include <string>
# 
# // Schreiben
# std::ofstream outfile("beispiel.txt");
# if (outfile.is_open()) {
#     outfile << "Hallo Welt!" << std::endl;
#     outfile << "Dies ist ein Beispiel." << std::endl;
#     outfile.close();
# }
# 
# // Lesen
# std::ifstream infile("beispiel.txt");
# if (infile.is_open()) {
#     std::string line;
#     while (std::getline(infile, line)) {
#         std::cout << line << std::endl;
#     }
#     infile.close();
# }

# In Python:

# Datei schreiben
print("Datei schreiben:")
try:
    # 'w' - Schreiben (überschreibt vorhandene Datei)
    with open('beispiel.txt', 'w', encoding='utf-8') as datei:
        datei.write("Hallo Welt!\n")
        datei.write("Dies ist ein Beispiel.\n")
    print("Datei erfolgreich geschrieben.")
except IOError as e:
    print(f"Fehler beim Schreiben der Datei: {e}")

# Datei lesen
print("\nDatei lesen:")
try:
    # 'r' - Lesen
    with open('beispiel.txt', 'r', encoding='utf-8') as datei:
        inhalt = datei.read()
        print(f"Gesamter Inhalt:\n{inhalt}")
except IOError as e:
    print(f"Fehler beim Lesen der Datei: {e}")

# Zeilenweise lesen
print("\nZeilenweise lesen:")
try:
    with open('beispiel.txt', 'r', encoding='utf-8') as datei:
        for i, zeile in enumerate(datei, 1):
            print(f"Zeile {i}: {zeile.strip()}")
except IOError as e:
    print(f"Fehler beim Lesen der Datei: {e}")

# An Datei anhängen
print("\nAn Datei anhängen:")
try:
    # 'a' - Anhängen (append)
    with open('beispiel.txt', 'a', encoding='utf-8') as datei:
        datei.write("Diese Zeile wurde angehängt.\n")
    print("Zeile erfolgreich angehängt.")
except IOError as e:
    print(f"Fehler beim Anhängen an die Datei: {e}")

# Datei erneut lesen
print("\nDatei nach dem Anhängen lesen:")
try:
    with open('beispiel.txt', 'r', encoding='utf-8') as datei:
        inhalt = datei.read()
        print(f"Aktualisierter Inhalt:\n{inhalt}")
except IOError as e:
    print(f"Fehler beim Lesen der Datei: {e}")
print()

# ===== Verschiedene Dateimodi =====
print("=== Verschiedene Dateimodi ===")

print("Dateimodi in Python:")
print("'r'  - Lesen (Standard)")
print("'w'  - Schreiben (überschreibt vorhandene Datei)")
print("'a'  - Anhängen (append)")
print("'x'  - Exklusives Erstellen (schlägt fehl, wenn die Datei existiert)")
print("'r+' - Lesen und Schreiben")
print("'w+' - Lesen und Schreiben (überschreibt vorhandene Datei)")
print("'a+' - Lesen und Anhängen")
print()

print("Zusätzliche Modi für Binärdateien:")
print("'rb', 'wb', 'ab', 'xb', 'r+b', 'w+b', 'a+b'")
print()

# ===== Binärdateien lesen und schreiben =====
print("=== Binärdateien lesen und schreiben ===")

# In C++:
# #include <fstream>
# #include <vector>
# 
# // Schreiben
# std::vector<int> data = {1, 2, 3, 4, 5};
# std::ofstream outfile("binary.dat", std::ios::binary);
# if (outfile.is_open()) {
#     outfile.write(reinterpret_cast<char*>(data.data()), data.size() * sizeof(int));
#     outfile.close();
# }
# 
# // Lesen
# std::vector<int> read_data(5);
# std::ifstream infile("binary.dat", std::ios::binary);
# if (infile.is_open()) {
#     infile.read(reinterpret_cast<char*>(read_data.data()), read_data.size() * sizeof(int));
#     infile.close();
# }

# In Python:
import struct

# Binärdatei schreiben
print("Binärdatei schreiben:")
try:
    # 'wb' - Binär schreiben
    with open('binary.dat', 'wb') as datei:
        # 5 Integer als binäre Daten schreiben
        # 'i' steht für 4-Byte Integer
        for zahl in [1, 2, 3, 4, 5]:
            datei.write(struct.pack('i', zahl))
    print("Binärdatei erfolgreich geschrieben.")
except IOError as e:
    print(f"Fehler beim Schreiben der Binärdatei: {e}")

# Binärdatei lesen
print("\nBinärdatei lesen:")
try:
    # 'rb' - Binär lesen
    with open('binary.dat', 'rb') as datei:
        zahlen = []
        # 5 Integer aus der Binärdatei lesen
        for _ in range(5):
            binary_data = datei.read(4)  # 4 Bytes für einen Integer
            if binary_data:
                zahl = struct.unpack('i', binary_data)[0]
                zahlen.append(zahl)
        print(f"Gelesene Zahlen: {zahlen}")
except IOError as e:
    print(f"Fehler beim Lesen der Binärdatei: {e}")
print()

# ===== Kontextmanager (with-Statement) =====
print("=== Kontextmanager (with-Statement) ===")

# In C++ wird RAII (Resource Acquisition Is Initialization) verwendet:
# {
#     std::ofstream file("beispiel.txt");
#     // Datei wird automatisch geschlossen, wenn file außer Reichweite geht
# }

# In Python verwenden wir das with-Statement:
print("Vorteile des with-Statements:")
print("1. Automatisches Schließen der Datei, auch bei Ausnahmen")
print("2. Sauberer, lesbarer Code")
print("3. Keine vergessenen close()-Aufrufe")
print()

print("Beispiel ohne with-Statement (nicht empfohlen):")
print("""
try:
    datei = open('beispiel.txt', 'r')
    inhalt = datei.read()
    print(inhalt)
finally:
    datei.close()  # Muss manuell geschlossen werden
""")

print("Beispiel mit with-Statement (empfohlen):")
print("""
with open('beispiel.txt', 'r') as datei:
    inhalt = datei.read()
    print(inhalt)
# Datei wird automatisch geschlossen
""")
print()

# ===== Dateipfade und -operationen =====
print("=== Dateipfade und -operationen ===")

import os
import os.path
import pathlib
import shutil

# os.path - Klassischer Ansatz
print("os.path-Modul:")
print(f"Aktuelles Verzeichnis: {os.getcwd()}")
print(f"Existiert 'beispiel.txt'? {os.path.exists('beispiel.txt')}")
print(f"Ist 'beispiel.txt' eine Datei? {os.path.isfile('beispiel.txt')}")
print(f"Ist '.' ein Verzeichnis? {os.path.isdir('.')}")
print(f"Absoluter Pfad: {os.path.abspath('beispiel.txt')}")
print(f"Dateiname: {os.path.basename('/pfad/zur/datei.txt')}")
print(f"Verzeichnisname: {os.path.dirname('/pfad/zur/datei.txt')}")
print(f"Pfad zusammensetzen: {os.path.join('pfad', 'zur', 'datei.txt')}")

# pathlib - Moderner, objektorientierter Ansatz
print("\npathlib-Modul:")
pfad = pathlib.Path('beispiel.txt')
print(f"Existiert? {pfad.exists()}")
print(f"Ist Datei? {pfad.is_file()}")
print(f"Absoluter Pfad: {pfad.absolute()}")
print(f"Dateiname: {pfad.name}")
print(f"Stammname: {pfad.stem}")
print(f"Erweiterung: {pfad.suffix}")
print(f"Übergeordnetes Verzeichnis: {pfad.parent}")
print(f"Pfad zusammensetzen: {pathlib.Path('pfad') / 'zur' / 'datei.txt'}")
print()

# ===== CSV-Dateien =====
print("=== CSV-Dateien ===")

import csv

# CSV-Datei schreiben
print("CSV-Datei schreiben:")
try:
    with open('personen.csv', 'w', newline='', encoding='utf-8') as csvfile:
        # CSV-Writer erstellen
        writer = csv.writer(csvfile)
        # Kopfzeile schreiben
        writer.writerow(['Name', 'Alter', 'Stadt'])
        # Daten schreiben
        writer.writerow(['Max', 30, 'Berlin'])
        writer.writerow(['Anna', 25, 'Hamburg'])
        writer.writerow(['Tim', 35, 'München'])
    print("CSV-Datei erfolgreich geschrieben.")
except IOError as e:
    print(f"Fehler beim Schreiben der CSV-Datei: {e}")

# CSV-Datei lesen
print("\nCSV-Datei lesen:")
try:
    with open('personen.csv', 'r', newline='', encoding='utf-8') as csvfile:
        # CSV-Reader erstellen
        reader = csv.reader(csvfile)
        # Kopfzeile lesen
        header = next(reader)
        print(f"Spalten: {header}")
        # Daten lesen
        for row in reader:
            print(f"Person: {row[0]}, {row[1]} Jahre, aus {row[2]}")
except IOError as e:
    print(f"Fehler beim Lesen der CSV-Datei: {e}")

# CSV mit Dictionary
print("\nCSV mit Dictionary:")
try:
    with open('personen_dict.csv', 'w', newline='', encoding='utf-8') as csvfile:
        # Spaltennamen definieren
        fieldnames = ['Name', 'Alter', 'Stadt']
        # DictWriter erstellen
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # Kopfzeile schreiben
        writer.writeheader()
        # Daten als Dictionaries schreiben
        writer.writerow({'Name': 'Max', 'Alter': 30, 'Stadt': 'Berlin'})
        writer.writerow({'Name': 'Anna', 'Alter': 25, 'Stadt': 'Hamburg'})
        writer.writerow({'Name': 'Tim', 'Alter': 35, 'Stadt': 'München'})
    print("CSV-Datei mit Dictionary erfolgreich geschrieben.")
except IOError as e:
    print(f"Fehler beim Schreiben der CSV-Datei: {e}")

# CSV mit Dictionary lesen
print("\nCSV mit Dictionary lesen:")
try:
    with open('personen_dict.csv', 'r', newline='', encoding='utf-8') as csvfile:
        # DictReader erstellen
        reader = csv.DictReader(csvfile)
        # Daten lesen
        for row in reader:
            print(f"Person: {row['Name']}, {row['Alter']} Jahre, aus {row['Stadt']}")
except IOError as e:
    print(f"Fehler beim Lesen der CSV-Datei: {e}")
print()

# ===== JSON-Dateien =====
print("=== JSON-Dateien ===")

import json

# JSON-Daten
personen = [
    {
        "name": "Max",
        "alter": 30,
        "stadt": "Berlin",
        "hobbys": ["Programmieren", "Lesen", "Sport"]
    },
    {
        "name": "Anna",
        "alter": 25,
        "stadt": "Hamburg",
        "hobbys": ["Musik", "Reisen", "Kochen"]
    }
]

# JSON-Datei schreiben
print("JSON-Datei schreiben:")
try:
    with open('personen.json', 'w', encoding='utf-8') as jsonfile:
        # JSON-Daten mit Einrückung schreiben
        json.dump(personen, jsonfile, indent=2)
    print("JSON-Datei erfolgreich geschrieben.")
except IOError as e:
    print(f"Fehler beim Schreiben der JSON-Datei: {e}")

# JSON-Datei lesen
print("\nJSON-Datei lesen:")
try:
    with open('personen.json', 'r', encoding='utf-8') as jsonfile:
        # JSON-Daten laden
        geladene_personen = json.load(jsonfile)
        # Daten ausgeben
        for person in geladene_personen:
            print(f"Person: {person['name']}, {person['alter']} Jahre, aus {person['stadt']}")
            print(f"Hobbys: {', '.join(person['hobbys'])}")
except IOError as e:
    print(f"Fehler beim Lesen der JSON-Datei: {e}")

# JSON-String erstellen
print("\nJSON-String erstellen:")
json_string = json.dumps(personen, indent=2)
print(f"JSON-String:\n{json_string}")

# JSON-String parsen
print("\nJSON-String parsen:")
parsed_data = json.loads(json_string)
print(f"Erste Person: {parsed_data[0]['name']}")
print()

# ===== Pickle (Serialisierung) =====
print("=== Pickle (Serialisierung) ===")

import pickle

# In C++ gibt es keine direkte Entsprechung zu Pickle
# Serialisierung muss manuell implementiert werden oder externe Bibliotheken verwenden

# Komplexes Objekt
class Person:
    def __init__(self, name, alter, stadt):
        self.name = name
        self.alter = alter
        self.stadt = stadt
    
    def __str__(self):
        return f"{self.name}, {self.alter} Jahre, aus {self.stadt}"

# Objekte erstellen
personen_objekte = [
    Person("Max", 30, "Berlin"),
    Person("Anna", 25, "Hamburg")
]

# Mit Pickle serialisieren
print("Objekte mit Pickle serialisieren:")
try:
    with open('personen.pickle', 'wb') as pickle_file:
        pickle.dump(personen_objekte, pickle_file)
    print("Objekte erfolgreich serialisiert.")
except IOError as e:
    print(f"Fehler beim Serialisieren: {e}")

# Mit Pickle deserialisieren
print("\nObjekte mit Pickle deserialisieren:")
try:
    with open('personen.pickle', 'rb') as pickle_file:
        geladene_objekte = pickle.load(pickle_file)
        for person in geladene_objekte:
            print(f"Geladene Person: {person}")
except IOError as e:
    print(f"Fehler beim Deserialisieren: {e}")

print("\nWichtige Hinweise zu Pickle:")
print("1. Pickle ist Python-spezifisch und nicht plattformübergreifend")
print("2. Pickle kann sicherheitskritisch sein (niemals Pickle-Daten aus unsicheren Quellen laden)")
print("3. Pickle ist nicht für die langfristige Datenspeicherung geeignet")
print("4. Für den Datenaustausch mit anderen Sprachen besser JSON verwenden")
print()

# ===== Arbeiten mit Verzeichnissen =====
print("=== Arbeiten mit Verzeichnissen ===")

# Verzeichnis erstellen
print("Verzeichnis erstellen:")
try:
    # Einzelnes Verzeichnis
    os.mkdir('testdir')
    print("Verzeichnis 'testdir' erstellt.")
    
    # Verschachtelte Verzeichnisse
    os.makedirs('testdir/subdir1/subdir2', exist_ok=True)
    print("Verschachtelte Verzeichnisse erstellt.")
except OSError as e:
    print(f"Fehler beim Erstellen der Verzeichnisse: {e}")

# Verzeichnisinhalt auflisten
print("\nVerzeichnisinhalt auflisten:")
try:
    print(f"Inhalt von '.': {os.listdir('.')}")
    print(f"Inhalt von 'testdir': {os.listdir('testdir')}")
except OSError as e:
    print(f"Fehler beim Auflisten des Verzeichnisinhalts: {e}")

# Durch Verzeichnisse navigieren
print("\nDurch Verzeichnisse navigieren:")
print(f"Aktuelles Verzeichnis: {os.getcwd()}")
try:
    # In ein Verzeichnis wechseln
    os.chdir('testdir')
    print(f"Neues aktuelles Verzeichnis: {os.getcwd()}")
    
    # Zurück zum ursprünglichen Verzeichnis
    os.chdir('..')
    print(f"Zurück zum ursprünglichen Verzeichnis: {os.getcwd()}")
except OSError as e:
    print(f"Fehler beim Navigieren: {e}")

# Dateien in Verzeichnissen erstellen
print("\nDateien in Verzeichnissen erstellen:")
try:
    with open('testdir/testfile.txt', 'w') as f:
        f.write("Dies ist eine Testdatei.\n")
    print("Datei 'testdir/testfile.txt' erstellt.")
except IOError as e:
    print(f"Fehler beim Erstellen der Datei: {e}")

# Rekursives Durchlaufen von Verzeichnissen
print("\nRekursives Durchlaufen von Verzeichnissen:")
try:
    for root, dirs, files in os.walk('testdir'):
        print(f"Verzeichnis: {root}")
        print(f"  Unterverzeichnisse: {dirs}")
        print(f"  Dateien: {files}")
except OSError as e:
    print(f"Fehler beim Durchlaufen der Verzeichnisse: {e}")

# Verzeichnisse und Dateien löschen
print("\nVerzeichnisse und Dateien löschen:")
try:
    # Datei löschen
    os.remove('testdir/testfile.txt')
    print("Datei 'testdir/testfile.txt' gelöscht.")
    
    # Leeres Verzeichnis löschen
    os.rmdir('testdir/subdir1/subdir2')
    print("Verzeichnis 'testdir/subdir1/subdir2' gelöscht.")
    os.rmdir('testdir/subdir1')
    print("Verzeichnis 'testdir/subdir1' gelöscht.")
    
    # Rekursives Löschen mit shutil
    shutil.rmtree('testdir')
    print("Verzeichnis 'testdir' rekursiv gelöscht.")
except OSError as e:
    print(f"Fehler beim Löschen: {e}")
print()

# ===== ÜBUNG =====
print("=== ÜBUNG ===")
print("1. Schreibe ein Programm, das eine Textdatei einliest und die Anzahl der Wörter, Zeilen und Zeichen zählt")
print("2. Erstelle ein Programm, das ein Verzeichnis durchsucht und alle Dateien nach Typ gruppiert")
print("3. Implementiere eine Funktion, die eine CSV-Datei einliest und die Daten in eine JSON-Datei konvertiert")

# TODO: Schreibe deinen Code hier
# def count_file_stats(filename):
#     ...

# Beispiellösung (auskommentiert)
"""
# 1. Dateistatistik
def count_file_stats(filename):
    # Zählt Wörter, Zeilen und Zeichen in einer Textdatei
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            inhalt = file.read()
            zeilen = inhalt.split('\n')
            wörter = inhalt.split()
            zeichen = len(inhalt)
            
            return {
                'zeilen': len(zeilen),
                'wörter': len(wörter),
                'zeichen': zeichen
            }
    except IOError as e:
        print(f"Fehler beim Lesen der Datei: {e}")
        return None

# Beispielaufruf
# stats = count_file_stats('beispiel.txt')
# if stats:
#     print(f"Statistik für 'beispiel.txt':")
#     print(f"Zeilen: {stats['zeilen']}")
#     print(f"Wörter: {stats['wörter']}")
#     print(f"Zeichen: {stats['zeichen']}")

# 2. Dateien nach Typ gruppieren
def group_files_by_type(directory):
    # Gruppiert Dateien in einem Verzeichnis nach Dateityp
    try:
        file_groups = {}
        
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            
            # Nur Dateien berücksichtigen, keine Verzeichnisse
            if os.path.isfile(filepath):
                # Dateierweiterung ermitteln
                _, extension = os.path.splitext(filename)
                extension = extension.lower()
                
                # Zur entsprechenden Gruppe hinzufügen
                if extension not in file_groups:
                    file_groups[extension] = []
                file_groups[extension].append(filename)
        
        return file_groups
    except OSError as e:
        print(f"Fehler beim Durchsuchen des Verzeichnisses: {e}")
        return None

# Beispielaufruf
# groups = group_files_by_type('.')
# if groups:
#     print("Dateien nach Typ gruppiert:")
#     for ext, files in groups.items():
#         print(f"{ext or 'Ohne Erweiterung'}: {len(files)} Dateien")
#         for file in files[:5]:  # Zeige maximal 5 Dateien pro Gruppe
#             print(f"  - {file}")
#         if len(files) > 5:
#             print(f"  ... und {len(files) - 5} weitere")

# 3. CSV zu JSON konvertieren
def csv_to_json(csv_filename, json_filename):
    # Konvertiert eine CSV-Datei in eine JSON-Datei
    try:
        # CSV-Datei lesen
        with open(csv_filename, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            data = list(reader)
        
        # JSON-Datei schreiben
        with open(json_filename, 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, indent=2)
        
        print(f"Konvertierung von '{csv_filename}' zu '{json_filename}' erfolgreich.")
        return True
    except Exception as e:
        print(f"Fehler bei der Konvertierung: {e}")
        return False

# Beispielaufruf
# csv_to_json('personen.csv', 'personen_converted.json')
"""