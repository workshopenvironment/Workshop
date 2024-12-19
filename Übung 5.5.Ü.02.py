def namens_umrechner(betrag, waehrung='USD'):
    if waehrung == 'USD':
        return  betrag * 1.1
    elif waehrung == 'GBP':
        return betrag * 0.9
    else:
        return None
while True:
    print("Währungsumrechner: EUR zu USD oder GBP")
    betrag = float(input("Bitte geben Sie den Betrag in EUR ein, den Sie umrechnen möchten: "))
    waehrung = input("Bitte geben Sie die Währung ein, in die Sie umrechnen möchten (USD/GBP). Drücken Sie enter für USD: ").upper()
    if waehrung not in ['USD', 'GBP', '']:
        print("Die angegebene Währung wird nicht unterstützt.")
    # elif waehrung == '': ZU VERSTEHEN
    #     ergebnis = namens_umrechner(betrag)
    else:    
        ergebnis = namens_umrechner(betrag, waehrung)   
        if ergebnis is not None:
            print(f"Umrechnungsergebnis: {ergebnis:.2f} {waehrung}")
            print()
            print(f"Umrechnungsergebnis: {ergebnis} {waehrung}")
            print()
            print(f"Umrechnungsergebnis: {round(ergebnis, 2)} {waehrung}")
        else:
            print("Es gab ein Problem bei der Währungsumrechnung.")
    laufen = input("Möchten Sie eine weitere Umrechnung durchführen? (ja/nein): ").lower()
    if laufen != 'ja':
        print("Programm beendet.")
        break            