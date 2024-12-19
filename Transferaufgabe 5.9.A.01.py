def buch_daten_speichern(titel, autor, jahr, seiten = '0'):
    dict = {'titel':titel, 'autor':autor, 'jahr':jahr, 'seiten': seiten}
    return dict
#sammlung = print(list(dict))

def buecher_sammlung(sammlung):
   anzahl_seiten = sum(int(i["seiten"]) for i in sammlung)
   return anzahl_seiten
sammlung = []
for _ in range(3):
    titel = input("Geben Sie den Titel dieses Buch ein! ")
    autor = input("Geben Sie den Namen des Autors dieses Buch ein! ")
    jahr = int(input("Geben Sie das Veröffentlichungsjahr ein! "))
    seiten = input("Geben Sie die Anzahl der Seiten dieses Buch ein (optional)! ")
    seiten = int(seiten) if seiten else 0
    dict = buch_daten_speichern(titel, autor, jahr, seiten)
    sammlung.append(dict)
anzahl_seiten = buecher_sammlung(sammlung)
print(f"Die gesamtanzahl der Seiten aller Bücher beträgt: {anzahl_seiten}")