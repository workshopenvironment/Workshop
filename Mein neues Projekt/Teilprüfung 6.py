class Buch:
    def __init__(self, titel, autor, kategorie, preis):
        self.titel = titel
        self.autor = autor 
        self.kategorie = kategorie
        self.preis = float(preis)

    def __str__(self):
        return '{} {} {} {:.2f}€'.format(self.titel, self.autor, self.kategorie, self.preis)
        #return f"Buch: '{self.titel}' von '{self.autor}', Kategorie: '{self.kategorie}', Preis: '{self.preis:.2f}'€"
    
class Buchladen:
    def __init__(self):
        self.inventar = []

    def hinzufuegen(self, buch):
        self.inventar.append(buch)

    def suche_kategorie(self, kategorie):
        result = []
        for buch in self.inventar:
            if buch.kategorie.lower() == kategorie.lower():
                result.append(buch)
        return result
        #return [buch for buch in self.inventar if buch.kategorie.lower() == kategorie.lower()]

    def berechnen_gesamtpreis(self, liste_buecher):
        gesamtpreis = 0
        for buch in liste_buecher:
            gesamtpreis += buch.preis
        return gesamtpreis    
        #return sum(buch.preis for buch in liste_buecher)
    
# Hauptprogramm
if __name__ == '__main__':
    buchladen = Buchladen()
    buch_1 = Buch("Die Grosse Liebe", "Romeo && Juliet", "Roman", "15.999")
    buch_2 = Buch("KI verstehen", "Erik Müller", "Wissenschaft", "45.012") 
    buch_3 = Buch("Liebe macht Karriere", "Adrien Thomas", "Roman", "25.016")
    buch_4 = Buch("Im Name der Wissenschaft", "Paul Maximillian", "Wissenschaft", "13.992")
    buchladen.hinzufuegen(buch_1)
    buchladen.hinzufuegen(buch_2)
    buchladen.hinzufuegen(buch_3)
    buchladen.hinzufuegen(buch_4)

    print("Bücher nach Kategorie 'Roman' durchsuchen und Gesamtpreis berechnen:\n")
    romane = buchladen.suche_kategorie("Roman")
    for buch in romane:
        print(buch)
    gesamtpreis_romane = buchladen.berechnen_gesamtpreis(romane)
    print(f"Gesamtpreis der Kategorie 'Roman': {gesamtpreis_romane:.2f}€")    

    print("\n\nBücher in der Kategorie 'Wissenschaft' durchsuchen und Gesamtpreis berechnen:\n")
    wissenschaft = buchladen.suche_kategorie("Wissenschaft")
    for buch in wissenschaft:
        print(buch)
    gesamtpreis_wissenschaft = buchladen.berechnen_gesamtpreis(wissenschaft)
    print(f"Gesamtpreis der Kategorie 'Wissenschaft': {gesamtpreis_wissenschaft:.2f}€")    
  