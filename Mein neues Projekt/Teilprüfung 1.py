# Dieses Skript fragt den Benutzer, welche Operation durchgeführt werden soll
print("Welche Operation möchten Sie durchführen? Operationen (Addition, Subtraktion, Multiplikation, Division): ")
# Initialisiere eine Variable, um die Schleife zu steuern
laufen = 'Nein' 
while laufen.lower() != 'ja':
    # Schritt a Auswählen der Operationen
    operation = input("Geben Sie bitte Ihre ausgewählte Operation (A, S, M, D):").upper()
    # Prüfen Sie, ob die eingegebene Operation gültig ist
    if operation not in ['A', 'S', 'M', 'D']:
        print("Ungültige Operation. Bitte A, S, M oder D eingeben.")
    else:
        print(f"Operation {operation} ausgewählt.")    
    # Schritt b Operation Addition
    if operation == 'A':
        # Schritt c Zahlen eingeben und direkt umwandeln 
        a = float(input("Geben Sie die erste Zahl ein: "))
        b = float(input("Geben Sie die zweite Zahl ein: "))
        # Schritt d Zahlen addieren
        summe = a + b
        print("Die Summe dieser Zahlen ist: ", summe)
    # Schritt e Operation Subtraktion    
    elif operation == 'S':
        # Schritt f Zahlen eingeben und direkt umwandeln
        c = float(input("Geben Sie die erste Zahl ein: "))
        d = float(input("Geben Sie die zweite Zahl ein: "))
        # Schritt g Zahlen subtrahieren
        subtraktion = c - d
        print("Die Subtraktion dieser Zahlen ist: ", subtraktion)
    # Schritt h Operation Multiplikation    
    elif operation == 'M':
        # Schritt i Zahlen eingeben und direkt umwandeln 
        e = float(input("Geben Sie die erste Zahl ein: "))
        f = float(input("Geben Sie die zweite Zahl ein: "))
        # Schritt j Zahlen multiplizieren
        multiplikation = e * f
        print("Die Multiplication dieser Zahlen ist: ", multiplikation)
    # Schritt k Operation Division     
    elif operation == 'D':
        # Einlesen einer Zeichenkette vom Benutzer
        eingabe = input("Bitte geben Sie eine Zahl ein: ")
        #eingabe_1 = input("Bitte geben Sie eine Zahl ein: ")
        # Überprüfung, ob die Eingabe eine Ganzzahl oder eine Gleitkommazahl ist 
        try:
            # Versuche, die Eingabe in eine Ganzzahl umzuwandeln
            int(eingabe)
            #int(eingabe_1)
            print("Die Eingabe ist eine Ganzzahl.")
        except ValueError:
            try:
                # Versuche, die eingabe in eine Gleitkommazahl umzuwandeln
                float(eingabe)
                #float(eingabe_1)
                print("Die eingabe ist eine Gleitkommazahl.")
            except ValueError:
                print("Die Eingabe ist weder eine Ganzzahl noch eine Gleitkommazahl.")  
        # Schritt l Zahlen eingeben und direkt umwandeln        
        g = float(input("Bitte geben Sie eine gültige Zahl ein: "))    
        h = float(input("Geben Sie eine zweite gültige Zahl ein: "))
        # if not g.isdigit() or not h.isdigit():
        #     print("Ungültige Eingabe. Bitte nur numerishe Werte eingeben.")
        # else:
        #     g = (input("Bitte geben Sie eine gültige Zahl ein: "))    
        #     h = (input("Geben Sie eine zweite gültige Zahl ein: "))       
        # Schritt m Prüfen ob die Divisioin durch Null ist 
        if h == 0:
            print("Ungultiges Division durch Null.")
            h = float(input("Geben Sie erneut die zweite gültige Zahl ein: ")) 
        # Schritt n Zahlen dividieren       
        division = g / h
        print("Die Division dieser Zahlen ist: ", division)
    else: 
        # Schritt o wenn keine Gültige Operation eingegeben wurde
        operation = input("Ungültige Eingabe. Bitte geben Sie erneut eine richtige (A, S, M, D) ")
    # Schritt p Abfrage, ob das Programm beendet werden soll            
    laufen = input("Möchten Sie das Programm beenden? (Ja/Nein): ")