def durchschnittspreis(preis_liste):
    if preis_liste is not None:
        summe = sum(preis_liste) / len(preis_liste)
        return summe
    return None
#liste_produkte = {'Laptop':'999.00', 'Smartphone':'599.00', 'Kopfhörer':'149.00', 'Smartwatch':'249.00', 'Tablet':'399.00', 'E-Book-Reader':'129.00', 'Fitness-Tracker':'79.00', 'Bluetoothlautsprecher':'89.00', 'Powerbank':'39.00', 'Webcam':'59.00'}
def produkt_filter(liste_produkte, buchstabe):
    return list(filter(lambda liste_produkte: liste_produkte.startswith(buchstabe), liste_produkte))
def max_preis(preis_liste):
    if not preis_liste:
        return None
    if len(preis_liste) == 1:
        return preis_liste[0]
    else:
        max_rest = max_preis(preis_liste[1:])
        return preis_liste[0] if preis_liste[0] > max_rest else max_rest
def preis_mit_steuer(preis, steuersatz = 19):
    return preis * (1 + steuersatz/100)
def erhoehe_preise(preis_liste, prozentsatz):
    return list(map(lambda preis: preis * (1 + prozentsatz / 100), preis_liste))
def drucke_produktliste(liste_produkte):
    for i in liste_produkte:
        print(liste_produkte)
    for i in range(len(liste_produkte)):
        print(liste_produkte)



liste = [10, 20, 30, 40]
liste_produkte = ['Apfel', 'Orange', 'Banane', 'Zitrone', 'Clementine']
erhoehung = 0.10 #10%
summe = durchschnittspreis(liste)
print(f"Den Durchschnittspreis dieser Liste ist: {summe}")
print("Durchschnittspreis:", durchschnittspreis(liste))
print("Produkte mit 'B':", produkt_filter(liste_produkte, 'B'))
print("Maximaler Preis:", max_preis(liste))
print("Preis mit Steuer:", preis_mit_steuer(100))
print("Preise erhöht:", erhoehe_preise(liste, erhoehung))
drucke_produktliste(liste_produkte)