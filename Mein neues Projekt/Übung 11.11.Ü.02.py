from tkinter import Tk, Label, Button, Entry, Radiobutton, StringVar

def farbe_aendern():
    wahl = var.get()
    if wahl == 'A':
        fenster.config(background='red')
    elif wahl == 'B':
        fenster.config(background='green')
    elif wahl == 'C':
        fenster.config(background='blue')        

def zuruecksetzen():
    fenster.config(background='SystemButtonFace')
    var.set(None)

#def abbrechen():
#    fenster.destroy()    

fenster = Tk()
fenster.title("Farbwahl Quiz")
#fenster.geometry("800x500") # Größe des Fensters
var = StringVar() # alle Radiobutton am Anfang sind ausgewählt ???
var.set("B") # nimmt per default die Value von radiobutton 'B'

Radiobutton(master=fenster, text="Rot", variable=var, value='A').grid(row=1, column=0, pady=5)
Radiobutton(master=fenster, text="Grün", variable=var, value='B').grid(row=1, column=1, pady=5)
Radiobutton(master=fenster, text="Blau", variable=var, value='C').grid(row=1, column=2, pady=5)

button = Button(master=fenster, text="Bestätigen", font=('Arial', 16), command=farbe_aendern)
button.grid(row=3, column=0, padx=10, pady=10)

button_1 = Button(master=fenster, text="Zurücksetzen", font=('Arial', 16), command=zuruecksetzen)
button_1.grid(row=3, column=1, padx=50, pady=10)

#button_2 = Button(master=fenster, text="Abbrechen", font=('Arial', 16), command=abbrechen)
#button_2.grid(row=3, column=2, padx=30, pady=30)

fenster.mainloop()