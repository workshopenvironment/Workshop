from datetime import datetime, time

class Bankkonto():
    def __init__(self, inhaber, konto_nr):
        self.inhaber = inhaber
        self.konto_nr = konto_nr
        self.kontostand = 0
        self.transactionen = []

    def einzahlen(self, betrag):
        self.kontostand += betrag
        self.transactionen.append((datetime.now(), "Einzahlung", betrag))
        self.transactionen = self.transactionen[-10:] # Behalte nur die letzten 10 Transaktionen

    def abheben(self, betrag):
        if self.kontostand <= betrag:
            print("Nicht genügend Guthaben")
        else:
            self.kontostand -= betrag
            self.transactionen.append((datetime.now(), "Abhebung", betrag))
            self.transactionen = self.transactionen[-10:]

    def letzte_transactionen(self):
        for datum, typ, betrag, in self.transactionen:
            print(f"{datum}: {typ} von {betrag}€")

def main():
    konto = Bankkonto("Mimi", "DE124567890")
    while True:
        aktion = input("Wählen Sie ein Aktion: (E)inzahlen, (A)bheben, (T)ransaktionen anzeigen, (B)eenden: ").upper()
        if aktion == "E":
            betrag = float(input("Betrag zum Einzahlen: "))
            konto.einzahlen(betrag)
            print(f"{betrag} wurde eingezahlt.")
        elif aktion == "A":
            betrag = float(input("Betrag zum Abheben: "))
            try:
                konto.abheben(betrag)
                print(f"{betrag} wurde abgehoben.")    
            except ValueError as e:
                print(e)
        elif aktion == "T":
            konto.letzte_transactionen()
        elif aktion == "B":
            break
        else:
            print("Ungültige Aktion.")

if __name__ == '__main__':
    main()                            





