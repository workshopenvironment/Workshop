''' Kapitel 11.pyw
Die Extension .pyw (statt .py) am Ende des Dateinamens ist von Bedeutung,
wenn das Programm durch Anklicken des Programmicons gestartet wird. 
'''

from tkinter import Tk, Label
from tkinter import *
from random import choice
SPRÜCHE = ['Du siehst heute gut aus', 'Du schaffst es!', 'Heute ist dein Tag!', 'Alles wird gelingen!']
def auswählen():
    text = choice(SPRÜCHE)
    label.config(text=text)
fenster = Tk()
fenster.title("Fenster")
button = Button(master=fenster, text='Neue Motivation', command=auswählen)
label = Label(master=fenster, width=25, height=2, font=('Arial', 16), text=SPRÜCHE[1], foreground='green')
label_1 = Label(master=fenster, text = 'Guten Morgen!', font=('Courier', 20), foreground='blue')
label_2 = Label(master=fenster, text = 'Schön dich zu sehen!', font=('Arial', 16), height=2, width=20, foreground='red')
label_2.pack()
label_1.pack()
label.pack(side=LEFT)
button.pack(side='right', padx=10)
fenster.mainloop()

from tkinter import Tk, Label, Button
from random import choice

def zufallsfarbe():
    z = '0123456789ABCDEF'
    return '#' + choice(z) + choice(z) + choice(z)

def farben_ändern():
    for feld in felder:
        feld.config(background=zufallsfarbe())

# Hauptprogramm

fenster = Tk()
fenster.title("Farben Ändern")
felder = []
for i in range(5):
    for j in range(5):
        feld = Label(master=fenster, width=8, height=2)
        felder.append(feld)
        feld.grid(column=i, row=j, padx=1, pady=1)
button = Button(master=fenster, text='Neue Farben', command=farben_ändern)
button.grid(column=0, row=5, columnspan=5)
fenster.mainloop()

from tkinter import Tk, Label, Button, Entry, LEFT

def rechnen():
    ausdruck = eingabe.get()
    try:
        ergebnis = eval(ausdruck) # Eventhandler
    except:
        ergebnis = 'Ungültiger Ausdruck'
    ausgabe.config(text = ergebnis)

fenster = Tk()
fenster.title("Rechner")
button = Button(master=fenster, text='Rechnen', font=('Arial', 12), command=rechnen)        
ausgabe = Label(master=fenster, width=20, height=2, font=('Arial', 12))
eingabe = Entry(master=fenster, font=('Arial', 12))
ausgabe.pack()
eingabe.pack(side=LEFT, padx=5, pady=5)
button.pack(side=LEFT, padx=5, pady=5)
fenster.mainloop()

from time import sleep
from tkinter import *
from _thread import start_new_thread

def countdown():
    start_new_thread(zählen, ())

def zählen():
    for zahl in ['3', '2', '1', 'LOS!']:
        label.config(text=zahl)
        sleep(1)
    sleep(2)
    label.config(text='')

fenster = Tk()
fenster.title("Countdown")
label = Label(master=fenster, font=('Arial', 40), width=6)
button = Button(master=fenster, command=countdown, text=' Start ')
label.pack()
button.pack()
fenster.mainloop()            