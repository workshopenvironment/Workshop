class Buch():
    def __init__(self, titel, autor):
        self.titel = titel
        self.autor = autor
        self.ausgeliehen = False

    def ausleihen(self):
        if self.ausgeliehen:
            print("Buch bereits ausgeliehen.")
        else:
            self.ausgeliehen = True    
            print(f"Das Buch '{self.titel}' von '{self.autor}' wurde ausgeliehen.")

    def zurueckgeben(self):
        if self.ausgeliehen:
            self.ausgeliehen = False
            print(f"Das Buch '{self.titel}' von '{self.autor}' wurde zurückgegeben.")
        else:
            print("Buch war nicht ausgeliehen")    

    def status(self):
        if self.ausgeliehen:
            print(f"Das buch '{self.titel}' von '{self.autor}' ist ausgeliehen.")
        else:
            print(f"Das Buch '{self.titel}' von '{self.autor}' ist verfügbar.")

# Beispil zur Nutzung der Klasse

buch1 = Buch("Python lernen", "Theodoro Bagwell")
buch1.status()
buch1.ausleihen()
buch1.status()
buch1.zurueckgeben()
buch1.status()