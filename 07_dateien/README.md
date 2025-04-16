# Dateien in Python

Dieses Modul behandelt den Umgang mit Dateien in Python und vergleicht ihn mit C++.

## Inhaltsübersicht

1. [Lesen und Schreiben](01_lesen_schreiben.py)
   - Textdateien lesen und schreiben
   - Binärdateien lesen und schreiben
   - Kontextmanager (with-Statement)
   - Dateipfade und -operationen
   - CSV-Dateien
   - JSON-Dateien
   - Pickle (Serialisierung)
   - Arbeiten mit Verzeichnissen

## Unterschiede zu C++

Python und C++ haben unterschiedliche Ansätze zum Umgang mit Dateien:

| Konzept | Python | C++ |
|---------|--------|-----|
| Dateiöffnung | `open(dateiname, modus)` | `std::ifstream`, `std::ofstream`, `std::fstream` |
| Lesemodi | `'r'` (Text), `'rb'` (Binär) | `std::ios::in`, `std::ios::binary` |
| Schreibmodi | `'w'`, `'a'`, `'x'` | `std::ios::out`, `std::ios::app`, `std::ios::trunc` |
| Dateioperationen | Methoden des Dateiobjekts | Stream-Operatoren und Methoden |
| Ressourcenverwaltung | `with`-Statement | RAII, Destruktoren |
| Pfadoperationen | `os.path`, `pathlib` | `<filesystem>` (C++17) |
| Serialisierung | `pickle`, `json` | Externe Bibliotheken oder manuelle Implementierung |

## Lernziele

Nach Abschluss dieses Moduls solltest du:

- Textdateien und Binärdateien in Python lesen und schreiben können
- Das `with`-Statement zur sicheren Ressourcenverwaltung verstehen und anwenden können
- Mit verschiedenen Dateiformaten wie CSV und JSON arbeiten können
- Objekte mit Pickle serialisieren und deserialisieren können
- Verzeichnisse erstellen, durchsuchen und manipulieren können
- Die Unterschiede zwischen Python und C++ im Umgang mit Dateien verstehen

## Weiterführende Ressourcen

- [Python Dokumentation zu Dateien](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [Python Dokumentation zu os.path](https://docs.python.org/3/library/os.path.html)
- [Python Dokumentation zu pathlib](https://docs.python.org/3/library/pathlib.html)
- [Python Dokumentation zu csv](https://docs.python.org/3/library/csv.html)
- [Python Dokumentation zu json](https://docs.python.org/3/library/json.html)
- [Python Dokumentation zu pickle](https://docs.python.org/3/library/pickle.html)