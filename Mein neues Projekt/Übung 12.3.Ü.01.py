from tkinter import Tk, Label, Button, Radiobutton, StringVar, Canvas

def button_geklickt():
    label.config(text="Button wurde geklickt!")

def auswahl_anzeigen(farbe):
    label.config(background=farbe)   

fenster = Tk()
fenster.title("Mein GUI-Programm")

label = Label(master=fenster, font=('Arial', 16), text='Hallo Welt!')
label.pack()
#label.grid(row=0, column=1, padx=5, pady=5)

button = Button(master=fenster, font=('Arial', 16), command=button_geklickt, text="Button")
button.pack()
#button.grid(row=1, column=1, padx=5, pady=5)

var = StringVar()
var.set("Rot")
radiobutton = Radiobutton(master=fenster, text="Rot", variable=var, value="red", command=lambda: auswahl_anzeigen("red"))
radiobutton_1 = Radiobutton(master=fenster, text="Blau", variable=var, value="blue", command=lambda: auswahl_anzeigen("blue"))
radiobutton.pack()
radiobutton_1.pack()
#radiobutton.grid(row=2, column=0, padx=5, pady=5)
#radiobutton_1.grid(row=2, column=1, padx=5, pady=5)

canvas = Canvas(master=fenster, width=200, height=200, background='white')
nr = canvas.create_oval(50, 50, 150, 150, fill='blue', outline='')
no = canvas.create_line(0, 50, 100, 50, 200, 150, fill='lightgrey', smooth=True, width=6)
#canvas.grid(row=3, column=1, padx=5,pady=5)
canvas.pack()

fenster.mainloop()