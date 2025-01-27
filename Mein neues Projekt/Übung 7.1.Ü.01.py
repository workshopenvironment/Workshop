import math, random
from random import randint

zufall_zahl = [random.randint(1, 100) for _ in range(10)]
print(zufall_zahl)

#list = [3, 2, 40, 4, 52, 6, 5, 9, 7, 8, 10]
def sortiere_und_zähle(list_zahlen):
    list_zahlen.sort()
    anzahl = len(list_zahlen)
    return anzahl
a = sortiere_und_zähle(zufall_zahl)
print(a)

tupel_liste = [(a, a**2) for a in zufall_zahl]
print(tupel_liste)

for zahl, quadrat in tupel_liste:
    print(f"Die Zahl {zahl} hat das Quadrat: {quadrat}")

if a > 5:
    print("Mehr als 5 Elemente.")
else:
    print("5 oder weniger Elemente.")    

