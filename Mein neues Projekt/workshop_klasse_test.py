# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 11:26:31 2025

@author: Romeo
"""

"""
 
Datentypen:
    Integer, Floats, Booleans, Strings, Listen, Sets, Dictionaries, Tupel
 
Primitive Datentypen: nur ein Element (Integer, Floats, Booleans, Strings)
Datenstrukturen: mehrere Elemente (Listen, Sets, Dictionaries, Tupel)
 
 
Kontrollstrukturen:
    1. if-else-Verknüpfung
    2. Schleifen:
        2.1 for-Schleifen (Wiederholung mit festgelegter Anzahl)
        2.2 while-Schleifen (Bedingte Wiederholung)

 
Funktionen:
    Zur Modularisierung von Algorithmen
Klassen:
    Vereinfacht gesagt eine Sammlung von Funktionen, 
    die zusammenhängende Aufgaben erledigen
    Objektorientierung am besten anhand von geometrischen Objekten vorstellbar
    Rechteck:
        Eigenschaften:
            Länge und Breite
            In der Objektorientierten Programmierung heißen Eigenschaften Attribute
        Operationen:
            Berechnung der Fläche
            Berechnung des Umkreises
            Operationen sind Funktionen, aber Funktionen in einer Klasse
            heißen Methoden
 
"""
 
 
liste = [1,2,3,4]
menge = {1,2,3,4} # jedes Element kommt nur einmal vor
tupel = (1,2,3)   # unveränderlich nach Definition
dictionary = {1:"hallo",2:4,"schlüssel3":42}
 
 
# gebe alle Zahlen von 1 bis 10 aus
 
for zahl in range(1,11):
    print(zahl)

print()
 
# gebe alle Zahlen von 1 bis 10 aus
 
zahl = 1
while zahl <= 10:
    print(zahl)
    zahl += 1
 
print()
 
# if-else-Verknüpfung
 
a = 5
 
if a < 10:
    print("Hilfe")
elif a == 10:
    print("Nein")
else:
    print("Größer")
 
 
# Funktionen
 
liste = [1,2,3,4]
 
summe = 0
for element in liste:
    summe = summe + element
 
print(summe)
 
 
summe = sum(liste)
mittelwert = summe/len(liste)
print(mittelwert)
 
print()
 
 
def mittelwert(liste):
    summe = sum(liste)
    mittelwert = summe/len(liste)
    return mittelwert

 
print(mittelwert(liste))
 
 
 
class Rechteck():
    # Konstruktormethode
    def __init__(self,laenge,breite):
        self.laenge = laenge
        self.breite = breite

    def flaeche(self):
        area = self.laenge * self.breite
        return area

    def umfang(self):
        circum = 2*self.laenge + 2*self.breite 
        return circum

 
 
 
rectangle = Rechteck(3, 1)
laenge = rectangle.laenge
print(laenge)
area = rectangle.flaeche()
print("Fläche ",area)
circum = rectangle.umfang()
print("Umfang ",circum)
 
rectangle = Rechteck(5,3)
laenge = rectangle.laenge
print(laenge)
 
 
"""
 
Array Klasse
 
Array Definition:
    Enthält Elemente von einem Datentyp
    Feste Größe
Insert-Methode, um Elemente zu einem Array hinzuzufügen.
 
 
"""
 
class Array():
    def __init__(self,datatype,size):
        self.array = []
        self.datatype = datatype
        self.size = size
        self.amount = 0

    def insert(self, item):
        # Elemente zum Array hinzufügen
        # Nur von einem Datentyp (also überprüfen)
        # Nur bis feste Größe (also überprüfen)
        if self.amount < self.size:
            #print("Array ist voll.")
            if isinstance(item, self.datatype):
                self.array.append(item)
                self.amount += 1
            else:
                print("Falscher Datentyp")
        else:
            print("Array is voll.")
      
    def __str__(self):
        return str(self.array) 

    def search(self, item):
        if len(self.array) == 0:
            print("Element wurde nicht gefunden")
        else:
            for element in self.array:
                if element == item:
                    return self.array.index(element)                        
            
    def delete(self, element):
        for i in self.array:
            if i == element:
                self.array.remove(i)
                self.amount -= 1

    
    def traverse(self, element):
        for i, element in enumerate(self.array):
            print(f"Index {i} : {element}")
            
print("Array dargestellt und Element hinzufügen")
array = Array(int, 5)
array.insert(3)
array.insert(5)
array.insert(6)
array.insert(8)
array.insert(10)
print(array)
print("Index der gefundene Element im Array(search)")
array.search(6)
print(array.search(6))
print("Element gelöscht und Array dargestellt")
array.delete(8)
print(array)
print("Element hinzugefügt und Array dargestellt")
array.insert(15)
print(array)
print("Alle Elemente des Arrays mit Print ausgeben")
array.traverse(element)
#print(traverse(array))

print(array.array)                