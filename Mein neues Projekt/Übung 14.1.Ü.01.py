class Auto():
    def __init__(self, marke, modell, baujahr):
        self.marke = marke
        self.modell = modell
        self.baujahr = baujahr
        self.kilometerstand = 0

    def fahren(self, kilometer):
        self.kilometerstand += kilometer

    def anzeigen(self):
        print(f"Marke: {self.marke}, Modell: {self.modell}, Baujahr: {self.baujahr}, Kilometerstand: {self.kilometerstand}")

# Erstellung von auto-Objekten

auto1 = Auto("Toyota", "Avensis", "2009")
auto2 = Auto("Hyundai", "Kona", "2022") 
auto3 = Auto("Mercedez", "CLS", "2020")

# Nutzung der Methode 'fahren'

auto1.fahren(15000)
auto2.fahren(2000)
auto3.fahren(250000)

# Anzeigen der Details der Autos

auto1.anzeigen()
auto2.anzeigen()
auto3.anzeigen()
