---
layout: default
title: Python-Kurs für C++ Programmierer
---

# Python-Kurs für C++ Programmierer

Willkommen zum interaktiven Python-Kurs! Dieser Kurs ist speziell für Lernende mit C++-Vorkenntnissen konzipiert und führt schrittweise in die Python-Programmierung ein.

## Kursstruktur

Der Kurs ist in folgende Module unterteilt:

1. [**Grundlagen**](grundlagen/index.md): Variablen, Datentypen, Operatoren, Ein-/Ausgabe
2. [**Kontrollstrukturen**](kontrollstrukturen/index.md): Bedingungen, Schleifen, List Comprehensions
3. [**Funktionen**](funktionen/index.md): Definition, Parameter, Rekursion
4. [**Datenstrukturen**](datenstrukturen/index.md): Listen, Dictionaries, Sets, Tuples
5. [**Objektorientierung**](objektorientierung/index.md): Klassen, Vererbung
6. [**Module und Pakete**](module_und_pakete/index.md): Eigene Module, Standardbibliothek
7. [**Dateien**](dateien/index.md): Lesen und Schreiben von Dateien
8. [**Ausnahmebehandlung**](ausnahmebehandlung/index.md): Try/Except
9. [**Projekte**](projekte/index.md): Praktische Anwendungen

## Interaktive Python-Umgebung

Dieser Kurs enthält interaktive Python-Beispiele, die direkt im Browser ausgeführt werden können. Du kannst den Code bearbeiten und sofort das Ergebnis sehen, ohne Python auf deinem Computer installieren zu müssen.

<div class="pyscript-example">
<h4>Beispiel: Hallo, Python!</h4>
<pre><code class="language-python">
# Dein erstes Python-Programm
print("Hallo, Python!")

# Probiere es aus - ändere den Text und führe den Code aus
name = "Welt"
print(f"Hallo, {name}!")
</code></pre>
</div>

## Einrichtung für lokale Entwicklung

Wenn du Python lokal auf deinem Computer verwenden möchtest, folge diesen Schritten:

### Installation von Python

1. Lade Python von [python.org](https://www.python.org/downloads/) herunter
2. Installiere Python mit der Option "Add Python to PATH"
3. Überprüfe die Installation mit `python --version` im Terminal

### Virtuelle Umgebung einrichten

```bash
# Erstellen der virtuellen Umgebung
python -m venv .venv

# Aktivieren der Umgebung
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Installation der benötigten Pakete
pip install -r requirements.txt
```

### Empfohlene VSCode-Erweiterungen

- Python (Microsoft)
- Pylint
- Python Test Explorer
- Python Docstring Generator
- Python Indent
- Jupyter

## Unterschiede zu C++

Dieser Kurs hebt die wichtigsten Unterschiede zwischen Python und C++ hervor:

- Python verwendet Einrückungen statt geschweifter Klammern
- Dynamische Typisierung statt statischer Typisierung
  - Python unterstützt jedoch optionale Typannotationen für bessere Lesbarkeit und Toolunterstützung
- Automatische Speicherverwaltung
- Alles ist ein Objekt
- Einfachere Syntax mit weniger Boilerplate-Code

<div class="cpp-comparison">
<h4>Vergleich: Hallo Welt in C++ und Python</h4>

<p>C++:</p>
<pre><code class="language-cpp">
#include &lt;iostream&gt;

int main() {
    std::cout << "Hallo, Welt!" << std::endl;
    return 0;
}
</code></pre>

<p>Python:</p>
<pre><code class="language-python">
print("Hallo, Welt!")
</code></pre>
</div>

## Ressourcen

- [Offizielle Python-Dokumentation](https://docs.python.org/de/3/)
- [Python für C++-Programmierer](https://realpython.com/python-vs-cpp/)
- [Python Cheat Sheet](https://www.pythoncheatsheet.org/)