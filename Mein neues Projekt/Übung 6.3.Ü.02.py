import math, random
from random import randint
a = random.randint(1,10)
print(a)

def berechne_quadrat(x):
    #y = x * x
    return x ** 2 
z = int(input("Geben Sie eine Zahl ein: "))
quadrat = berechne_quadrat(z)
print(f"Die Quadrat dieser Zahl {z} ist: {quadrat}")

if a > 5:
    zufallszahl = berechne_quadrat(a)
    print(f"Das Ergebnis dieser Berechnung des Quadrats von {a} ist: {zufallszahl}")
else:
    print(f"Die Zahl {a} ist kleiner oder gleich 5") 

for i in range(1,a+1):
    #b = print(i)
    print(f"Die aktuelle Zahl lautet: {i}")       
