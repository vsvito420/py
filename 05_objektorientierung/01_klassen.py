#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Klassen und Objekte in Python
Vergleich mit C++
"""

# ===== Grundlagen von Klassen =====
print("=== Grundlagen von Klassen ===")

# In C++:
# class Person {
# private:
#     std::string name;
#     int alter;
# public:
#     Person(std::string n, int a) : name(n), alter(a) {}
#     void vorstellen() { std::cout << "Ich bin " << name << ", " << alter << " Jahre alt." << std::endl; }
# };

# In Python:
class Person:
    """Eine einfache Klasse zur Repräsentation einer Person."""
    
    def __init__(self, name, alter):
        """Konstruktor (Initialisierer)"""
        self.name = name
        self.alter = alter
    
    def vorstellen(self):
        """Methode zur Vorstellung der Person"""
        print(f"Ich bin {self.name}, {self.alter} Jahre alt.")

# Objekt erstellen (Instanziierung)
# In C++: Person max("Max", 25);
max_person = Person("Max", 25)

# Methode aufrufen
# In C++: max.vorstellen();
max_person.vorstellen()

# Auf Attribute zugreifen
# In C++: nur möglich, wenn Attribute public sind oder Getter existieren
print(f"Name: {max_person.name}")
print(f"Alter: {max_person.alter}")

# Attribute ändern
max_person.alter = 26
print(f"Neues Alter: {max_person.alter}")
print()

# ===== Zugriffsmodifikatoren und Konventionen =====
print("=== Zugriffsmodifikatoren und Konventionen ===")

# In C++ gibt es private, protected und public
# In Python gibt es keine echten Zugriffsmodifikatoren, nur Konventionen

class Konto:
    def __init__(self, inhaber, kontonummer, kontostand=0):
        self.inhaber = inhaber          # Öffentlich (public)
        self._kontonummer = kontonummer  # Geschützt (protected) - Konvention mit _
        self.__kontostand = kontostand   # Privat (private) - Name Mangling mit __
    
    def einzahlen(self, betrag):
        """Öffentliche Methode zum Einzahlen"""
        if betrag > 0:
            self.__kontostand += betrag
            return True
        return False
    
    def abheben(self, betrag):
        """Öffentliche Methode zum Abheben"""
        if 0 < betrag <= self.__kontostand:
            self.__kontostand -= betrag
            return True
        return False
    
    def get_kontostand(self):
        """Getter für den Kontostand"""
        return self.__kontostand
    
    def _interne_methode(self):
        """Geschützte Methode (sollte nicht direkt aufgerufen werden)"""
        print("Diese Methode ist für interne Zwecke gedacht.")
    
    def __sehr_privat(self):
        """Private Methode (Name Mangling)"""
        print("Diese Methode ist sehr privat.")

# Konto erstellen
mein_konto = Konto("Max Mustermann", "DE123456789", 1000)

# Öffentliche Attribute und Methoden
print(f"Inhaber: {mein_konto.inhaber}")
mein_konto.einzahlen(500)
print(f"Kontostand nach Einzahlung: {mein_konto.get_kontostand()}")

# Geschützte Attribute (Konvention)
print(f"Kontonummer (geschützt): {mein_konto._kontonummer}")  # Funktioniert, sollte aber vermieden werden
mein_konto._interne_methode()  # Funktioniert, sollte aber vermieden werden

# Private Attribute (Name Mangling)
# print(mein_konto.__kontostand)  # AttributeError: 'Konto' object has no attribute '__kontostand'
# mein_konto.__sehr_privat()      # AttributeError: 'Konto' object has no attribute '__sehr_privat'

# Name Mangling: __name wird zu _Klassenname__name
print(f"Kontostand über Name Mangling: {mein_konto._Konto__kontostand}")  # Funktioniert, aber sehr schlechter Stil!
mein_konto._Konto__sehr_privat()  # Funktioniert, aber sehr schlechter Stil!
print()

# ===== Properties =====
print("=== Properties ===")

# In C++:
# class Temperatur {
# private:
#     double celsius;
# public:
#     double getCelsius() const { return celsius; }
#     void setCelsius(double c) { celsius = c; }
#     double getFahrenheit() const { return celsius * 9.0/5.0 + 32.0; }
#     void setFahrenheit(double f) { celsius = (f - 32.0) * 5.0/9.0; }
# };

# In Python:
class Temperatur:
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    # Property für Celsius
    @property
    def celsius(self):
        """Getter für Celsius"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, wert):
        """Setter für Celsius"""
        if wert < -273.15:
            raise ValueError("Temperatur unter dem absoluten Nullpunkt!")
        self._celsius = wert
    
    # Property für Fahrenheit
    @property
    def fahrenheit(self):
        """Getter für Fahrenheit"""
        return self._celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, wert):
        """Setter für Fahrenheit"""
        self.celsius = (wert - 32) * 5/9  # Nutzt den Celsius-Setter mit Validierung

