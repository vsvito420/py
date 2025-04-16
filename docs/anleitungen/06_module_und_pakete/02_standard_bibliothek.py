#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Python Standard-Bibliothek
Vergleich mit C++
"""

# ===== Überblick über die Standard-Bibliothek =====
print("=== Überblick über die Standard-Bibliothek ===")

print("Python verfügt über eine umfangreiche Standard-Bibliothek, die oft als 'Batteries Included' bezeichnet wird.")
print("Im Gegensatz zu C++ müssen viele Funktionen nicht selbst implementiert werden.")
print("Hier sind einige der wichtigsten Module der Standard-Bibliothek:")
print()

# ===== Mathematische Module =====
print("=== Mathematische Module ===")

# In C++:
# #include <cmath>
# #include <complex>
# #include <random>
# 
# double wurzel = std::sqrt(16.0);
# double sinus = std::sin(M_PI / 2);
# std::complex<double> z(3.0, 4.0);
# double betrag = std::abs(z);

# In Python:
import math
import cmath  # Für komplexe Zahlen
import random
import statistics

# math - Grundlegende mathematische Funktionen
print("math-Modul:")
print(f"Quadratwurzel von 16: {math.sqrt(16)}")
print(f"Sinus von 90°: {math.sin(math.pi/2)}")
print(f"Pi: {math.pi}")
print(f"Euler'sche Zahl e: {math.e}")
print(f"Fakultät von 5: {math.factorial(5)}")
print(f"GGT von 24 und 36: {math.gcd(24, 36)}")

# cmath - Komplexe Zahlen
print("\ncmath-Modul:")
z = complex(3, 4)  # 3 + 4j
print(f"Komplexe Zahl: {z}")
print(f"Betrag: {abs(z)}")
print(f"Quadratwurzel: {cmath.sqrt(z)}")

# random - Zufallszahlen
print("\nrandom-Modul:")
print(f"Zufallszahl zwischen 0 und 1: {random.random()}")
print(f"Zufallszahl zwischen 1 und 10: {random.randint(1, 10)}")
print(f"Zufällige Auswahl: {random.choice(['Apfel', 'Banane', 'Kirsche'])}")
zahlen = [1, 2, 3, 4, 5]
random.shuffle(zahlen)
print(f"Gemischte Liste: {zahlen}")

# statistics - Statistische Funktionen
print("\nstatistics-Modul:")
daten = [2, 4, 4, 4, 5, 5, 7, 9]
print(f"Daten: {daten}")
print(f"Mittelwert: {statistics.mean(daten)}")
print(f"Median: {statistics.median(daten)}")
print(f"Modus: {statistics.mode(daten)}")
print(f"Standardabweichung: {statistics.stdev(daten)}")
print()

# ===== Datei- und Pfadoperationen =====
print("=== Datei- und Pfadoperationen ===")

# In C++:
# #include <fstream>
# #include <filesystem>
# 
# std::ofstream outfile("datei.txt");
# outfile << "Hallo Welt!" << std::endl;
# outfile.close();
# 
# std::ifstream infile("datei.txt");
# std::string line;
# std::getline(infile, line);
# infile.close();
# 
# namespace fs = std::filesystem;
# fs::path p = fs::current_path() / "datei.txt";
# bool exists = fs::exists(p);

# In Python:
import os
import os.path
import pathlib
import shutil
import tempfile

# os und os.path - Betriebssystemfunktionen und Pfadoperationen
print("os und os.path-Module:")
print(f"Aktuelles Verzeichnis: {os.getcwd()}")
print(f"Inhalt des aktuellen Verzeichnisses: {os.listdir('.')}")
print(f"Existiert 'README.md'? {os.path.exists('README.md')}")
print(f"Ist '.' ein Verzeichnis? {os.path.isdir('.')}")
print(f"Dateiname von '/pfad/zur/datei.txt': {os.path.basename('/pfad/zur/datei.txt')}")
print(f"Verzeichnisname von '/pfad/zur/datei.txt': {os.path.dirname('/pfad/zur/datei.txt')}")
print(f"Pfad zusammensetzen: {os.path.join('pfad', 'zur', 'datei.txt')}")

# pathlib - Objektorientierte Pfadoperationen (moderner)
print("\npathlib-Modul:")
p = pathlib.Path('.')
print(f"Aktuelles Verzeichnis: {p.absolute()}")
print(f"Inhalt des aktuellen Verzeichnisses: {list(p.iterdir())}")
datei_pfad = pathlib.Path('/pfad/zur/datei.txt')
print(f"Dateiname: {datei_pfad.name}")
print(f"Stammname: {datei_pfad.stem}")
print(f"Erweiterung: {datei_pfad.suffix}")
print(f"Verzeichnis: {datei_pfad.parent}")
print(f"Pfad zusammensetzen: {p / 'unterverzeichnis' / 'datei.txt'}")

# Dateien lesen und schreiben
print("\nDateioperationen:")
print("Datei schreiben:")
print("""
with open('beispiel.txt', 'w') as f:
    f.write('Hallo Welt!\\n')
    f.write('Dies ist ein Beispiel.\\n')
