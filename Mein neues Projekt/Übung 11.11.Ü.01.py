from tkinter import Tk, Label, Button, Entry

def button_ok():
    inhalt = entry.get()
    print(f"Eingegebener Text: {inhalt}")

def fenster_schließen():
    fenster.destroy()

fenster = Tk()
fenster.title("Mein erstes GUI-Programm")

label = Label(master=fenster, font=('Arial', 14), text='Willkommen zu meinem Programm', foreground='blue', background='yellow')
label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

entry = Entry(master=fenster, width=20)
entry.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

button = Button(master=fenster, text = 'OK', command=button_ok)
button.grid(row=2, column=0, padx=5, pady=5)

button_1 = Button(master=fenster, text = 'Abbrechen', command=fenster_schließen)
button_1.grid(row=2, column=1, padx=5, pady=5)

fenster.mainloop()