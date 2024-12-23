import json
#PFAD = '''{"Datei.txt"}'''
#kontakt = {'Name': name, 'E-mail': email, 'Telefonnumer': telefon}
def speichere_kontakt(name, email, telefon):
    kontakt = [{'Name': name, 'E-mail': email, 'Telefonnumer': telefon}]
    try:
        with open('kontakte.json', 'r+') as file:
            daten = json.load(file)
            daten.append(kontakt)
            file.seek(0)
            json.dump(daten, file, indent=4)
    except (FileNotFoundError, json.JSONDecodeError):
        with open('kontakte.json', 'w') as file:
            json.dump([kontakt], file, indent=4)
        print("Neue Datei wurde erstellt, da keine vorhanden war.")    

def lade_kontakte():
    try:
        with open('kontakte.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Fehler beim laden der Kontakte. Datei existiert nicht oder ist beschädigt.")
        return []

def benutzeroberflaeche():
    while True:
        aktion = input("Möchten Sie einen neuen Kontakt speichern (s) oder vorhandene Kontakte anzeigen (a)? (s/a/beenden): ")
        if aktion.lower() == 'beenden':
            break
        elif aktion.lower() == 's':
            name = input("Name: ")
            email = input("E-mail: ")
            telefon = input("Telefonnummer: ")
            speichere_kontakt(name, email, telefon)
            print("Kontakt gespeichert.")
        elif aktion.lower() == 'a':
            kontakte = lade_kontakte()
            if kontakte:
                for kontakt in kontakte:
                    #print(kontakt)  
                    #print(f"Name: {kontakt.get('Name', 'Unbekannt')}, E-mail: {kontakt.get('E-mail', 'Keine E-Mail')}, Telefonnummer: {kontakt.get('Telefonnummer', 'Keine Telefonnummer')}")
                    print(f"Name: {kontakt['Name']}, E-mail: {kontakt['E-mail']}, Telefonnummer: {kontakt['Telefonnummer']}")
            else:
                print("Keine Kontakte gefunden.")
        else:
            print("Ungültige Eingabe")
if __name__ == "__main__":
    benutzeroberflaeche()                                