""")

print("Datei lesen:")
print("""
with open('beispiel.txt', 'r') as f:
    inhalt = f.read()
    print(inhalt)
""")

print("Zeilenweise lesen:")
print("""
with open('beispiel.txt', 'r') as f:
    for zeile in f:
        print(zeile.strip())
""")

# shutil - Erweiterte Dateioperationen
print("\nshutil-Modul:")
print("Datei kopieren: shutil.copy('quelle.txt', 'ziel.txt')")
print("Verzeichnis kopieren: shutil.copytree('quellverzeichnis', 'zielverzeichnis')")
print("Datei verschieben: shutil.move('quelle.txt', 'ziel.txt')")
print("Verzeichnis löschen: shutil.rmtree('verzeichnis')")

# tempfile - Temporäre Dateien und Verzeichnisse
print("\ntempfile-Modul:")
print("Temporäre Datei erstellen: temp = tempfile.NamedTemporaryFile()")
print("Temporäres Verzeichnis erstellen: temp_dir = tempfile.TemporaryDirectory()")
print()

# ===== Datum und Zeit =====
print("=== Datum und Zeit ===")

# In C++:
# #include <chrono>
# #include <ctime>
# 
# auto now = std::chrono::system_clock::now();
# std::time_t now_time = std::chrono::system_clock::to_time_t(now);
# std::cout << "Aktuelle Zeit: " << std::ctime(&now_time);
# 
# auto start = std::chrono::high_resolution_clock::now();
# // Code ausführen
# auto end = std::chrono::high_resolution_clock::now();
# auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
# std::cout << "Dauer: " << duration.count() << " ms" << std::endl;

# In Python:
import time
import datetime
import calendar

# time - Grundlegende Zeitfunktionen
print("time-Modul:")
print(f"Aktuelle Zeit (Sekunden seit Epoch): {time.time()}")
print(f"Aktuelle Zeit (formatiert): {time.ctime()}")
print(f"Aktuelle Zeit (strukturiert): {time.localtime()}")
print(f"Formatierte Zeit: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}")

# Zeitmessung
print("\nZeitmessung:")
print("""
start = time.time()
# Code ausführen
end = time.time()
dauer = end - start
print(f"Dauer: {dauer} Sekunden")
""")

# datetime - Objektorientierte Datum- und Zeitoperationen
print("\ndatetime-Modul:")
jetzt = datetime.datetime.now()
print(f"Aktuelles Datum und Uhrzeit: {jetzt}")
print(f"Jahr: {jetzt.year}, Monat: {jetzt.month}, Tag: {jetzt.day}")
print(f"Stunde: {jetzt.hour}, Minute: {jetzt.minute}, Sekunde: {jetzt.second}")
print(f"Formatiert: {jetzt.strftime('%Y-%m-%d %H:%M:%S')}")

# Datum erstellen
datum = datetime.date(2023, 12, 31)
print(f"Erstelltes Datum: {datum}")

# Zeitdifferenzen
delta = datetime.timedelta(days=7, hours=3)
nächste_woche = jetzt + delta
print(f"In einer Woche und 3 Stunden: {nächste_woche}")

# calendar - Kalenderfunktionen
print("\ncalendar-Modul:")
print(f"Ist 2024 ein Schaltjahr? {calendar.isleap(2024)}")
print("Kalender für März 2023:")
print(calendar.month(2023, 3))
print()

# ===== Datenstrukturen =====
print("=== Datenstrukturen ===")

# In C++:
# #include <vector>
# #include <deque>
# #include <list>
# #include <map>
# #include <set>
# #include <queue>
# #include <stack>
# #include <algorithm>
# 
# std::vector<int> v = {1, 2, 3, 4, 5};
# std::deque<int> d = {1, 2, 3, 4, 5};
# std::map<std::string, int> m = {{"eins", 1}, {"zwei", 2}};
# std::set<int> s = {1, 2, 3, 4, 5};
# std::priority_queue<int> pq;
# std::stack<int> st;

# In Python:
import collections
import heapq
import array
import bisect

# collections - Erweiterte Container-Datentypen
print("collections-Modul:")

# deque - Doppelseitige Warteschlange
deque = collections.deque([1, 2, 3, 4, 5])
print(f"deque: {deque}")
deque.append(6)  # Am Ende hinzufügen
deque.appendleft(0)  # Am Anfang hinzufügen
print(f"Nach append und appendleft: {deque}")
deque.pop()  # Vom Ende entfernen
deque.popleft()  # Vom Anfang entfernen
print(f"Nach pop und popleft: {deque}")

# Counter - Zählt Elemente
counter = collections.Counter(['a', 'b', 'c', 'a', 'b', 'a'])
print(f"Counter: {counter}")
print(f"Häufigste Elemente: {counter.most_common(2)}")

# defaultdict - Dictionary mit Standardwert
default_dict = collections.defaultdict(int)  # Standardwert 0
default_dict['a'] += 1
default_dict['b'] += 2
print(f"defaultdict: {default_dict}")
print(f"Nicht existierender Schlüssel 'c': {default_dict['c']}")  # Gibt 0 zurück

# OrderedDict - Dictionary mit Reihenfolge (in neueren Python-Versionen weniger wichtig)
ordered_dict = collections.OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(f"OrderedDict: {ordered_dict}")

# namedtuple - Benannte Tupel
Person = collections.namedtuple('Person', ['name', 'alter', 'beruf'])
person = Person('Max', 30, 'Entwickler')
print(f"namedtuple: {person}")
print(f"Name: {person.name}, Alter: {person.alter}")

# heapq - Heap-Datenstruktur (Prioritätswarteschlange)
print("\nheapq-Modul:")
heap = [5, 3, 7, 1, 9]
heapq.heapify(heap)  # In-place in einen Heap umwandeln
print(f"Heap: {heap}")
heapq.heappush(heap, 4)  # Element hinzufügen
print(f"Nach heappush: {heap}")
kleinster = heapq.heappop(heap)  # Kleinstes Element entfernen
print(f"Kleinstes Element: {kleinster}")
print(f"Nach heappop: {heap}")

# array - Effiziente Arrays mit einheitlichem Typ
print("\narray-Modul:")
arr = array.array('i', [1, 2, 3, 4, 5])  # 'i' für signed int
print(f"Array: {arr}")
arr.append(6)
print(f"Nach append: {arr}")

# bisect - Binäre Suche und Einfügen in sortierte Listen
print("\nbisect-Modul:")
sortiert = [1, 3, 5, 7, 9]
print(f"Sortierte Liste: {sortiert}")
pos = bisect.bisect(sortiert, 4)  # Position finden
print(f"Position für 4: {pos}")
bisect.insort(sortiert, 4)  # Einfügen an der richtigen Position
print(f"Nach insort: {sortiert}")
print()

# ===== Weitere nützliche Module =====
print("=== Weitere nützliche Module ===")

# In C++:
# #include <regex>
# #include <thread>
# #include <mutex>
# #include <condition_variable>
# #include <future>
# #include <functional>
# #include <algorithm>
# #include <numeric>

# In Python:
import re
import json
import csv
import pickle
import threading
import multiprocessing
import itertools
import functools
import sys
import argparse
import logging

# re - Reguläre Ausdrücke
print("re-Modul:")
text = "Python ist eine großartige Programmiersprache. Python ist einfach zu lernen."
muster = r"Python"
treffer = re.findall(muster, text)
print(f"Treffer: {treffer}")
ersetzt = re.sub(muster, "Java", text)
print(f"Ersetzt: {ersetzt}")

# json - JSON-Verarbeitung
print("\njson-Modul:")
person_dict = {
    "name": "Max",
    "alter": 30,
    "hobbys": ["Programmieren", "Lesen", "Sport"],
    "adresse": {
        "straße": "Hauptstraße 1",
        "stadt": "Berlin"
    }
}
json_str = json.dumps(person_dict, indent=2)
print(f"JSON-String:\n{json_str}")
zurück = json.loads(json_str)
print(f"Zurück zu Dictionary: {zurück['name']}, {zurück['alter']}")

# csv - CSV-Verarbeitung
print("\ncsv-Modul:")
print("""
# CSV-Datei schreiben
with open('personen.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Name', 'Alter', 'Stadt'])
    writer.writerow(['Max', 30, 'Berlin'])
    writer.writerow(['Anna', 25, 'Hamburg'])

