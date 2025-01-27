text = '\"Ich bin hier gewesen \tTabulator und trinke gerne \u2615 \U0001F600Grinsendes Gesicht. \n Ich habe \\Backsclash \u2764Herz Emoji auch bei meiner Schwester einen guten Eindruck gelassen \u263A.\"'
print(text)

wort = input("Geben Sie ein Wort ein: ")
wortanzahl = text.count(wort)
print(f"Das Wort {wort} kommt {wortanzahl} Mal vor.")

ersetze_wort = input("Geben Sie bitte ein neues Wort ein: ")
neuer_text = text.replace(wort, ersetze_wort)
print(text)
print(neuer_text)

with open('modifizierter_text.txt', mode='w', encoding='utf-8') as datei:
    datei.write(neuer_text)

import json

try:
    with open('daten_1.json', mode='r', encoding='utf-8') as datei:
        #json.dump(neuer_text, datei, ensure_ascii=False, indent=4)
        inhalt = json.load('daten_1.json')
        print(inhalt)
except FileNotFoundError:
    print("Die Datei 'daten_1.json' wurde nicht gefunden.")        