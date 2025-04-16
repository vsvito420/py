#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Rekursion in Python
Vergleich mit C++
"""

# ===== Grundlagen der Rekursion =====
print("=== Grundlagen der Rekursion ===")

# Rekursion ist ein Konzept, bei dem eine Funktion sich selbst aufruft
# Jede rekursive Funktion benötigt:
# 1. Einen Basisfall (Abbruchbedingung)
# 2. Einen rekursiven Fall (ruft sich selbst mit verändertem Zustand auf)

# In C++:
# int fakultät(int n) {
#     if (n <= 1) return 1;  // Basisfall
#     return n * fakultät(n - 1);  // Rekursiver Fall
# }

# In Python:
def fakultät(n):
    """Berechnet die Fakultät einer Zahl rekursiv."""
    # Basisfall
    if n <= 1:
        return 1
    # Rekursiver Fall
    return n * fakultät(n - 1)

# Beispielaufrufe
print(f"Fakultät von 5: {fakultät(5)}")  # 5! = 5 * 4 * 3 * 2 * 1 = 120
print(f"Fakultät von 0: {fakultät(0)}")  # 0! = 1 (per Definition)

# Ablauf von fakultät(5):
# fakultät(5) = 5 * fakultät(4)
# fakultät(4) = 4 * fakultät(3)
# fakultät(3) = 3 * fakultät(2)
# fakultät(2) = 2 * fakultät(1)
# fakultät(1) = 1 (Basisfall erreicht)
# Rückwärts auflösen: 2 * 1 = 2, 3 * 2 = 6, 4 * 6 = 24, 5 * 24 = 120
print()

# ===== Fibonacci-Sequenz rekursiv =====
print("=== Fibonacci-Sequenz rekursiv ===")

# In C++:
# int fibonacci(int n) {
#     if (n <= 1) return n;
#     return fibonacci(n - 1) + fibonacci(n - 2);
# }

# In Python:
def fibonacci(n):
    """Berechnet die n-te Fibonacci-Zahl rekursiv."""
    # Basisfälle
    if n <= 0:
        return 0
    if n == 1:
        return 1
    # Rekursiver Fall
    return fibonacci(n - 1) + fibonacci(n - 2)

# Beispielaufrufe
for i in range(10):
    print(f"Fibonacci({i}) = {fibonacci(i)}")

# Ablauf von fibonacci(5):
# fibonacci(5) = fibonacci(4) + fibonacci(3)
# fibonacci(4) = fibonacci(3) + fibonacci(2)
# fibonacci(3) = fibonacci(2) + fibonacci(1)
# fibonacci(2) = fibonacci(1) + fibonacci(0)
# fibonacci(1) = 1 (Basisfall)
# fibonacci(0) = 0 (Basisfall)
# Rückwärts auflösen: 1 + 0 = 1, 1 + 1 = 2, 2 + 1 = 3, 3 + 2 = 5
print()

# ===== Rekursionstiefe und Stack-Überlauf =====
print("=== Rekursionstiefe und Stack-Überlauf ===")

# Python hat eine begrenzte Rekursionstiefe (standardmäßig ca. 1000)
import sys
print(f"Maximale Rekursionstiefe: {sys.getrecursionlimit()}")

# Ändern der Rekursionstiefe (Vorsicht!)
# sys.setrecursionlimit(2000)
# print(f"Neue maximale Rekursionstiefe: {sys.getrecursionlimit()}")

# Beispiel für eine Funktion, die zu einem Stack-Überlauf führen würde
def endlos_rekursiv(n):
    """Eine Funktion ohne ordentlichen Basisfall."""
    print(f"Rekursionstiefe: {n}")
    # Kein Basisfall oder unzureichender Basisfall
    # Auskommentiert, um tatsächlichen Stack-Überlauf zu vermeiden
    # return endlos_rekursiv(n + 1)

# Nicht ausführen, würde zu einem RecursionError führen
# endlos_rekursiv(1)
print()

# ===== Tail-Rekursion =====
print("=== Tail-Rekursion ===")

# Tail-Rekursion ist eine spezielle Form der Rekursion, bei der der rekursive Aufruf
# die letzte Operation in der Funktion ist (keine weiteren Berechnungen danach)

# In C++ können Compiler Tail-Rekursion optimieren (Tail Call Optimization)
# In Python gibt es keine automatische Tail-Call-Optimierung

# Nicht-Tail-Rekursive Fakultät (wie oben)
def fakultät_nicht_tail(n):
    """Nicht-Tail-Rekursive Berechnung der Fakultät."""
    if n <= 1:
        return 1
    return n * fakultät_nicht_tail(n - 1)  # Multiplikation nach dem rekursiven Aufruf

# Tail-Rekursive Fakultät
def fakultät_tail(n, akkumulator=1):
    """Tail-Rekursive Berechnung der Fakultät."""
    if n <= 1:
        return akkumulator
    return fakultät_tail(n - 1, n * akkumulator)  # Keine weitere Berechnung nach dem Aufruf

print(f"Nicht-Tail-Rekursive Fakultät von 5: {fakultät_nicht_tail(5)}")
print(f"Tail-Rekursive Fakultät von 5: {fakultät_tail(5)}")
print()

# ===== Rekursion vs. Iteration =====
print("=== Rekursion vs. Iteration ===")

# Rekursive Lösung (wie oben)
def fibonacci_rekursiv(n):
    """Berechnet die n-te Fibonacci-Zahl rekursiv."""
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_rekursiv(n - 1) + fibonacci_rekursiv(n - 2)

# Iterative Lösung
def fibonacci_iterativ(n):
    """Berechnet die n-te Fibonacci-Zahl iterativ."""
    if n <= 0:
        return 0
    if n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

print(f"Rekursive Fibonacci(10): {fibonacci_rekursiv(10)}")
print(f"Iterative Fibonacci(10): {fibonacci_iterativ(10)}")

# Leistungsvergleich
import time

# Für größere Werte wird der Unterschied deutlicher
n = 30

# Zeitmessung für rekursive Lösung
start = time.time()
fib_rekursiv = fibonacci_rekursiv(n)
ende = time.time()
print(f"Rekursive Fibonacci({n}) = {fib_rekursiv}")
print(f"Zeit für rekursive Lösung: {ende - start:.6f} Sekunden")

# Zeitmessung für iterative Lösung
start = time.time()
fib_iterativ = fibonacci_iterativ(n)
ende = time.time()
print(f"Iterative Fibonacci({n}) = {fib_iterativ}")
print(f"Zeit für iterative Lösung: {ende - start:.6f} Sekunden")
print()

# ===== Memoization zur Optimierung =====
print("=== Memoization zur Optimierung ===")

# Memoization ist eine Technik, bei der Ergebnisse zwischengespeichert werden,
# um wiederholte Berechnungen zu vermeiden

# Manuelle Memoization
def fibonacci_memo(n, memo={}):
    """Berechnet die n-te Fibonacci-Zahl rekursiv mit Memoization."""
    if n in memo:
        return memo[n]
    
    if n <= 0:
        return 0
    if n == 1:
        return 1
    
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

# Mit Decorator aus functools
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_cached(n):
    """Berechnet die n-te Fibonacci-Zahl rekursiv mit automatischer Caching."""
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_cached(n - 1) + fibonacci_cached(n - 2)

# Leistungsvergleich
n = 35

# Zeitmessung für einfache rekursive Lösung
start = time.time()
fib_rekursiv = fibonacci_rekursiv(n)
ende = time.time()
print(f"Einfache Rekursion ({n}): {ende - start:.6f} Sekunden")

# Zeitmessung für Memoization
start = time.time()
fib_memo = fibonacci_memo(n)
ende = time.time()
print(f"Mit Memoization ({n}): {ende - start:.6f} Sekunden")

# Zeitmessung für lru_cache
start = time.time()
fib_cached = fibonacci_cached(n)
ende = time.time()
print(f"Mit lru_cache ({n}): {ende - start:.6f} Sekunden")

# Zeitmessung für iterative Lösung
start = time.time()
fib_iterativ = fibonacci_iterativ(n)
ende = time.time()
print(f"Iterativ ({n}): {ende - start:.6f} Sekunden")
print()

# ===== Praktische Anwendungen der Rekursion =====
print("=== Praktische Anwendungen der Rekursion ===")

# 1. Verzeichnisstruktur durchsuchen
import os

def liste_dateien(verzeichnis, ebene=0):
    """Listet alle Dateien in einem Verzeichnis und seinen Unterverzeichnissen rekursiv auf."""
    einrückung = "  " * ebene
    print(f"{einrückung}Verzeichnis: {verzeichnis}")
    
    try:
        for eintrag in os.listdir(verzeichnis):
            pfad = os.path.join(verzeichnis, eintrag)
            if os.path.isdir(pfad):
                liste_dateien(pfad, ebene + 1)  # Rekursiver Aufruf für Unterverzeichnisse
            else:
                print(f"{einrückung}  Datei: {eintrag}")
    except PermissionError:
        print(f"{einrückung}  Keine Berechtigung für dieses Verzeichnis")
    except FileNotFoundError:
        print(f"{einrückung}  Verzeichnis nicht gefunden")

# Nicht ausführen, um die Ausgabe übersichtlich zu halten
# liste_dateien(".")

# 2. Quicksort-Algorithmus
def quicksort(arr):
    """Sortiert eine Liste mit dem Quicksort-Algorithmus (rekursiv)."""
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    links = [x for x in arr if x < pivot]
    mitte = [x for x in arr if x == pivot]
    rechts = [x for x in arr if x > pivot]
    
    return quicksort(links) + mitte + quicksort(rechts)

# Beispiel
unsortiert = [3, 6, 8, 10, 1, 2, 1]
sortiert = quicksort(unsortiert)
print(f"Unsortiert: {unsortiert}")
print(f"Sortiert: {sortiert}")

# 3. Türme von Hanoi
def türme_von_hanoi(n, quelle, ziel, hilfe):
    """Löst das Türme von Hanoi-Problem für n Scheiben."""
    if n == 1:
        print(f"Bewege Scheibe 1 von {quelle} nach {ziel}")
        return
    
    türme_von_hanoi(n - 1, quelle, hilfe, ziel)
    print(f"Bewege Scheibe {n} von {quelle} nach {ziel}")
    türme_von_hanoi(n - 1, hilfe, ziel, quelle)

print("\nTürme von Hanoi mit 3 Scheiben:")
türme_von_hanoi(3, "A", "C", "B")
print()

# ===== ÜBUNG =====
print("=== ÜBUNG ===")
print("1. Schreibe eine rekursive Funktion, die prüft, ob ein String ein Palindrom ist")
print("2. Implementiere den Euklidischen Algorithmus zur Berechnung des GGT rekursiv")
print("3. Schreibe eine rekursive Funktion, die eine Liste umkehrt")

# TODO: Schreibe deinen Code hier
# def ist_palindrom(text):
#     ...

# Beispiellösung (auskommentiert)
"""
# 1. Palindrom-Prüfung
def ist_palindrom(text):
    # Entferne Leerzeichen und wandle in Kleinbuchstaben um
    text = text.lower().replace(" ", "")
    
    # Basisfall: Ein leerer String oder ein einzelnes Zeichen ist ein Palindrom
    if len(text) <= 1:
        return True
    
    # Prüfe, ob das erste und letzte Zeichen gleich sind
    if text[0] != text[-1]:
        return False
    
    # Rekursiver Fall: Prüfe den Rest des Strings
    return ist_palindrom(text[1:-1])

print(f"'radar' ist ein Palindrom: {ist_palindrom('radar')}")
print(f"'Anna' ist ein Palindrom: {ist_palindrom('Anna')}")
print(f"'Python' ist ein Palindrom: {ist_palindrom('Python')}")

# 2. Euklidischer Algorithmus (GGT)
def ggt(a, b):
    # Basisfall: Wenn b gleich 0 ist, ist a der GGT
    if b == 0:
        return a
    
    # Rekursiver Fall: GGT(a, b) = GGT(b, a mod b)
    return ggt(b, a % b)

print(f"GGT(48, 18) = {ggt(48, 18)}")
print(f"GGT(17, 5) = {ggt(17, 5)}")

# 3. Liste umkehren
def liste_umkehren(liste):
    # Basisfall: Eine leere Liste oder eine Liste mit einem Element
    if len(liste) <= 1:
        return liste
    
    # Rekursiver Fall: Erstes Element ans Ende der umgekehrten Restliste anhängen
    return liste_umkehren(liste[1:]) + [liste[0]]

original = [1, 2, 3, 4, 5]
umgekehrt = liste_umkehren(original)
print(f"Original: {original}")
print(f"Umgekehrt: {umgekehrt}")
"""