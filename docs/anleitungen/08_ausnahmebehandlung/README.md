# Modul 8: Ausnahmebehandlung in Python

[&larr; Modul 7: Dateien](../07_dateien/README.md) | [Zurück zur Übersicht](../README.md) | [Modul 9: Projekte &rarr;](../09_projekte/README.md)

Dieses Modul behandelt die Ausnahmebehandlung (Exception Handling) in Python und vergleicht sie mit C++.

## Inhaltsübersicht

1. [Try-Except](01_try_except.py)
   - Grundlagen der Ausnahmebehandlung
   - Verschiedene Ausnahmetypen
   - Mehrere Except-Blöcke
   - Else und Finally
   - Eigene Ausnahmen definieren
   - Ausnahmen auslösen
   - Ausnahmen verketten
   - Context Manager und with-Statement
   - Best Practices

## Unterschiede zu C++

Python und C++ haben unterschiedliche Ansätze zur Ausnahmebehandlung:

| Konzept | Python | C++ |
|---------|--------|-----|
| Syntax | `try`/`except`/`else`/`finally` | `try`/`catch`/`throw` |
| Ausnahmetypen | Klassen, die von `Exception` erben | Beliebige Typen (oft Klassen, die von `std::exception` erben) |
| Ressourcenverwaltung | `with`-Statement | RAII (Resource Acquisition Is Initialization) |
| Spezifizierung | Keine Deklaration der geworfenen Ausnahmen | Früher `throw()`-Spezifikation, jetzt `noexcept` |
| Standardausnahmen | Umfangreiche Hierarchie | Begrenzte Hierarchie in `<stdexcept>` |
| Performance | Langsamer (nicht für Kontrollfluss) | Schneller, aber immer noch teuer |

## Lernziele

Nach Abschluss dieses Moduls solltest du:

- Ausnahmen in Python korrekt abfangen und behandeln können
- Die verschiedenen Ausnahmetypen in Python kennen
- Eigene Ausnahmen definieren können
- Die Unterschiede zwischen Python und C++ in Bezug auf Ausnahmebehandlung verstehen
- Best Practices für die Ausnahmebehandlung anwenden können

## Übungen

Nach dem Durcharbeiten der Beispiele solltest du die Übungen im Ordner `übungen` lösen:
- [übung_07.py](../übungen/übung_07.py) - Ausnahmebehandlung und Dateien

## Weiterführende Themen

- [Dateien](../07_dateien/01_lesen_schreiben.py) - Fehlerbehandlung bei Dateioperationen
- [Objektorientierung](../05_objektorientierung/02_vererbung.py) - Eigene Ausnahmeklassen definieren
- [Projekte](../09_projekte/README.md) - Robuste Fehlerbehandlung in größeren Anwendungen

## Weiterführende Ressourcen

- [Python Dokumentation zu Ausnahmen](https://docs.python.org/3/tutorial/errors.html)
- [Python Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)
- [Python with-Statement und Context Manager](https://docs.python.org/3/reference/compound_stmts.html#with)

---

[&larr; Modul 7: Dateien](../07_dateien/README.md) | [Zurück zur Übersicht](../README.md) | [Modul 9: Projekte &rarr;](../09_projekte/README.md)