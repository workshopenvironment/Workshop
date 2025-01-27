from tkinter import Tk, Label, Entry, Button

def loesche_text():
    entry.delete(0, 'end')

def schliesse_fenster():
    fenster.destroy()    

fenster = Tk()
fenster.title("Meine erste Grafische Benutzeroberfläche")
label = Label(master=fenster, font=('Arial', 14), text="Hallo Welt!", foreground='blue')
entry = Entry(fenster)
label.pack()
entry.pack()

buttons = [("Text löschen", loesche_text), ("Fenster schließen", schliesse_fenster)]

for text, funktion in buttons:
    button = Button(master=fenster, command=funktion, text=text)
    button.pack(side='bottom', pady=5)

fenster.mainloop()