# Temperatur-Objekt erstellen
temp = Temperatur(25)

# Properties verwenden (wie Attribute)
print(f"Celsius: {temp.celsius}")
print(f"Fahrenheit: {temp.fahrenheit}")

# Properties setzen
temp.celsius = 30
print(f"Neue Celsius: {temp.celsius}")
print(f"Neue Fahrenheit: {temp.fahrenheit}")

temp.fahrenheit = 68
print(f"Celsius nach Fahrenheit-Änderung: {temp.celsius}")

# Validierung
try:
    temp.celsius = -300  # Unter dem absoluten Nullpunkt
except ValueError as e:
    print(f"Fehler: {e}")
print()

# ===== Klassenmethoden und statische Methoden =====
print("=== Klassenmethoden und statische Methoden ===")

# In C++:
# class MathUtils {
# public:
#     static double PI() { return 3.14159265359; }
#     static double kreisUmfang(double radius) { return 2 * PI() * radius; }
# };

# In Python:
class MathUtils:
    """Utility-Klasse für mathematische Operationen"""
    
    # Klassenvariable
    PI = 3.14159265359
    
    def __init__(self):
        raise NotImplementedError("Diese Klasse sollte nicht instanziiert werden")
    
    @classmethod
    def kreis_umfang(cls, radius):
        """Klassenmethode zur Berechnung des Kreisumfangs
        
        Verwendet die Klassenvariable PI
        """
        return 2 * cls.PI * radius
    
    @staticmethod
    def quadrat_fläche(seitenlänge):
        """Statische Methode zur Berechnung der Quadratfläche
        
        Benötigt keine Klassenvariablen
        """
        return seitenlänge ** 2

# Klassenvariable verwenden
print(f"PI: {MathUtils.PI}")

# Klassenmethode aufrufen (ohne Instanz)
umfang = MathUtils.kreis_umfang(5)
print(f"Umfang eines Kreises mit Radius 5: {umfang}")

# Statische Methode aufrufen (ohne Instanz)
fläche = MathUtils.quadrat_fläche(4)
print(f"Fläche eines Quadrats mit Seitenlänge 4: {fläche}")

# Unterschied zwischen Klassenmethode und statischer Methode:
# - Klassenmethode erhält die Klasse als ersten Parameter (cls)
# - Statische Methode erhält weder self noch cls
print()

# ===== Dunder-Methoden (Magic Methods) =====
print("=== Dunder-Methoden (Magic Methods) ===")

# In C++:
# class Vektor {
# private:
#     double x, y;
# public:
#     Vektor(double x, double y) : x(x), y(y) {}
#     Vektor operator+(const Vektor& other) const { return Vektor(x + other.x, y + other.y); }
#     bool operator==(const Vektor& other) const { return x == other.x && y == other.y; }
#     friend std::ostream& operator<<(std::ostream& os, const Vektor& v);
# };
# std::ostream& operator<<(std::ostream& os, const Vektor& v) {
#     os << "Vektor(" << v.x << ", " << v.y << ")";
#     return os;
# }

# In Python:
class Vektor:
    """Klasse zur Repräsentation eines 2D-Vektors"""
    
    def __init__(self, x, y):
        """Konstruktor"""
        self.x = x
        self.y = y
    
    def __str__(self):
        """String-Repräsentation für print()"""
        return f"Vektor({self.x}, {self.y})"
    
    def __repr__(self):
        """Offizielle String-Repräsentation"""
        return f"Vektor(x={self.x}, y={self.y})"
    
    def __add__(self, other):
        """Addition mit +"""
        if isinstance(other, Vektor):
            return Vektor(self.x + other.x, self.y + other.y)
        return NotImplemented
    
    def __sub__(self, other):
        """Subtraktion mit -"""
        if isinstance(other, Vektor):
            return Vektor(self.x - other.x, self.y - other.y)
        return NotImplemented
    
    def __mul__(self, other):
        """Multiplikation mit * (Skalarprodukt oder Skalierung)"""
        if isinstance(other, (int, float)):
            # Skalierung
            return Vektor(self.x * other, self.y * other)
        if isinstance(other, Vektor):
            # Skalarprodukt
            return self.x * other.x + self.y * other.y
        return NotImplemented
    
    def __eq__(self, other):
        """Gleichheit mit =="""
        if isinstance(other, Vektor):
            return self.x == other.x and self.y == other.y
        return NotImplemented
    
    def __len__(self):
        """Länge mit len()"""
        return 2  # 2D-Vektor hat 2 Komponenten
    
    def __getitem__(self, index):
        """Indexzugriff mit []"""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        raise IndexError("Vektor-Index außerhalb des Bereichs")

