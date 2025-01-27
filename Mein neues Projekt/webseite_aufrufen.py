# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 14:24:30 2025

@author: Romeo
"""

from urllib.request import urlopen # Daten aus dem Internet 
from re import findall # aus dem Kapitel 9 für regüläre Ausdrücke

def urls_finden(url_webseite):
    'Liefert eine Menge mit allen URLs auf webseite'
    with urlopen(url_webseite) as stream: # Webseite mit dem URL 'webseite' wird aus dem Internet heruntergeladen und dem Stream 'stream' zugeordnet
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
    
    