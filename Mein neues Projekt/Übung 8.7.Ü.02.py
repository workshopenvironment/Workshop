alter = 40
hobbies_liste = ['Fußball spielen', 'Spaziergang', 'Lesen']
lieblingsfarben = ('blau', 'rot', 'weiß')

for i in hobbies_liste:
    print(f"Eines meiner Hobbies ist: {i}")

def jahre_bis_rente(alter):
    if alter < 65:
        rest_jahre = 65 - alter
        print(f"Du hast noch {rest_jahre} Jahren bis zur rente.")
    else:
        print("Du hast schon das Jahrlimit erreicht.")        
ergebnis = jahre_bis_rente(alter)

import json

daten = {"Hobbies": hobbies_liste, "Lieblingsfarben": lieblingsfarben}
#daten = {"Hobbies": ["Fussball spielen", "Spaziergang", "Lesen"], "Lieblingsfarben": ["blau", "rot", "weiß"]}
try:
    with open('persoenliche_daten.json', 'w', encoding = 'utf-8') as datei:
        json.dump(daten, datei, ensure_ascii=False, indent=4) #indent=4:
#Die JSON-Daten werden mit einer Einrückung von 4 Leerzeichen formatiert (lesbarer für Menschen).
        print(daten)
except (FileNotFoundError, json.JSONDecodeError):
    print("Fehler beim speichern der Daten oder Datei existiert nicht.") 


