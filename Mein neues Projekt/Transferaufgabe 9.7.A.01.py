import re
import json

# try:
#     with open('file.txt', mode='r', encoding='utf-8') as datei:
#             inhalt_text = datei.read()
# except FileNotFoundError:
#       print("Die Datei 'file.txt' wurde nicht gefunden.")            
def lese_text(dateiname):
    with open(dateiname, mode='r', encoding='utf-8') as datei:
        inhalt_text = datei.read()
        return inhalt_text  

def finde_großbuchstaben_wörter(text):
    return re.findall(r'\b[A-ZÄÖÜ][a-zäöüß]*', text)

def zaehle_wörter(liste_wörter):
    wort_zaehler = {}
    for wort in liste_wörter:
        if wort in wort_zaehler:
            wort_zaehler[wort] += 1
        else:
            wort_zaehler[wort] = 1
    return wort_zaehler 

def speichere_daten(dateiname, dictionary):
    with open(dateiname, mode='w', encoding='utf-8') as datei:
        json.dump(dictionary, datei, ensure_ascii=False, indent=4)           

def lese_datei(dateiname):
    with open(dateiname, mode='r', encoding='utf-8') as datei:
        inhalt_datei = json.load(datei)
        print(inhalt_datei)  

# Hauptprogramm

text = lese_text('fichier.txt')
liste_wörter = finde_großbuchstaben_wörter(text)
wort_zaehler = zaehle_wörter(liste_wörter)
speichere_daten(wort_zaehler, 'wort_zaehler.json')
lese_datei('wort_zaehler.json')              