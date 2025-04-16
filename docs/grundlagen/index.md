---
layout: default
title: Python Grundlagen
---

# Python Grundlagen

In diesem Modul lernst du die grundlegenden Konzepte der Python-Programmierung kennen:
Variablen, Datentypen, Operatoren und Ein-/Ausgabe.

## Inhaltsverzeichnis

- [Variablen](#variablen)
- [Datentypen](#datentypen)
- [Operatoren](#operatoren)
- [Ein- und Ausgabe](#ein-und-ausgabe)

## Variablen

In Python werden Variablen ohne explizite Typdeklaration erstellt. 
Der Typ einer Variablen wird automatisch anhand des zugewiesenen Wertes bestimmt.

### Vergleich mit C++

In C++ müssen Variablen mit einem Typ deklariert werden:

```cpp
int zahl = 42;
string name = "C++";
bool istWahr = true;
```

In Python entfällt die Typdeklaration:

<div class="pyscript-example">
<pre><code class="language-python">
# Variablen verschiedener Typen
zahl = 42
name = "Python"
ist_wahr = True

# Ausgabe der Variablen
print(f"zahl: {zahl}, Typ: {type(zahl)}")
print(f"name: {name}, Typ: {type(name)}")
print(f"ist_wahr: {ist_wahr}, Typ: {type(ist_wahr)}")

# Variablen können ihren Typ ändern
zahl = "Jetzt bin ich ein String"
print(f"zahl nach Änderung: {zahl}, Typ: {type(zahl)}")

# Mehrfachzuweisung
a, b, c = 1, 2, 3
print(f"a: {a}, b: {b}, c: {c}")
</code></pre>
</div>

> **Hinweis:** Python-Variablen sind dynamisch typisiert, d.h. der Typ kann sich während der Laufzeit ändern.
> Dies bietet Flexibilität, erfordert aber auch Sorgfalt, um unerwartete Typänderungen zu vermeiden.

### Übung: Variablen

Erstelle eigene Variablen verschiedener Typen und experimentiere mit Typänderungen:

<div class="pyscript-exercise">
<pre><code class="language-python">
# TODO: Erstelle eigene Variablen und gib sie aus
# Beispiel:
# meine_zahl = 100
# print(f"Meine Zahl: {meine_zahl}")

</code></pre>
</div>

## Datentypen

Python hat verschiedene eingebaute Datentypen. Die wichtigsten sind:

- **Numerische Typen**: int, float, complex
- **Sequenztypen**: str, list, tuple
- **Mapping-Typ**: dict
- **Set-Typen**: set, frozenset
- **Boolesche Typen**: bool
- **None-Typ**: NoneType

### Beispiel: Numerische Datentypen

<div class="pyscript-example">
<pre><code class="language-python">
# Integer (Ganzzahl)
ganzzahl = 42
print(f"ganzzahl: {ganzzahl}, Typ: {type(ganzzahl)}")

# Float (Fließkommazahl)
fliesskomma = 3.14
print(f"fliesskomma: {fliesskomma}, Typ: {type(fliesskomma)}")

# Complex (Komplexe Zahl)
komplex_zahl = 1 + 2j
print(f"komplex_zahl: {komplex_zahl}, Typ: {type(komplex_zahl)}")
print(f"Realteil: {komplex_zahl.real}, Imaginärteil: {komplex_zahl.imag}")
</code></pre>
</div>

### Beispiel: Sequenz- und Container-Typen

<div class="pyscript-example">
<pre><code class="language-python">
# String (Zeichenkette)
text = "Hallo Python"
print(f"text: {text}, Typ: {type(text)}")

# List (Liste)
liste = [1, 2, 3, "vier", 5.0]
print(f"liste: {liste}, Typ: {type(liste)}")

# Tuple (Tupel) - unveränderlich
tupel = (1, 2, 3, "vier", 5.0)
print(f"tupel: {tupel}, Typ: {type(tupel)}")

# Dictionary (Wörterbuch)
woerterbuch = {"name": "Python", "version": 3.11, "ist_cool": True}
print(f"woerterbuch: {woerterbuch}, Typ: {type(woerterbuch)}")

# Set (Menge) - keine Duplikate
menge = {1, 2, 3, 3, 4, 4, 5}  # Duplikate werden automatisch entfernt
print(f"menge: {menge}, Typ: {type(menge)}")
</code></pre>
</div>

### Typannotationen in Python

Obwohl Python dynamisch typisiert ist, unterstützt es seit Python 3.5 optionale Typannotationen.
Diese dienen der Dokumentation und können von Tools wie mypy zur statischen Typüberprüfung verwendet werden.

<div class="pyscript-example">
<pre><code class="language-python">
# Beispiel für Typannotationen
def greet(name: str) -> str:
    return f"Hallo, {name}!"

# Variablen mit Typannotationen
alter: int = 25
name: str = "Max"
gewichte: list[float] = [65.5, 70.2, 68.7]

print(greet(name))
print(f"In 10 Jahren bist du {alter + 10} Jahre alt.")
</code></pre>
</div>

### Übung: Datentypen

Experimentiere mit verschiedenen Datentypen:

<div class="pyscript-exercise">
<pre><code class="language-python">
# TODO: Erstelle Variablen mit verschiedenen Datentypen und teste ihre Eigenschaften
# Beispiel:
# meine_liste = [1, 2, 3]
# meine_liste.append(4)
# print(meine_liste)

</code></pre>
</div>

## Operatoren

Python unterstützt verschiedene Arten von Operatoren:

### Beispiel: Arithmetische Operatoren

<div class="pyscript-example">
<pre><code class="language-python">
# Addition, Subtraktion, Multiplikation, Division
print(f"7 + 3 = {7 + 3}")
print(f"7 - 3 = {7 - 3}")
print(f"7 * 3 = {7 * 3}")
print(f"7 / 3 = {7 / 3}")  # Fließkomma-Division

# Ganzzahl-Division, Modulo, Potenz
print(f"7 // 3 = {7 // 3}")  # Ganzzahl-Division (abrunden)
print(f"7 % 3 = {7 % 3}")    # Modulo (Rest)
print(f"2 ** 3 = {2 ** 3}")  # Potenz (2³)

# Vorrang von Operatoren
print(f"7 + 3 * 2 = {7 + 3 * 2}")      # Multiplikation vor Addition
print(f"(7 + 3) * 2 = {(7 + 3) * 2}")  # Klammern haben Vorrang
</code></pre>
</div>

### Beispiel: Vergleichs- und logische Operatoren

<div class="pyscript-example">
<pre><code class="language-python">
# Vergleichsoperatoren
print(f"5 > 3: {5 > 3}")
print(f"5 < 3: {5 < 3}")
print(f"5 >= 5: {5 >= 5}")
print(f"5 <= 4: {5 <= 4}")
print(f"5 == 5: {5 == 5}")
print(f"5 != 5: {5 != 5}")

# Logische Operatoren
print(f"True and False: {True and False}")
print(f"True or False: {True or False}")
print(f"not True: {not True}")

# Kombination von Operatoren
x = 10
print(f"5 < x < 15: {5 < x < 15}")  # Verkettete Vergleiche
</code></pre>
</div>

### Übung: Operatoren

Experimentiere mit verschiedenen Operatoren:

<div class="pyscript-exercise">
<pre><code class="language-python">
# TODO: Schreibe Ausdrücke mit verschiedenen Operatoren
# Beispiel:
# ergebnis = (10 + 5) * 2 / 3
# print(f"Das Ergebnis ist: {ergebnis}")

</code></pre>
</div>

## Ein- und Ausgabe

Python bietet einfache Möglichkeiten für Ein- und Ausgabe. Die Funktion `print()` wird für die Ausgabe verwendet,
während `input()` für die Benutzereingabe zuständig ist.

### Beispiel: Ausgabe mit print()

<div class="pyscript-example">
<pre><code class="language-python">
# Einfache Ausgabe
print("Hallo, Welt!")

# Mehrere Werte ausgeben
name = "Python"
version = 3.11
print("Programmiersprache:", name, "Version:", version)

# Formatierte Ausgabe mit f-Strings (ab Python 3.6)
print(f"Programmiersprache: {name}, Version: {version}")

# Formatierte Ausgabe mit format()
print("Programmiersprache: {}, Version: {}".format(name, version))

# Ausgabe mit Trennzeichen und Endzeichen
print("Eins", "Zwei", "Drei", sep=" - ", end=" >>> ")
print("Neue Zeile")
</code></pre>
</div>

> **Hinweis zu input() in PyScript:** Die Funktion `input()` funktioniert in PyScript nicht wie in einer normalen Python-Umgebung.
> In einer lokalen Python-Installation würde sie so verwendet werden:
> ```python
> # Eingabe vom Benutzer
> name = input("Wie heißt du? ")
> print(f"Hallo, {name}!")
> ```
> In PyScript können wir stattdessen HTML-Elemente verwenden, um Benutzereingaben zu erhalten.

### Übung: Formatierte Ausgabe

Experimentiere mit verschiedenen Ausgabeformaten:

<div class="pyscript-exercise">
<pre><code class="language-python">
# TODO: Erstelle formatierte Ausgaben mit verschiedenen Methoden
# Beispiel:
# name = "Max"
# alter = 25
# print(f"{name} ist {alter} Jahre alt.")

</code></pre>
</div>

## Zusammenfassung

In diesem Modul hast du die Grundlagen der Python-Programmierung kennengelernt:

- Variablen werden ohne explizite Typdeklaration erstellt
- Python hat verschiedene eingebaute Datentypen (int, float, str, list, dict, ...)
- Operatoren für arithmetische Berechnungen, Vergleiche und logische Operationen
- Ein- und Ausgabe mit `input()` und `print()`

Im nächsten Modul werden wir uns mit [Kontrollstrukturen](../kontrollstrukturen/index.md) beschäftigen.

### Abschlussübung

Schreibe ein kleines Programm, das verschiedene Konzepte aus diesem Modul kombiniert:

<div class="pyscript-exercise">
<pre><code class="language-python">
# TODO: Schreibe ein Programm, das:
# 1. Verschiedene Variablentypen verwendet
# 2. Arithmetische Operationen durchführt
# 3. Formatierte Ausgaben erzeugt
# 4. Typumwandlungen demonstriert

</code></pre>
</div>

---

[← Zurück zur Übersicht](../index.md) | [Weiter zu Kontrollstrukturen →](../kontrollstrukturen/index.md)