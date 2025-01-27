text = '\"Diese Buchstabe \u0409 gehört nicht zu dem Alphabet \u263A und muss \n durch {0} geändert werden.\"'
print(text.format("variable Teile"))

try:
    with open('beispiel.txt', 'r', encoding='utf-8') as datei:
        inhalt = datei.read()
        print(inhalt)
except FileNotFoundError:
    print("Die Datei 'beispiel.txt' wurde nicht gefunden.") 

import json
def speichere_json(data, dateiname):
    with open(dateiname, 'w', encoding='utf-8') as datei:
        json.dump(data, datei, ensure_ascii=False) # ensure_ascii = False bedeutet die Zeichen bleibenn in ihrer ursprünlichen Form (z.B. ä, ü, ö, ß, usw...) statt als Unicode-Escapes

daten = {"name" : "Max Mustermann", "alter" : "30"}
speichere_json(daten, 'daten.json')                   
    
try:
    with open('nicht_existierende_datei.txt', 'r', encoding='utf-8') as datei:
        inhalt = datei.read()
        print(inhalt)
except FileNotFoundError:
    print("Die Datei 'nicht_existierende_datei.txt' wurde nicht gefunden.")            