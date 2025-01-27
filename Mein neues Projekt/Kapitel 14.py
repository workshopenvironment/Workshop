'''
class Klassenname:
    Docstring
    def __init__(self, ...):
        Anweisungen zur Initialisierung

    def methode_1(self, ...):
        Anweisungen

...
'''
class Flasche:
    'Modell einer Flasche'
    def __init__(self):
        self.inhalt = 0
        self.max_inhalt = 1000
        self.geöffnet = False

    def öffnen(self):
        self.geöffnet = True

    def schließen(self):
        self.geöffnet = False

    def füllen(self, volumen):
        if self.geöffnet:
            if self.inhalt + volumen <= self.max_inhalt:
                self.inhalt += volumen

    def leeren(self):
        if self.geöffnet:
            self.inhalt = 0

a = Flasche()
a.öffnen()
a.füllen(100)
print(a.inhalt)
b = Flasche()
b.öffnen()
b.füllen(500)
b.füllen(1000)
print(b.inhalt)               

class Geld:
    'Die Klasse modelliert Geldbeträge'
    wechselkurs = {'USD':0.8154,
                   'GBP': 1.1129,
                   'EUR':1.0,
                   'JPY':0.0079}
    
    def __init__(self, währung, betrag):
        if währung not in self.wechselkurs:
            raise ValueError(f"Ungültige Währung: {währung}")
        self.währung = währung
        self.betrag = float(betrag)

    def berechneEuro(self):
        'Konertiert den Betrag in Euro.'
        return self.betrag * self.wechselkurs[self.währung]

    def __add__(self, geld):
        'Addiert zwei Geldbeträge.'
        if not isinstance(geld, Geld):
            raise ValueError("Das Argument muss ein Objekt der Klase 'Geld' sein.")
        a = self.berechneEuro()
        b = geld.berechneEuro()
        summe = (a + b) / self.wechselkurs[self.währung]
        return Geld(self.währung, summe)

    def __str__(self):
        'String-Darstellung des Geldbetrags.'
        return '{} {}'.format(self.währung, round(self.betrag, 2))

# Hauptprogramm
if __name__ == '__main__':
    a = Geld('EUR', 10)
    b = Geld('USD', 1)
    print(a+b)    

#from geld import Geld
from tkinter import Tk, Text, Button, LEFT, END

class App():
    def __init__(self):
        self.fenster = Tk()
        self.fenster.title("Geld abrechnen")
        self.text = Text(master=self.fenster, width=30, height=6)
        self.button = Button(master=self.fenster, text='Abrechnen', command=self.abrechnen)
        self.text.pack()
        self.button.pack(side=LEFT, padx=5, pady=5)
        self.fenster.mainloop()

    def abrechnen(self):
        text = self.text.get(1.0, END)
        zeilen = text.split('\n')
        summe = Geld('EUR', 15)
        for z in zeilen:
            try:
                währung, betrag = z.split()
                summe = summe + Geld(währung, betrag)
            except:
                pass
        self.text.insert(END, '\n\nSumme: ' + str(summe))

App()         

# Farbtester
from tkinter import Tk, Label, Text, Button, Frame, BOTH

class Farbtester(Tk):
    'Das Hauptfenster des Farbtesters'
    def __init__(self):
        super().__init__()
        self.title("Farbtester")
        self.geometry("300x200")
        
        # Label zur Anzeige der Farbe
        self.farbanzeige = Label(self, text="Farbe", background="#000000", foreground="white", font=("Arial", 16))
        self.farbanzeige.pack(fill=BOTH, expand=True, pady=10)

        #Container für die Schaltflächen
        self.schaltflächen_frame = Frame(self)
        self.schaltflächen_frame.pack()

        # RGB-Werte initialisieren
        self.rgb = [0, 0, 0]

        # Drei spezielle Schlatflächen erstellen
        self.schaltflächen = []
        for i in range(3):
            btn = Farbknopf(self.schaltflächen_frame, self, i)
            btn.grid(row=0, column=i, padx=5, pady=5)
            self.schaltflächen.append(btn)

        # Initiale Farbe einstellen
        self.aktualisiere_farbe()

    def aktualisiere_farbe(self):
        'Aktualisiert die Hintergrundfarbe des Labels basierend auf RGB.'
        hex_farbe = "#{:02X}{:02X}{:02X}".format(*self.rgb)
        self.farbanzeige.config(background=hex_farbe)

