# from tkinter import *
# from random import randint

# def wuerfeln():
#     global summe
#     text = label.cget('text')
#     zahl = randint(1, 6)
#     summe += zahl
#     label.config(text=text + '' + str(zahl))
#     if summe > 21:
#         label.config(bg='yellow')

# def loeschen():
#     global summe
#     summe = 0
#     label.config(text='', bg='white')

# summe = 0

# # Widgets

# fenster = Tk()
# bild_würfel = PhotoImage(file='wuerfel_logo.png')
# bild_löschen = PhotoImage(file='loeschen_logo.png')
# label = Label(master=fenster, font=('Arial', 30), width=16, text='', background='white')
# b_würfeln = Button(master=fenster, image=bild_würfel, command=wuerfeln)
# b_löschen = Button(master=fenster, image=bild_löschen, command=loeschen)

# # Layout

# label.pack()
# b_würfeln.pack(side=LEFT, padx=30, pady=10)
# b_löschen.pack(side=RIGHT, padx=30, pady=10)
# fenster.mainloop()

from tkinter import *

fenster = Tk()
fenster.title("Fläche gestalten")
canvas = Canvas(master=fenster, width=200, height=200, background='white')
nr = canvas.create_oval(50, 50, 150, 150, fill='blue', outline='')
no = canvas.create_line(0, 50, 100, 150, 200, 100, fill='black', width=6, smooth=True)

canvas.pack()
fenster.mainloop()

from canvasvg import saveall # muss vorher 'pip install canvasvg' in der Console eingeben 
from tkinter import *
from random import choice
from time import asctime

def neue_farbe():
    z = '0123456789ABCDEF'
    return '#' + choice(z) + choice(z) + choice(z)

def malen():
    global id0, id1, id2
    id0 = bild.create_rectangle(0,0,250,300, fill=neue_farbe(), outline='')
    id1 = bild.create_rectangle(100,0,150,300, fill=neue_farbe(), outline='')
    id2 = bild.create_rectangle(0,100,250,200, fill=neue_farbe(), outline='')

def löschen():
    bild.delete(id0)
    bild.delete(id1)
    bild.delete(id2)    

def speichern():
    zeitstempel=asctime()
    for ch in ':. ':
        zeitstempel = zeitstempel.replace(ch, '')
    saveall('bild'+zeitstempel+'.svg', bild)

fenster = Tk()
fenster.title("Creative Coding")
button_malen = Button(master=fenster, text='Malen', command=malen)
button_löschen = Button(master=fenster, text='Löschen', command=löschen)
button_speichern = Button(master=fenster, text='Speichern', command=speichern)

bild = Canvas(master=fenster, width=250, height=300)
bild.pack()
button_malen.pack(side=LEFT, padx=5, pady=5)
button_löschen.pack(side=LEFT, padx=5, pady=5)
button_speichern.pack(side=LEFT, padx=5, pady=5)
fenster.mainloop()

from tkinter import Label, Button, Tk
from urllib.request import urlopen
from PIL import Image, ImageTk # muss vorher 'pip install pillow' in der Console eingeben

URL = 'http://lamp01.dortmund.de/webcams/friedensplatz/current.jpg'

def neues_bild():
    global bild_tk
    stream = urlopen(URL)
    bild_pil = Image.open(stream)
    bild_tk = ImageTk.PhotoImage(bild_pil)
    label.config(image=bild_tk)

#FILE = 'foto.jpg'
fenster = Tk()
fenster.title("Image darstellen")
#im = Image.open(FILE)
# im = Image.new(mode='RGB', size=(200, 100), color=190)
# print(im.mode)
# im.show()

button = Button(master=fenster, font=('Arial', 20), text='Neues Bild', command=neues_bild)
button.pack(padx=10, pady=10)
label = Label(master=fenster)
label.pack()
neues_bild()
fenster.mainloop()