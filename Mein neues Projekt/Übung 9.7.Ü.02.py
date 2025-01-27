test = "Ich werde hier meine Zeit verbringen und nichts anderes machen und dann bin ich weg. " + chr(0x2764) # Herz-Zeichen
print(test)

test += "\nDies ist eine neue Zeile."
print(test)

anzahl = test.count('e') # Wie oft das 'e' im Test vorkommt?
print(f"Das Zeichen 'e' kommt {anzahl} Mal im Text vor.")

liste_string = ['Python', 'ist', 'toll']
verbundener_string = ', '.join(liste_string)   
print(verbundener_string)

with open('datei.txt', 'w', encoding='utf-8') as datei:
    datei.write(test)

try:
    with open('datei.txt', 'r', encoding='utf-8') as datei:
        inhalt = datei.read()    
        print(inhalt)
except FileNotFoundError:
    print("Die Datei 'datei.txt' wurde nicht gefunden.")     

import json

daten = {"name" : "Alex", "alter" : "37"}
with open('daten_2.json', mode='w', encoding='utf-8') as datei:
    json.dump(daten, datei, ensure_ascii=False, indent=4)

try:
    with open('daten_2.json', mode='r', encoding='utf-8') as datei:
        json.load(datei)
except FileNotFoundError:
    print("Die Datei 'daten_2.json' wurde nicht gefunden.")            