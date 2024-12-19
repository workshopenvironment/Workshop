import math, random 
from random import randint
x = random.randint(1, 100)
print(x)
def quadratwurzel(x):
    zahl = math.sqrt(x)
    return zahl
neu_zahl = quadratwurzel(x)
print(f"Die Quadratwurzel von dieser zufälliger Ganzzahl ist: {neu_zahl}")
if x > 50:
    neu_zahl_1 = quadratwurzel(x)
    print(f"Die Quadratwurzel dieser neue Zahl {x} ist: {neu_zahl_1}")
else:
    print(f"Zahl ist {x} oder kleiner")
for i in range(1, 6):
    neu_zahl_2 = quadratwurzel(i)
    print(f"Das Ergebnis dieser Zahlen der Funktion Quadratwurzel ist: {neu_zahl_2}")
