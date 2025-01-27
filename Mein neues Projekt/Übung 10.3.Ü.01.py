import os
def erstelle_verzeichnis(directory):
    if os.path.exists(directory):
        print("Verzeichnis 'directory' existiert schon.")
    else:
        os.mkdir(directory)
        print("Verzeichnis 'directory' wurde erstellt.")    

def speichere_text_in_datei(dateiname, text):
    try:
        with open(dateiname, 'w', encoding='utf-8') as datei:
            datei.write(text)
            print(f"Der Text wurde in 'dateiname' gespeichert.")
    except FileNotFoundError:
        print("Die Datei 'dateiname' wurde nicht gefunden.")                

def lese_datei(dateiname):
    try:
        with open(dateiname, 'r', encoding='utf-8') as datei:
            inhalt = datei.read()
            print(f"Die datei 'dateiname' wurde gelesen. Inhalt von '{dateiname}': \n{inhalt}")
    except FileNotFoundError:
        print("Die Datei 'dateiname' wurde nicht gefunden. ")    

def liste_dateien_in_verzeichnis(directory):
    inhalt = os.listdir(directory)
    print(f"Dateien in '{directory}':")
    for item in inhalt:
        if os.path.isdir(item):
            print(item)            

# Hauptprogramm

directory = 'MeineDaten'
dateiname = os.path.join(directory, 'beispiel.txt')
text = "Das ist ein Beispieltext."

erstelle_verzeichnis(directory)
speichere_text_in_datei(dateiname, text)
lese_datei(dateiname)
liste_dateien_in_verzeichnis(directory)