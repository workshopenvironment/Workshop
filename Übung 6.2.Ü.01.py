import math
m = math.sqrt(256)
print(m)

from math import pi
radius = 7
umfang = math.pi * radius**2
print(f"Der Umfang ist: {umfang}")

def fahrenheit_zu_celsuis(fahrenheit):
    temp = (fahrenheit - 32) * 5/9
    return temp
fahrenheit = 68
temperatur = fahrenheit_zu_celsuis(fahrenheit)
print(f"Die Temperatur in Celsuis lautet: {temperatur}")

import math 
for i in range (1, 6):
    print(i, end = ' ')

''' Das gesamte Modul importieren: import modulname. Zum Beispiel: import math. 
Um eine Funktion zu verwenden, muss man den Modulnamen voranstellen, z.B. math.sqrt(4).'''

''' Spezifische Funktionen aus einem Modul importieren: from modulname import funktion. Zum Beispiel: 
from math import sqrt. Die Funktion kann dann direkt verwendet werden, z.B. sqrt(4).'''