f = open('text.txt', 'w')
f.write('Annelies Geburtstag: 15. November')
f.close()

g = open('text.txt', 'r')
erinnerung = g.read()
g.close()
print(erinnerung)

b = b'fdfwjjs-'
a = b.decode()
print(list(b))
print(a)

try:
    stream = open('text.txt', 'r')
    daten = stream.read()
    stream.close()
except:
    print("Fehler")    

stream = open('text.txt', 'w')
try:
    neu_datei = stream.write('Meine Daten')
except:
    print('Fehler!')
finally:
    stream.close()     
print(stream)
print(neu_datei, '+')

# Die ist gleich als den try: except: finally: aber kürzer und eleganter
with open('text.txt' , 'w') as stream:
    stream.write('Meine neuen Daten \n')
    stream.write('Daten für das Experiment')
    #3/0

import pickle # Datenstruktur speichern und laden
liste = [1, 2, 3]
with open('liste.dat', 'wb') as stream:
    pickle.dump(liste, stream)
with open('liste.dat', 'rb') as stream:
    liste_1 = pickle.load(stream)
print(liste_1)        

from time import time # Digitaler Planer(Dinge eintragen, die man zu erledigen sind. Mit Stunden/Minuten dabei)
import pickle

PFAD = 'plan.dat'
MENÜ = '''
n: neue Aktivität eingeben
d: dringenste Aktivitäten
e: Ende
'''
def laden():
    try:
        with open('PFAD', 'rb') as f:
            plan = pickle.load(f)
    except:
        plan = []
    return plan 
def speichern (plan):
    with open('PFAD', 'wb') as f:
        pickle.dump(plan, f)
def eingabe(plan):
    aktivität = input('Aktivität: ')
    stunden = input('In wie viel Stunden zu erledigen? ')
    plan += [(int(stunden) * 3600 + time(), aktivität)]
    speichern(plan)
def ausgabe(plan):
    plan.sort()
    dringend = plan[0:5]
    for deadline, aktivität in dringend:
        restzeit = (deadline - time())/60
        print('Noch', round(restzeit), 'Minuten für:', aktivität)
plan = laden()
#auswahl = 'x'
while ausgabe != 'e':
    print(MENÜ)
    auswahl = input('Auswahl: ')
    if auswahl == 'n':
        eingabe(plan)
    elif auswahl == 'd':
        ausgabe(plan)
    else:    
        print('Bis bald!')    
        break                            

import json # Daten im JSON-Format speichern
TEL = '''{"Tom": ["0172 567 343", "03202 67231"], "Anna": [], "Tina": ["0201 89 7551"]}'''
tel = json.loads(TEL)
for name in tel.keys():
    print(name, tel[name])

from urllib.request import urlopen # Daten aus dem Internet 
from re import findall # aus dem Kapitel 9 für regüläre Ausdrücke

def urls_finden(url_webseite):
    'Liefert eine Menge mit allen URLs auf webseite'
    with urlopen(url_webseite) as stream: # Webseite mit dem URL 'webseite' wird aus dem Internet heruntergeladen und dem Stream f zugeordnet
        htmltext = stream.read().decode() # Inhalt der Webseite wird gelesen und als String dem Namen 'htmltext' zugewiesen
    reg = r'https?://.+?\.html' # reguläre Ausdruck sagt: zuerst kommt 'http',  dann eventuell 's', dann '://', eine möglich kurze Zeichenfolge (mit mindestens einem Zeichen), die so gewählt ist, dass danach '.html' folgt. Ein wichtiger Aspekt des regulären Ausdrucks ist der >> nicht gierige<< Quantor +?.    
    url_liste = findall(reg, htmltext) # Liste aller gefundenen URLs wird erstellt
    return set(url_liste) # zurückgegeben wird die Menge der gefundenen URLs. In ihr kommt jeder URL nur einmal vor

# Hauptprogramm
url = input('Webseite: ')
try:
    urls = urls_finden(url)
    print('Ich habe folgende URLs gefunden:')
    for url in urls:
        print(url)
except:
    print('Ich konnte keine URLs finden.')
    print('Prüfen Sie die Internetverbindung.')        