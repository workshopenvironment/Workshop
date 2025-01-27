import os
DATEINAME = 'example.txt'
def erstelle_datei(DATEINAME, inhalt, verzeichnis= '.'):
    voller_pfad = os.path.join(verzeichnis, DATEINAME)
    try:
        with open(DATEINAME, 'w', encoding='utf-8') as datei:
            datei.write(inhalt)
            print(f"Datei 'DATEINAME' wurde erfolgreich erstellt.")
    except FileNotFoundError:
        print("Die Datei 'DATEINAME' wurde nicht gefunden.")
    except Exception as e:
        print(f"Fehler beim Erstellen der Datei 'Dateiname': {e}")

# Beispielaufruf

erstelle_datei(DATEINAME, 'Das ist ein Test.', 'meinVerzeichnis')            

def listdir_filter(verzeichnis, endung):
    return [datei for datei in os.listdir(verzeichnis) if datei.endswith(endung)]

# Beispielaufruf

print(listdir_filter('.', '.txt'))

def umbenennen_dateien(verzeichnis, alte_endung, präfix):
    for datei in os.listdir(verzeichnis):
        if datei.endswith(alte_endung):
            neuer_name = präfix + datei
            os.rename(os.path.join(verzeichnis, datei), os.path.join(verzeichnis, neuer_name))
    print(f"Dateien wurden umbennant.")

# Beispielaufruf

umbenennen_dateien('.', '.txt', 'neu_')            

import json
DATEINAME_1 = 'example.json'
def json_speichern(dictionary, DATEINAME_1):
    try:
        with open(DATEINAME_1, 'w', encoding='utf-8') as datei:
            inhalt = json.dump(dictionary, datei, ensure_ascii=False, indent=4)
            print(f"Die Datei {inhalt} wurde erfolgreich gespeirchert.")
    except FileNotFoundError:
        print(f"Die Datei 'example.json' wurde nicht gefunden.")  

# Beispielaufruf

meine_daten = [{"name": "Albert", "alter" : 45}, {"name" : "Christoph", "alter" : 35}]
json_speichern(meine_daten, DATEINAME_1)        

def json_laden(DATEINAME_1):
    with open(DATEINAME_1, 'r') as datei:
        return json.load(datei)

# Beispielaufruf

geladene_daten = json_laden(DATEINAME_1)
print(f"Die Datei {geladene_daten} wurde erfolgreich geladen.")

import re
def regex_suche(verzeichnis, regex):
    passende_dateien = []
    for datei in os.listdir(verzeichnis):
        if datei.endswith('.txt'):
            with open(os.path.join(verzeichnis, DATEINAME), 'r') as file:
                inhalt = file.read()
                #print(inhalt)
                if re.search(regex, inhalt):
                    passende_dateien.append(datei)
    return passende_dateien

# Beispielaufruf

print(regex_suche('.', r'\bTest\b'))                