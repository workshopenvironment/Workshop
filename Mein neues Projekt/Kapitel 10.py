import os
print('Unterverzeichnisse:')
inhalt = os.listdir()
for item in inhalt:
    if os.path.isdir(item):
        print(item)

import sys
print('Ihre Systemplattform ist', sys.platform)
print('Python-Version:')
print('Python '+ sys.version)
if sys.platform == 'win32':
    from winsound import Beep
    Beep(700, 1000)
else:
    print('Beep!')       

inhalt = sys.getsizeof(1) # ergibt 28 Bytes das nennt man *Overhead*        
print(inhalt)
a = range(1000000) 
b = list(range(1000000))
contenu = sys.getsizeof(a)
contenus = sys.getsizeof(b)
print(contenu) # Speicherplatz von 48 Bytes (abstrakte Zahlen)
print(contenus) # Speicherplatz für eine liste ist mehr also 8000056 Bytes (tatsächlich einzelne Zahlen-Objekte)

a = [1, 2, 3]
referenz = sys.getrefcount(a)
print(referenz)
b = a
print(b)
referenze = sys.getrefcount(a)
print(referenze)

import sys, random
original_stdout =  sys.stdout
with open('zahlen.txt', 'w') as sys.stdout:
    print('Zufallszahlen zwischen 1 und 1000')
    for i in range(5):
        print(i, random.randint(1, 1000))
sys.stdout = original_stdout
print("Zufallszahlen wurden in eine Datei geschreiben.")       