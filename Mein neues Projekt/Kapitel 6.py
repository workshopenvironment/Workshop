# -*- coding: utf-8 -*-
"""
Spyder-Editor

Dies ist eine temporäre Skriptdatei.
"""

import math, random
import math as m
from math import sqrt
from math import pi

from random import randint
for i in range(1, 6):
    zufallszahl = randint(1, 6)
    print(zufallszahl, end = '  ')
a = math.sqrt(2)
b = m.sqrt(3)
c = sqrt(4)
r = 5
d = 2 * pi * r**2
print(a, b)
print(b, c)
print(d)
#print(zeitpunkt)

# =============================================================================
# from time import localtime, sleep
# while True:
#     zeitpunkt = localtime()
#     print(zeitpunkt.tm_hour, 'Uhr', zeitpunkt.tm_min, 'Min', zeitpunkt.tm_sec, 'Sec')
#     sleep(60)
# =============================================================================
from math import radians, tan
entfernung = float(input("Entfernung zum Baum (m): "))
a = float(input("Augenhöhe (m):"))
alpha = float(input("Blickwinckel (Grad): "))
math.radians(alpha)
print(alpha)
h = a + tan(radians(alpha)) * entfernung
print(f"Höhe des Baums: {h}")

from random import randint
for i in range(0, 100):
    zufallszahl = 55
    print("Bitte geben Sie eine Zahl zwischen 0 und 100 ein.")
    a = random.randint(0, 100)
    print(f"Zahl: {a}")
    if a >= 100:
        print("Zu groß!")
    elif a <= 100:
        print(f"Zu klein!")
    elif a == zufallszahl:
        print(f"Herzlichen Glückwunsch! Sie haben die Zahl gefunden! {a}")
    else:
        print("Keine zahl gefunden")
print("Keine zahl gefunden")        

from time import localtime, sleep
while True:
    zeit = localtime()
    if (6 <= zeit.tm_hour <= 12):
        print(zeit.tm_hour, 'Uhr', zeit.tm_min)
        print("Guten Morgen")
    elif (12 <= zeit.tm_hour <= 18):
        print("Guten Tag")
    elif (18 <= zeit.tm_hour <= 24):
        print("Guten Abend")            
        
t = ('Radiergummi', 0.45)
artikel, preis = t        
warenstand = [('Papier, 500 Blatt', 4.45), ('Laminierfolien Din A 4', 2.50), ('Radiergummi', 0.45)]
for artikel, preis in warenstand:
    print(artikel, 'Preis: ', preis, '€')
a = warenstand.count(t)
b = len(warenstand)
print(a, b)


import math, random
from random import choice
def ziehe_lotto_zahlen():
    zahlen = list(range(1, 50))
    gezogene_zahlen = []
    while len(gezogene_zahlen) < 6:
        zahl = random.choice(zahlen)
        if zahl not in gezogene_zahlen:
            gezogene_zahlen.append(zahl)
    return sorted(gezogene_zahlen)
lottozahlen = ziehe_lotto_zahlen()
print(f"Die gezogenen Lottozahlen sind: {lottozahlen}")


def binaere_suche(liste, ziel):
    #links, rechts = 0, len(liste) - 1
    links = 0
    rechts = len(liste)-1
    while (links <= rechts):
        mitte = (links + rechts) // 2
        if liste[mitte] == ziel:
            return mitte
        elif liste[mitte] < ziel:
            links = mitte + 1
        else:
            rechts = mitte - 1
    return None
liste = [1, 2, 3, 4, 5, 6]
ziel = 6 
index = binaere_suche(liste, ziel)
print(f"Das element {ziel} wurde an Position {index} gefunden.") 
#if index != -1:
#   print(f"Das element {ziel} ist nicht in der Liste.")

# Programmieren Sie einen Weihnachtsbaum           
# prime number generation (Projekt)  

print('   \n Guten \n Morgen \n'.strip())
