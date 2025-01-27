import re
import json
from collections import Counter

try: #f)
    with open('feedback.txt', mode='r', encoding='utf-8') as datei: #a)
        inhalt = datei.read()
        print(inhalt)
        print() #b)
        # Regulärer Ausdruck, um Datumsangaben im Format  DD.MM.YYYY zu finden
        date_pattern = r"\b\d{2}\.\d{2}\.\d{4}\b"
        # Suche alle Übereinstimmungen im Text
        dates = re.findall(date_pattern, inhalt)
        # Gib die Liste der gefundenen Datumsangaben aus 
        print("Gefundene Datumsangaben: ")
        print(dates)
        print()
        #Zähle die Häufigkeit jedes Datums(Dictionary)
        date_counts = Counter(dates) #c)
        print("Häufigkeiten der gefundenen Datumsangaben: ")
        for date, count in date_counts.items():
            print(f"Das Datum/Schlüssel {date}: kommt/Wert {count} Mal vor.")
        print(date_counts)
        print()
        # Liste für die Kommentare
        separate_liste = [] #d)
        # Text in einzelne Zeilen teilen
        lines = inhalt.splitlines()
        # Regulärer Ausdruck, um das Wort "exzellent" zu finden (unabhängig von den Groß-/Kleinschreibung)
        keyword_pattern = r"\bexzellent\b"
        # Durchlaufe jede Zeile und prüfe, ob das Wort "exzellent" enthält
        separate_liste = [line.strip() for line in lines if re.search(keyword_pattern, line, re.IGNORECASE)]
        # Gib die Liste der Kommentaren aus
        print("Kommentare mit dem Wort 'exzellent': ")
        for comment in separate_liste:
            print(comment)        
        print(separate_liste)
        print()
        # Datumsvorkommen speichern in json
        with open('datums_vorkommen.json', mode='w', encoding='utf-8') as datei: #e)
            json.dump(date_counts, datei, ensure_ascii=False, indent=4)
            print(f"\u2705 Datumsvorkommen gespeichert in 'datums_vorkommen.json'.")
        # Exzellente Kommentare speichern in json
        with open('exzellente_feedbacks.json', mode='w', encoding='utf-8') as datei:
            json.dump(separate_liste, datei, ensure_ascii=False, indent=4)
            print(f"\u2705 Exzellente Feedbacks gespeichert in: 'exzellente_feedbacks.json'.")    
except FileNotFoundError: #f)
    print("\u274C Die datei 'feedback.txt' wurde nicht gefunden.")    
except PermissionError:
    print("\u26D4 Fehler: Es fehlen Berechtigungen zum Lesen oder Schreiben der Datei.")
except json.JSONDecodeError:
    print("\u26A0 Fehler beim Verarbeiten von JSON-Daten.")
except Exception as e:
    print(f"\u2757 Ein unerwarteter Fehler ist aufgetreten: {e}")       



   



 





