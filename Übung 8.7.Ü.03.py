namen_liste = ["Florence", "Ghislain", "Nelly", "Yannick", "Sophie"]
import json
try:
    with open('freunde.txt', 'w') as datei:
        json.dump(namen_liste, datei)
except Exception as e:
    print("Fehler beim Speichern in der Liste: {e}")

try:
    with open('freunde.txt', 'r') as datei:
        geladene_liste = json.load(datei)
        print("Geladene Freunde Liste:", geladene_liste)
except Exception as e:
    print("Ein Fehler ist aufgetreten beim Laden der Liste: {e}")

try:
    with open("freunde.txt", 'r+') as datei:
        freunde = json.load(datei)
        freunde.append("Felix") # Neuen Namen hinzufügen
        datei.seek(0) # Zurück zum Anfang der Datei gehen
        json.dump(freunde, datei)
        datei.truncate() # Entfernt überschüssige Daten am Ende der Datei
        print("Neu Liste mit neuen Name:", freunde)
except Exception as e:
    print("Ein Fehler ist aufgetreten beim Aktualisieren der Liste: {e}")        

 