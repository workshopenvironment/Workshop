import json

# Definition der Funktion, die eine Liste von Namen aus einer Textdatei liest
def namen_aus_datei(dateiname):
    try:
        with open(dateiname, 'r', encoding='utf-8') as datei:
            namen = [zeile.strip() for zeile in datei] # Jede Zeile in der Datei wird mit .strip() berücksichtigt ... Entfernen der Leerzeichen überall in der datei
            return namen 
    except FileNotFoundError: # Wenn datei nicht existiert
        print(f"Ein Fehler ist aufgetreten beim Laden die Datei {dateiname}.")
        return []
    except IOError: # Fehler beim Zugriff auf die Datei
        print(f"Ein Fehler ist aufgetreten beim Lesen die Datei {dateiname}.")
        return []
    except Exception as e: # Unerwartete Fehler und gibt fehlermeldung aus
        print("Ein Fehler ist aufgetreten: {e}")
        return []

dateiname = 'textdatei.txt'    
namen_liste = namen_aus_datei(dateiname) # Aufruf der Funktion
if namen_liste:
    print(f"Gelesene Namen: {namen_liste}") # gibt die Liste der Namen als Array zurück
else:
    print(f"Es wurden keine Namen geladen.") # Datei existiert nicht von daher keine Namen

# konvertiert die Liste der Namen in JSON-Format und speichert sie in der angegebenen Datei
def umwandlung(namen, dateiname):
    try:
        with open(dateiname, 'w', encoding='utf-8') as datei:
            json.dump(namen, datei, ensure_ascii=False, indent=4) # Datei gespeichert 
            print(f"Namen wurden erfolgreich in der datei {dateiname} gespeichert.")
    except IOError:
        print(f"Fehler: Ein Fehler ist beim Schreiben in die Datei '{dateiname}' aufgetreten.")        
        print(f"Fehler: Ein Fehler ist beim Schreiben in die Datei {dateiname} aufgetreten.")
    except Exception as e:
        print("Ein unerwartete Fehler ist aufgetreten: {e}")
        
eingabedatei = "textdatei.txt"
ausgabedatei = "textdatei.json"

namen_liste = namen_aus_datei(eingabedatei)
if namen_liste:
    umwandlung(namen_liste, ausgabedatei)
else:
    print("Keine Namen vorhanden, die gespeichert werden könnten.")    

def benutzeroberflaeche():
    MENÜ = ''' 
    1- Namen aus der Datei lesen
    2- Namen als JSON-Format speichern
    3- Namen anzeigen
    4- Beenden     
'''
    namen_liste  = []
    while True:
        print(MENÜ)
        try:
            auswahl = int(input("Wählen Sie bitte eine Option aus (1-4): "))
        except ValueError: # Prüfen ob der Benutzer eine Zahl oder einen String eingibt und spückt Fehler aus indem fall einen String eingegen wurde
            print("Ungültige Eingabe. Bitte geben Sie eine Zahl zwischen 1 und 4 ein: ")
            continue
        if auswahl == 1:
            dateiname = input("Geben Sie den Namen der Datei ein: ")    
            namen_liste = namen_aus_datei(dateiname)
            if namen_liste:
                print(f"Namen erfolgreich gelesen: {namen_liste}")
            else:
                print("Keine Namen gefunden.")
        elif auswahl == 2:
            if not namen_liste:
                print("Es gibt keine Namen, die gespeichert werden können. Bitte geben Sie zuerst Namen ein.")
            else:
                ausgabedatei = input("Geben Sie den Namen der Datei ein, in der die Namen gespeichert werden sollen: ")
                umwandlung(namen_liste, ausgabedatei)
        elif auswahl == 3:
            if not namen_liste:
                print("Es gibt keine Namen, die angezeigt werden können. Bitte geben Sie zuerst Namen ein.")
            else:
                print(f"Akruelle Liste der Namen: {namen_liste}")
        elif auswahl == 4:
            print("-----Programm beendet-----")
            break
        else:
            print("Ungültige Auswahl. Bitte wählen Sie eine Option zwischen 1 und 4 aus.")

benutzeroberflaeche()                                                