# CSV-Datei lesen
with open('personen.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
""")

# pickle - Objekte serialisieren
print("\npickle-Modul:")
print("""
# Objekt serialisieren
with open('daten.pickle', 'wb') as f:
    pickle.dump(person_dict, f)

# Objekt deserialisieren
with open('daten.pickle', 'rb') as f:
    geladen = pickle.load(f)
""")

# threading und multiprocessing - Nebenläufigkeit
print("\nthreading und multiprocessing-Module:")
print("""
# Threading
import threading

def worker(name):
    print(f"Thread {name} startet")
    # Arbeit erledigen
    print(f"Thread {name} beendet")

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
""")

print("""
# Multiprocessing
import multiprocessing

def worker(name):
    print(f"Prozess {name} startet")
    # Arbeit erledigen
    print(f"Prozess {name} beendet")

if __name__ == "__main__":
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
""")

# itertools - Iteratoren für effiziente Schleifen
print("\nitertools-Modul:")
print(f"count: {list(itertools.islice(itertools.count(10, 2), 5))}")  # 10, 12, 14, 16, 18
print(f"cycle: {list(itertools.islice(itertools.cycle('ABC'), 7))}")  # A, B, C, A, B, C, A
print(f"combinations: {list(itertools.combinations('ABC', 2))}")  # ('A', 'B'), ('A', 'C'), ('B', 'C')
print(f"permutations: {list(itertools.permutations('ABC', 2))}")  # Alle Permutationen

# functools - Funktionen höherer Ordnung
print("\nfunctools-Modul:")

@functools.lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(f"fibonacci(10) mit Caching: {fibonacci(10)}")

# Partielle Funktionen
add5 = functools.partial(lambda x, y: x + y, 5)
print(f"add5(10): {add5(10)}")  # 15

# reduce
summe = functools.reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
print(f"reduce-Summe: {summe}")  # 15

# sys - Systemspezifische Parameter und Funktionen
print("\nsys-Modul:")
print(f"Python-Version: {sys.version}")
print(f"Plattform: {sys.platform}")
print(f"Pfad: {sys.path}")
print(f"Kommandozeilenargumente: {sys.argv}")

# argparse - Kommandozeilenargumente parsen
print("\nargparse-Modul:")
print("""
parser = argparse.ArgumentParser(description='Beispielprogramm')
parser.add_argument('--input', help='Eingabedatei')
parser.add_argument('--output', help='Ausgabedatei')
parser.add_argument('--verbose', action='store_true', help='Ausführliche Ausgabe')
args = parser.parse_args()
""")

# logging - Protokollierung
print("\nlogging-Modul:")
print("""
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.debug('Debug-Nachricht')
logging.info('Info-Nachricht')
logging.warning('Warnung')
logging.error('Fehler')
logging.critical('Kritischer Fehler')
""")
print()

# ===== ÜBUNG =====
print("=== ÜBUNG ===")
print("1. Schreibe ein Skript, das eine Textdatei einliest und die Häufigkeit jedes Wortes zählt")
print("2. Erstelle eine Funktion, die das aktuelle Datum in verschiedenen Formaten ausgibt")
print("3. Implementiere einen einfachen Dateimanager, der Dateien kopieren, verschieben und löschen kann")

# TODO: Schreibe deinen Code hier
# def count_words(filename):
#     ...

# Beispiellösung (auskommentiert)
"""
# 1. Worthäufigkeit zählen
def count_words(filename):
    # Zählt die Häufigkeit jedes Wortes in einer Textdatei
    word_count = collections.Counter()
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                # Zeile in Wörter aufteilen und Satzzeichen entfernen
                words = re.findall(r'\b\w+\b', line.lower())
                word_count.update(words)
        
        return word_count
    except FileNotFoundError:
        print(f"Fehler: Die Datei '{filename}' wurde nicht gefunden.")
        return None

# Beispielaufruf
# häufigkeit = count_words('beispiel.txt')
# print("Die 10 häufigsten Wörter:")
# for word, count in häufigkeit.most_common(10):
#     print(f"{word}: {count}")

# 2. Datum in verschiedenen Formaten
def print_date_formats():
    # Aktuelles Datum in verschiedenen Formaten ausgeben
    now = datetime.datetime.now()
    
    formats = {
        "Standard": now.strftime("%Y-%m-%d %H:%M:%S"),
        "Nur Datum": now.strftime("%d.%m.%Y"),
        "Nur Zeit": now.strftime("%H:%M:%S"),
        "Lang": now.strftime("%A, %d. %B %Y"),
        "ISO 8601": now.isoformat(),
        "Unix-Timestamp": str(int(time.time()))
    }
    
    for name, date_format in formats.items():
        print(f"{name}: {date_format}")

# Beispielaufruf
# print_date_formats()

# 3. Einfacher Dateimanager
class SimpleFileManager:
    def __init__(self):
        self.current_dir = os.getcwd()
    
    def list_files(self, directory=None):
        # Dateien im angegebenen Verzeichnis auflisten
        dir_to_list = directory or self.current_dir
        try:
            files = os.listdir(dir_to_list)
            for file in files:
                full_path = os.path.join(dir_to_list, file)
                size = os.path.getsize(full_path)
                mod_time = time.ctime(os.path.getmtime(full_path))
                file_type = "Verzeichnis" if os.path.isdir(full_path) else "Datei"
                print(f"{file} - {file_type}, {size} Bytes, Geändert: {mod_time}")
        except Exception as e:
            print(f"Fehler beim Auflisten der Dateien: {e}")
    
    def copy_file(self, source, destination):
        # Datei kopieren
        try:
            shutil.copy2(source, destination)
            print(f"Datei von '{source}' nach '{destination}' kopiert.")
        except Exception as e:
            print(f"Fehler beim Kopieren der Datei: {e}")
    
    def move_file(self, source, destination):
        # Datei verschieben
        try:
            shutil.move(source, destination)
            print(f"Datei von '{source}' nach '{destination}' verschoben.")
        except Exception as e:
            print(f"Fehler beim Verschieben der Datei: {e}")
    
    def delete_file(self, file_path):
        # Datei oder Verzeichnis löschen
        try:
            if os.path.isdir(file_path):
                shutil.rmtree(file_path)
                print(f"Verzeichnis '{file_path}' gelöscht.")
            else:
                os.remove(file_path)
                print(f"Datei '{file_path}' gelöscht.")
        except Exception as e:
            print(f"Fehler beim Löschen: {e}")
    
    def create_directory(self, directory):
        # Verzeichnis erstellen
        try:
            os.makedirs(directory, exist_ok=True)
            print(f"Verzeichnis '{directory}' erstellt.")
        except Exception as e:
            print(f"Fehler beim Erstellen des Verzeichnisses: {e}")

# Beispielaufruf
# file_manager = SimpleFileManager()
# file_manager.list_files()
# file_manager.create_directory('test_dir')
# with open('test_file.txt', 'w') as f:
#     f.write('Testinhalt')
# file_manager.copy_file('test_file.txt', 'test_dir/test_file_copy.txt')
# file_manager.list_files('test_dir')
# file_manager.move_file('test_file.txt', 'test_dir/test_file_moved.txt')
# file_manager.list_files('test_dir')
# file_manager.delete_file('test_dir')
"""