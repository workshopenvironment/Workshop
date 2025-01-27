# x = "hello“
# print(id(x)) # Rufe die Speicheradresse von 'x' ab

# # Versuchen Sie, die Zeichenkette zu ändern
# x = x + "world“
# print(id(x)) # Speicheradresse ist anders, ein neues Objekt wird erstellt

# print(x) # Ausgabe: "hello world“

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