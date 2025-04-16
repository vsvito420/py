# Modul 4: Datenstrukturen

In diesem Modul lernst du die wichtigsten Datenstrukturen in Python kennen und wie sie sich von C++ unterscheiden.

## Lernziele

- Listen verstehen und effektiv nutzen
- Dictionaries (assoziative Arrays) für Key-Value-Paare einsetzen
- Sets für Mengenoperationen verwenden
- Tuples als unveränderliche Sequenzen nutzen
- Die richtige Datenstruktur für verschiedene Anwendungsfälle auswählen
- Unterschiede zu C++ erkennen

## Dateien in diesem Modul

1. `01_listen.py` - Listen und ihre Methoden
2. `02_dictionaries.py` - Dictionaries und ihre Anwendungen
3. `03_sets.py` - Sets und Mengenoperationen
4. `04_tuples.py` - Tuples und ihre Besonderheiten

## Wichtige Unterschiede zu C++

| C++ | Python | Beispiel Python |
|-----|--------|----------------|
| `std::vector<int> v` | `list = []` | `zahlen = [1, 2, 3]` |
| `std::map<std::string, int> m` | `dict = {}` | `personen = {"Max": 30}` |
| `std::set<int> s` | `set = set()` | `menge = {1, 2, 3}` |
| `std::tuple<int, std::string> t` | `tuple = ()` | `person = (30, "Max")` |
| Homogene Container | Heterogene Container | `mix = [1, "text", True]` |
| Explizite Speicherverwaltung | Automatische Speicherverwaltung | Kein `delete` oder `free()` nötig |
| Statische Typisierung | Dynamische Typisierung | Keine Typdeklaration nötig |

## Übungen

Nach dem Durcharbeiten der Beispiele solltest du die Übungen im Ordner `übungen` lösen:
- `übung_04.py` - Datenstrukturen und ihre Anwendungen