#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Vererbung und Polymorphismus in Python
Vergleich mit C++
"""

# ===== Einfache Vererbung =====
print("=== Einfache Vererbung ===")

# In C++:
# class Person {
# protected:
#     std::string name;
#     int alter;
# public:
#     Person(std::string n, int a) : name(n), alter(a) {}
#     void vorstellen() { std::cout << "Ich bin " << name << ", " << alter << " Jahre alt." << std::endl; }
# };
# 
# class Student : public Person {
# private:
#     std::string studienfach;
# public:
#     Student(std::string n, int a, std::string f) : Person(n, a), studienfach(f) {}
#     void vorstellen() override { 
#         Person::vorstellen();
#         std::cout << "Ich studiere " << studienfach << "." << std::endl; 
#     }
# };

# In Python:
class Person:
    """Basisklasse für Personen"""
    
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter
    
    def vorstellen(self):
        print(f"Ich bin {self.name}, {self.alter} Jahre alt.")

class Student(Person):
    """Abgeleitete Klasse für Studenten"""
    
    def __init__(self, name, alter, studienfach):
        # Konstruktor der Basisklasse aufrufen
        super().__init__(name, alter)
        # Zusätzliches Attribut
        self.studienfach = studienfach
    
    # Methode überschreiben (override)
    def vorstellen(self):
        # Methode der Basisklasse aufrufen
        super().vorstellen()
        # Zusätzliche Funktionalität
        print(f"Ich studiere {self.studienfach}.")

# Objekte erstellen
person = Person("Max", 30)
student = Student("Anna", 22, "Informatik")

# Methoden aufrufen
print("Person stellt sich vor:")
person.vorstellen()

print("\nStudent stellt sich vor:")
student.vorstellen()

# Vererbungshierarchie prüfen
print(f"\nIst student eine Instanz von Student? {isinstance(student, Student)}")
print(f"Ist student eine Instanz von Person? {isinstance(student, Person)}")
print(f"Ist Student eine Unterklasse von Person? {issubclass(Student, Person)}")
print()

# ===== Mehrfachvererbung =====
print("=== Mehrfachvererbung ===")

# In C++:
# class Mitarbeiter {
# protected:
#     double gehalt;
# public:
#     Mitarbeiter(double g) : gehalt(g) {}
#     void gehalt_anzeigen() { std::cout << "Gehalt: " << gehalt << " Euro" << std::endl; }
# };
# 
# class Dozent : public Person, public Mitarbeiter {
# private:
#     std::string fachgebiet;
# public:
#     Dozent(std::string n, int a, double g, std::string f) 
#         : Person(n, a), Mitarbeiter(g), fachgebiet(f) {}
#     void vorstellen() override {
#         Person::vorstellen();
#         std::cout << "Ich bin Dozent für " << fachgebiet << "." << std::endl;
#         gehalt_anzeigen();
#     }
# };

# In Python:
class Mitarbeiter:
    """Klasse für Mitarbeiter"""
    
    def __init__(self, gehalt):
        self.gehalt = gehalt
    
    def gehalt_anzeigen(self):
        print(f"Gehalt: {self.gehalt} Euro")

class Dozent(Person, Mitarbeiter):
    """Klasse mit Mehrfachvererbung von Person und Mitarbeiter"""
    
    def __init__(self, name, alter, gehalt, fachgebiet):
        # Konstruktoren beider Basisklassen aufrufen
        Person.__init__(self, name, alter)
        Mitarbeiter.__init__(self, gehalt)
        # Zusätzliches Attribut
        self.fachgebiet = fachgebiet
    
    # Methode überschreiben
    def vorstellen(self):
        # Methode der ersten Basisklasse aufrufen
        Person.vorstellen(self)
        # Zusätzliche Funktionalität
        print(f"Ich bin Dozent für {self.fachgebiet}.")
        # Methode der zweiten Basisklasse aufrufen
        self.gehalt_anzeigen()

# Dozent-Objekt erstellen
dozent = Dozent("Dr. Schmidt", 45, 5000, "Künstliche Intelligenz")

# Methode aufrufen
print("Dozent stellt sich vor:")
dozent.vorstellen()

# Method Resolution Order (MRO)
print("\nMethod Resolution Order (MRO) für Dozent:")
for klasse in Dozent.__mro__:
    print(f"- {klasse.__name__}")
print()

# ===== Diamond-Problem und super() =====
print("=== Diamond-Problem und super() ===")

# In C++:
# class A {
# public:
#     void methode() { std::cout << "A::methode()" << std::endl; }
# };
# 
# class B : public A {
# public:
#     void methode() override { std::cout << "B::methode()" << std::endl; }
# };
# 
# class C : public A {
# public:
#     void methode() override { std::cout << "C::methode()" << std::endl; }
# };
# 
# class D : public B, public C {
# public:
#     // Ambiguität muss explizit aufgelöst werden
#     void methode() override { B::methode(); }
# };

# In Python:
class A:
    def methode(self):
        print("A.methode()")

class B(A):
    def methode(self):
        print("B.methode()")
        super().methode()

class C(A):
    def methode(self):
        print("C.methode()")
        super().methode()

class D(B, C):
    def methode(self):
        print("D.methode()")
        super().methode()

# D-Objekt erstellen
d = D()

# Methode aufrufen
print("Aufruf von d.methode():")
d.methode()

# Method Resolution Order (MRO)
print("\nMethod Resolution Order (MRO) für D:")
for klasse in D.__mro__:
    print(f"- {klasse.__name__}")
print()

# ===== Abstrakte Klassen und Interfaces =====
print("=== Abstrakte Klassen und Interfaces ===")

# In C++:
# class Form {
# public:
#     virtual double fläche() const = 0;  // Reine virtuelle Methode
#     virtual double umfang() const = 0;  // Reine virtuelle Methode
#     virtual ~Form() {}  // Virtueller Destruktor
# };
# 
# class Kreis : public Form {
# private:
#     double radius;
# public:
#     Kreis(double r) : radius(r) {}
#     double fläche() const override { return 3.14159 * radius * radius; }
#     double umfang() const override { return 2 * 3.14159 * radius; }
# };

# In Python:
from abc import ABC, abstractmethod

class Form(ABC):
    """Abstrakte Basisklasse für geometrische Formen"""
    
    @abstractmethod
    def fläche(self):
        """Berechnet die Fläche der Form"""
        pass
    
    @abstractmethod
    def umfang(self):
        """Berechnet den Umfang der Form"""
        pass
    
    def beschreiben(self):
        """Konkrete Methode (nicht abstrakt)"""
        print(f"Diese Form hat eine Fläche von {self.fläche()} und einen Umfang von {self.umfang()}.")

class Kreis(Form):
    """Konkrete Implementierung eines Kreises"""
    
    def __init__(self, radius):
        self.radius = radius
    
    def fläche(self):
        return 3.14159 * self.radius ** 2
    
    def umfang(self):
        return 2 * 3.14159 * self.radius

class Rechteck(Form):
    """Konkrete Implementierung eines Rechtecks"""
    
    def __init__(self, breite, höhe):
        self.breite = breite
        self.höhe = höhe
    
    def fläche(self):
        return self.breite * self.höhe
    
    def umfang(self):
        return 2 * (self.breite + self.höhe)

# Objekte erstellen
kreis = Kreis(5)
rechteck = Rechteck(4, 6)

# Methoden aufrufen
print("Kreis:")
print(f"Fläche: {kreis.fläche()}")
print(f"Umfang: {kreis.umfang()}")
kreis.beschreiben()

print("\nRechteck:")
print(f"Fläche: {rechteck.fläche()}")
print(f"Umfang: {rechteck.umfang()}")
rechteck.beschreiben()

# Versuch, eine abstrakte Klasse zu instanziieren
try:
    form = Form()  # Dies sollte einen Fehler verursachen
except TypeError as e:
    print(f"\nFehler beim Instanziieren der abstrakten Klasse: {e}")
print()

# ===== Polymorphismus =====
print("=== Polymorphismus ===")

def form_info(form):
    """Funktion, die mit jeder Form-Instanz arbeitet"""
    print(f"Fläche: {form.fläche()}")
    print(f"Umfang: {form.umfang()}")

# Liste mit verschiedenen Formen
formen = [Kreis(3), Rechteck(5, 4), Kreis(2.5)]

# Polymorphe Verwendung
print("Polymorphe Verwendung von Formen:")
for i, form in enumerate(formen, 1):
    print(f"\nForm {i} ({type(form).__name__}):")
    form_info(form)
print()

# ===== Mixin-Klassen =====
print("=== Mixin-Klassen ===")

# In C++ werden Mixins typischerweise über Mehrfachvererbung implementiert
# In Python sind Mixins einfacher und häufiger

class JSONMixin:
    """Mixin-Klasse für JSON-Serialisierung"""
    
    def to_json(self):
        """Konvertiert Objekt-Attribute in ein JSON-Dictionary"""
        return {key: value for key, value in self.__dict__.items() 
                if not key.startswith('_')}

class StringRepresentationMixin:
    """Mixin-Klasse für String-Repräsentation"""
    
    def __str__(self):
        """Erzeugt eine lesbare String-Darstellung"""
        attrs = ', '.join(f"{key}={value}" for key, value in self.__dict__.items()
                         if not key.startswith('_'))
        return f"{self.__class__.__name__}({attrs})"

class Produkt(JSONMixin, StringRepresentationMixin):
    """Klasse, die Mixins verwendet"""
    
    def __init__(self, name, preis, kategorie):
        self.name = name
        self.preis = preis
        self.kategorie = kategorie

# Produkt erstellen
laptop = Produkt("Laptop XYZ", 999.99, "Elektronik")

# Mixin-Funktionalität nutzen
print(f"String-Repräsentation: {laptop}")
print(f"JSON-Repräsentation: {laptop.to_json()}")
print()

# ===== Vererbung vs. Komposition =====
print("=== Vererbung vs. Komposition ===")

# Vererbung: "ist ein"-Beziehung
class Fahrzeug:
    def __init__(self, marke, modell):
        self.marke = marke
        self.modell = modell
    
    def fahren(self):
        print(f"{self.marke} {self.modell} fährt.")

class Auto(Fahrzeug):  # Auto "ist ein" Fahrzeug
    def __init__(self, marke, modell, türen):
        super().__init__(marke, modell)
        self.türen = türen
    
    def hupen(self):
        print("Huuuup!")

# Komposition: "hat ein"-Beziehung
class Motor:
    def __init__(self, leistung):
        self.leistung = leistung
    
    def starten(self):
        print(f"Motor mit {self.leistung} PS startet.")

class Fahrrad:
    def __init__(self, marke, modell):
        self.marke = marke
        self.modell = modell
    
    def fahren(self):
        print(f"{self.marke} {self.modell} wird getreten.")

class Motorrad:  # Motorrad "hat einen" Motor
    def __init__(self, marke, modell, motor_leistung):
        self.marke = marke
        self.modell = modell
        self.motor = Motor(motor_leistung)  # Komposition
    
    def fahren(self):
        self.motor.starten()
        print(f"{self.marke} {self.modell} fährt.")

# Objekte erstellen
auto = Auto("VW", "Golf", 5)
fahrrad = Fahrrad("Cube", "Reaction")
motorrad = Motorrad("Honda", "CBR", 125)

# Methoden aufrufen
print("Auto:")
auto.fahren()
auto.hupen()

print("\nFahrrad:")
fahrrad.fahren()

print("\nMotorrad:")
motorrad.fahren()
print()

# ===== ÜBUNG =====
print("=== ÜBUNG ===")
print("1. Erstelle eine abstrakte Basisklasse 'Tier' mit den abstrakten Methoden 'laut_machen' und 'bewegen'")
print("2. Implementiere zwei konkrete Tierklassen (z.B. 'Hund' und 'Vogel'), die von 'Tier' erben")
print("3. Erstelle eine Mixin-Klasse 'HaustierMixin' mit Methoden wie 'füttern' und 'streicheln'")
print("4. Implementiere eine Klasse 'Haustier', die sowohl von einer Tierklasse als auch vom HaustierMixin erbt")

# TODO: Schreibe deinen Code hier
# from abc import ABC, abstractmethod
# 
# class Tier(ABC):
#     ...

# Beispiellösung (auskommentiert)
"""
from abc import ABC, abstractmethod

