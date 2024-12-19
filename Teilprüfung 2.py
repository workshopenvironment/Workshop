# Datenbankstruktur (Beispiel)
buecherei_datenbank = [
    {"Titel": "Python lernen", "Autor": "Max Mustermann", "Jahr": 2020},
    {"Titel": "Fortgeschrittene Python-Programmierung", "Autor": "Erika Musterfrau", "Jahr": 2021},
    {"Titel": "Python lernen", "Autor": "John Doe", "Jahr": 2019}
]

# a)
def suche_buch(titel,autor=None):
    ergebnisse = []
    for buch in buecherei_datenbank:
        if titel.lower() in buch["Titel"].lower():
            if autor is None or autor.lower() in buch["Autor"].lower():
                ergebnisse.append(buch)
    return ergebnisse
titel_suche = "Python lernen"
autor_suche = "John Doe"
ergebnis_1 = suche_buch(titel_suche)
print(f"Suchergebniss nur nach dem Titel: {ergebnis_1}")
ergebnis_2 = suche_buch(titel_suche,autor_suche)
print(f"Suchergebniss nach Titel und Autor: {ergebnis_2}")     

# b)
def fuege_buch_hinzu(titel,autor,jahr):
    neues_buch = {"Titel": titel, "Autor": autor, "Jahr": jahr}
    ergebnis = buecherei_datenbank.append(neues_buch)
    return ergebnis
titel = input("Geben Sie einen Titel ein: ")
autor = input("Geben Sie ein Autor ein: ")
jahr = int(input("Geben Sie ein Jahr ein: "))
fuege_buch_hinzu(titel,autor,jahr)
print(buecherei_datenbank)

# c)
def buecher_nach_jahr(jahr):
   x = list(filter(lambda buch: int(buch["Jahr"]) == jahr, buecherei_datenbank))
   return x
x = buecher_nach_jahr(jahr)
print(x)
zahl = int(input("Geben Sie das Jahr ein! "))
print(list(x))

# d)
def zeige_datenbank():
    print("Aktuelle Bücher in der Datenbank:")
    for buch in buecherei_datenbank:
        print(f" - {buch["Titel"]} von {buch["Autor"]} im Jahr ({buch["Jahr"]})")
zeige_datenbank()

# e)
while True:
    print("Machen Sie diese Funktionen der Reihe nach: ")
    print("1- Anzeige der Bücherei-Datenbank: ")
    print("2- Fügt ein Buch hinzu: ")
    print("3- Suche nach Buch oder Büchern: ")
    print("4- Nach Jahr Buch oder Büchern filtern: ")
    print("5- Programm beenden")

    auswahl = input("Geben Sie eine Option zwischen 1 bis 5 aus: ")
    
    if auswahl == "1":
        zeige_datenbank()
    elif auswahl == "2":
        fuege_buch_hinzu(titel,autor,jahr)
    elif auswahl == "3":
        suche_buch(titel,autor=None)
    elif auswahl == "4":
        buecher_nach_jahr(jahr)
    elif auswahl =="5":
        beenden = input("Möchten Sie das Programm beenden? (Ja/Nein): ").lower()
        if beenden == 'ja':
            print("---Programm Beendet---")
            break              