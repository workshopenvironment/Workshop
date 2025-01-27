# def einkaufliste():
#     liste = []
#     print("Bitte geben Sie fünf Lebensmittel für Ihre Einkaufsliste ein:")
#     for i in range(5):
#         lebensmitteln = input(f"Geben Sie ein Lebensmittel ein {i + 1}: ")
#         liste.append(lebensmitteln)
#     print("Einkaufliste erstellt:", liste)
#     return liste
# einkauf_liste = einkaufliste()

einkaufliste = ["Brot", "Äpfel", "Orange", "Bananen", "Wassermelone", "Hönigmelone", "Kiwis"]

# def einkauf_hinzufuegen(lebensmittel):
#     neu_liste = einkaufliste
#     eingabe = input("Geben Sie ein Lebensmittel ein: ")
#     for lebensmittel in neu_liste:
#         if eingabe == lebensmittel:
#             print("Lebensmittel bereits in der Liste")
#         else:
#             neu_liste.append(lebensmittel)
#     print("Neue Einkaufliste erstellt: ", neu_liste)
#     return neu_liste
# neu_liste_1 = einkauf_hinzufuegen(lebensmittel)    

def einkauf_hinzufuegen(lebensmittel):
    if lebensmittel in einkaufliste:
        print("Lebensmittel bereits in der Liste!")
    else:
        einkaufliste.append(lebensmittel)
        print(f"{lebensmittel} wurde zur Einkaufsliste hinzugefügt.")
#eingabe = input("Geben Sie ein Lebensmittel ein: ")
#neu_liste = einkauf_hinzufuegen(eingabe)
#print(einkaufliste)        

for i in range(3):
    eingabe = input("Geben Sie ein Lebensmittel ein: ")
    neu_liste = einkauf_hinzufuegen(eingabe)
#print(einkaufliste) 

try:
    with open('einkaufsliste.txt', 'w') as file:
        for lebensmittel in einkaufliste:
            file.write(lebensmittel + '\n')
except Exception as e:
    print(f"Ein Fehler ist aufgetreten: {e}")

try:
    with open('einkaufsliste.txt', 'r') as file:
        inhalt = file.readlines()
        print(inhalt)
        print("Einkaufliste: ")
        for lebensmittel in inhalt:
            print(lebensmittel.strip())
except Exception as e:
    print(f"Ein Fehler ist aufgetreten beim Lesen der Datei: {e}")
            