# Vektoren erstellen
v1 = Vektor(3, 4)
v2 = Vektor(1, 2)

# __str__ und __repr__
print(f"v1: {v1}")
print(f"Repräsentation: {repr(v1)}")

# __add__ und __sub__
v3 = v1 + v2
print(f"v1 + v2 = {v3}")
v4 = v1 - v2
print(f"v1 - v2 = {v4}")

# __mul__
v5 = v1 * 2
print(f"v1 * 2 = {v5}")
skalarprodukt = v1 * v2
print(f"Skalarprodukt v1 * v2 = {skalarprodukt}")

# __eq__
print(f"v1 == v2: {v1 == v2}")
print(f"v1 == Vektor(3, 4): {v1 == Vektor(3, 4)}")

# __len__ und __getitem__
print(f"Länge von v1: {len(v1)}")
print(f"v1[0]: {v1[0]}")
print(f"v1[1]: {v1[1]}")
print()

# ===== Weitere wichtige Dunder-Methoden =====
print("=== Weitere wichtige Dunder-Methoden ===")

class Sammlung:
    """Klasse zur Demonstration weiterer Dunder-Methoden"""
    
    def __init__(self, elemente=None):
        self.elemente = elemente if elemente is not None else []
    
    def __bool__(self):
        """Wahrheitswert mit bool()"""
        return len(self.elemente) > 0
    
    def __contains__(self, item):
        """Enthaltensein mit in"""
        return item in self.elemente
    
    def __iter__(self):
        """Iterator mit for-Schleife"""
        return iter(self.elemente)
    
    def __call__(self, index):
        """Aufruf als Funktion mit ()"""
        return self.elemente[index]

# Sammlung erstellen
sammlung = Sammlung([1, 2, 3, 4, 5])

# __bool__
if sammlung:
    print("Sammlung ist nicht leer")

leere_sammlung = Sammlung()
if not leere_sammlung:
    print("Leere Sammlung ist leer")

# __contains__
print(f"Enthält 3: {3 in sammlung}")
print(f"Enthält 6: {6 in sammlung}")

# __iter__
print("Elemente der Sammlung:")
for element in sammlung:
    print(element, end=" ")
print()

# __call__
print(f"Element an Index 2: {sammlung(2)}")
print()

# ===== ÜBUNG =====
print("=== ÜBUNG ===")
print("1. Erstelle eine Klasse 'Rechteck' mit Breite und Höhe als Attribute")
print("2. Implementiere Methoden zur Berechnung von Fläche und Umfang")
print("3. Füge Properties hinzu, die sicherstellen, dass Breite und Höhe positiv sind")
print("4. Implementiere die Dunder-Methoden __str__, __eq__ und __add__ (Addition zweier Rechtecke)")

# TODO: Schreibe deinen Code hier
# class Rechteck:
#     ...

# Beispiellösung (auskommentiert)
"""
class Rechteck:
    def __init__(self, breite, höhe):
        self._breite = 0  # Wird durch Property gesetzt
        self._höhe = 0    # Wird durch Property gesetzt
        self.breite = breite  # Property-Setter aufrufen
        self.höhe = höhe      # Property-Setter aufrufen
    
    @property
    def breite(self):
        return self._breite
    
    @breite.setter
    def breite(self, wert):
        if wert <= 0:
            raise ValueError("Breite muss positiv sein")
        self._breite = wert
    
    @property
    def höhe(self):
        return self._höhe
    
    @höhe.setter
    def höhe(self, wert):
        if wert <= 0:
            raise ValueError("Höhe muss positiv sein")
        self._höhe = wert
    
    def fläche(self):
        return self.breite * self.höhe
    
    def umfang(self):
        return 2 * (self.breite + self.höhe)
    
    def __str__(self):
        return f"Rechteck(breite={self.breite}, höhe={self.höhe})"
    
    def __eq__(self, other):
        if not isinstance(other, Rechteck):
            return NotImplemented
        return self.breite == other.breite and self.höhe == other.höhe
    
    def __add__(self, other):
        if not isinstance(other, Rechteck):
            return NotImplemented
        # Addition durch Aneinanderlegen (neue Breite = Summe der Breiten, Höhe bleibt)
        return Rechteck(self.breite + other.breite, self.höhe)

# Test
r1 = Rechteck(5, 3)
r2 = Rechteck(2, 3)

print(f"Rechteck 1: {r1}")
print(f"Fläche: {r1.fläche()}")
print(f"Umfang: {r1.umfang()}")

print(f"Rechteck 2: {r2}")
print(f"r1 == r2: {r1 == r2}")

r3 = r1 + r2
print(f"r1 + r2: {r3}")
print(f"Neue Fläche: {r3.fläche()}")

try:
    ungültig = Rechteck(-1, 5)
except ValueError as e:
    print(f"Fehler: {e}")
"""