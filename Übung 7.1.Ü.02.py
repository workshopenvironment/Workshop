import math, random

def erzeuge_zufallszahlen_liste(anzahl, max_wert):
    a = [random.randint(1, max_wert) for _ in range(anzahl)]
    return a

def berechne_durchschnitt(anzahl_liste):
    return sum(anzahl_liste) / len(anzahl_liste)

def sortiere_und_teile(anzahl_liste):
    anzahl_liste.sort()
    print(type(anzahl_liste))
    mitte = len(anzahl_liste) // 2
    if len(anzahl_liste) % 2 != 0:
        return anzahl_liste[:mitte+1], anzahl_liste[mitte+1:]
    else:
        return anzahl_liste[:mitte], anzahl_liste[mitte:]
    
zufallszahlen_liste = erzeuge_zufallszahlen_liste(10, 100)    

print(f"Zufallszahlen: {zufallszahlen_liste}")

durchschnitt = berechne_durchschnitt(zufallszahlen_liste)
print(f"Durchschnitt: {durchschnitt}")

erste_haelfte, zweite_haelfte = sortiere_und_teile(zufallszahlen_liste)
print(f"Erste Hälfte: {erste_haelfte}")
print(f"Zweite Hälfte: {zweite_haelfte}")