class Farbknopf(Button):
    'Eine Schaltfläche zur Steuerung eines RGB-Werts'
    def __init__(self, parent, controller, index):
        super().__init__(parent, text="0", font=("Arial", 14), width=4, command=self.erhöhe_wert)
        self.controller = controller
        self.index = index

    def erhöhe_wert(self):
        'Erhöht den RGB-Wert und aktualisiert die Anzeige.'
        # Aktuellen Wert erhöhen (0-15 als Hexadezimalenwert)
        self.controller.rgb[self.index] = (self.controller.rgb[self.index] + 1) % 16
        # Text der Schaltfläche aktualisieren
        self.config(text="{:X}".format(self.controller.rgb[self.index]))
        # Farbe im Hauptfenster aktualisieren
        self.controller.aktualisiere_farbe()

# Hauptprogramm
if __name__ == "__main__":
    app = Farbtester()
    app.mainloop()        

# Farbtester andere Möglichkeit
from tkinter import Button, Label, Tk, LEFT

class Taste(Button):
    'Schaltfläche, die eine Hexadezimalziffer anzeigt'
    ziffern = '0123456789ABCDEF'
    def __init__(self, app):
        self.i = 0
        self.app = app
        Button.__init__(self, master=app, text=self.ziffern[self.i], command=self.druecken, font=('Arial', 16), width=3)

    def druecken(self):
        self.i = (self.i + 1) % 16
        self.config(text=self.ziffern[self.i])
        self.app.farbe_anzeigen()

    def ziffer(self):
        return self.ziffern[self.i]

class App(Tk):
    'Anwendungsfenster'
    def __init__(self):
        Tk.__init__(self)
        self.label = Label(master=self, width=20, height=6)
        self.tasten = [Taste(self) for i in range(3)]

        #Layout
        self.label.pack()
        for t in self.tasten:
            t.pack(side=LEFT, padx=5, pady=5)
        self.farbe_anzeigen()
        self.mainloop()

    def farbe_anzeigen(self):
        r, g, b = [t.ziffer() for t in self.tasten]
        code = '#' + r + g + b
        self.label.config(background=code)

App()            

# Zahlenregen ohne Farben und ohne Punktestand

from tkinter import *
from random import randint, choice
from _thread import start_new_thread
from time import sleep

class Zahl:
    def __init__(self, app):
        self.canvas = app.canvas
        self.schläger = app.schläger
        self.wert = 0
        self.id = self.canvas.create_text(0, 0, text='')
        start_new_thread(self.run, ())

    def run(self):
        c = self.canvas
        while True:
            x, y = randint(10, 290), -10
            self.wert = randint(-10, 10)
            c.itemconfigure(self.id, text=str(self.wert))
            c.coords(self.id, x, y)
            x1, y1, x2, y2 = c.coords(self.schläger.id) 
            hit = self.id in c.find_overlapping(x1, y1, x2, y2)
            sleep(randint(0, 30)/10)
            while (y < 200) and not hit:
                sleep(0.05)
                x, y = c.coords(self.id)
                c.move(self.id, 0, 5)
                x1, y1, x2, y2 = c.coords(self.schläger.id)
                hit = self.id in c.find_overlapping(x1, y1, x2, y2)

class Schläger:
    def __init__(self, canvas):
        self.canvas = canvas
        self.id = canvas.create_rectangle(10, 185, 40, 190)

    def links(self):
        self.canvas.move(self.id, -20, 0)

    def rechts(self):
        self.canvas.move(self.id, 20, 0)

class App():
    def __init__(self):
        self.punkte = 0
        self.fenster = Tk()
        self.fenster("Zahlen regen (Spiel)")
        self.canvas = Canvas(self.fenster, width=300, height=200)
        self.schläger = Schläger(self.canvas)
        for i in range(12):
            Zahl(self)
        self.b_links = Button(master=self.fenster, text='<--', command=self.schläger.links)
        self.b_rechts = Button(master=self.fenster, text='-->', command=self.schläger.rechts)
        self.canvas.pack()
        self.b_links.pack(side=LEFT, padx=5, pady=5)
        self.b_rechts.pack(side=LEFT, padx=5, pady=5)
        self.fenster.mainloop()

App()