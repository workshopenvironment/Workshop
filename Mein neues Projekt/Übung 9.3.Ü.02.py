import json

def zaehle_wort(text, wort):
    return text.lower().count(wort.lower())

def ersetze_wort(text, wort, neues_wort):
    wort = 'traurig'
    neues_wort = wort.replace('traurig', 'glücklich')
    return neues_wort     

def wort_teilen_in_saetze(text):
    return text.split('.')

def speichere_als_json(dateiname, daten):
    with open(dateiname, mode='w', encoding='utf-8') as datei:
        json.dump(daten, datei, ensure_ascii=False, indent=4)   


try:
    with open('tagebuch.txt', mode='r', encoding='utf-8') as datei:
        inhalt = datei.read()
        print(inhalt)
except FileNotFoundError:
    print("Die Datei 'tagebuch.txt' wurde nicht gefunden.")
else:
    wort_vorkommen = zaehle_wort(inhalt, 'traurig')
    print(f"Das Wort 'traurig' kommt {wort_vorkommen} Mal vor.")

    aktualisierter_text = ersetze_wort(inhalt, 'traurig', 'glücklich')

    with open('tagebuch_neu.txt', mode='w', encoding='utf-8') as neu_datei:
        neu_datei.write(aktualisierter_text)

    saetze = wort_teilen_in_saetze(aktualisierter_text)
    speichere_als_json('tagebuch_saetze.json', saetze)        