class Tier(ABC):
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter
    
    @abstractmethod
    def laut_machen(self):
        pass
    
    @abstractmethod
    def bewegen(self):
        pass
    
    def beschreiben(self):
        print(f"{self.name} ist {self.alter} Jahre alt.")

class Hund(Tier):
    def __init__(self, name, alter, rasse):
        super().__init__(name, alter)
        self.rasse = rasse
    
    def laut_machen(self):
        print(f"{self.name} bellt: Wuff!")
    
    def bewegen(self):
        print(f"{self.name} läuft auf vier Pfoten.")

class Vogel(Tier):
    def __init__(self, name, alter, flügelspannweite):
        super().__init__(name, alter)
        self.flügelspannweite = flügelspannweite
    
    def laut_machen(self):
        print(f"{self.name} zwitschert: Piep!")
    
    def bewegen(self):
        print(f"{self.name} fliegt mit einer Flügelspannweite von {self.flügelspannweite} cm.")

class HaustierMixin:
    def füttern(self):
        print(f"{self.name} wird gefüttert und ist glücklich.")
    
    def streicheln(self):
        print(f"{self.name} wird gestreichelt und genießt es.")
    
    def spielen(self, spielzeug):
        print(f"{self.name} spielt mit {spielzeug}.")

class Haustier(Hund, HaustierMixin):
    def __init__(self, name, alter, rasse, besitzer):
        Hund.__init__(self, name, alter, rasse)
        self.besitzer = besitzer
    
    def beschreiben(self):
        super().beschreiben()
        print(f"{self.name} gehört {self.besitzer}.")

# Test
bello = Haustier("Bello", 5, "Golden Retriever", "Max")
print("Haustier-Hund:")
bello.beschreiben()
bello.laut_machen()
bello.bewegen()
bello.füttern()
bello.streicheln()
bello.spielen("Ball")

print("\nVogel:")
tweety = Vogel("Tweety", 2, 20)
tweety.beschreiben()
tweety.laut_machen()
tweety.bewegen()
"""