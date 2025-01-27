import os, json

verzeichnis = 'meine_daten'
if not os.path.exists(verzeichnis):
    os.mkdir(verzeichnis)
dictionary = [
    {"name" : "Koffi", "alter" : 50, "beruf" : "Artist"},
    {"name" : "Eto'o", "alter" : 70, "beruf" : "Fussballer"},
    {"name" : "Lula Da silva", "alter" : 76, "beruf" : "Präsident"}
]    
with open(os.path.join(verzeichnis, 'daten_1.json'), 'w') as datei:
    json.dump(dictionary, datei)

try:
    with open(os.path.join(verzeichnis, 'daten_1.json'), 'r') as datei:
        inhalt = json.load(datei)    
        print(inhalt)
except FileNotFoundError:
    print("Die Datei '{inhalt}' wurde nicht gefunden.")    

def aktualisiere_daten():
    name = input("Name: ")
    alter = input("Alter: ")
    beruf = input("Beruf: ")
    neuer_eintrag = {'name': name, 'alter': alter, 'beruf': beruf}

    try:
        with open(os.path.join(verzeichnis, 'daten_1.json'), 'r+', encoding='utf-8') as datei:
            dictionary = json.load(datei)
            dictionary.append(neuer_eintrag)
            datei.seek(0)
            json.dump(dictionary, datei, ensure_ascii=False, indent=4)
            print(dictionary)
    except FileNotFoundError:
        print("Die Datei wurde nicht gefunden.")
aktualisiere_daten()                
