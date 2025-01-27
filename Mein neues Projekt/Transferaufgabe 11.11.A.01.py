from tkinter import Tk, Entry, Label, Button, Radiobutton, Text, StringVar, END
from datetime import datetime

def aktuelle_zeit_als_string():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def begruessung():
    name = entry.get()
    zeit = zeit_var.get()
    begruessungtext = f"{zeit}, {name}!"
    label.config(text=begruessungtext)
    log.insert(END, f"{aktuelle_zeit_als_string()}: {begruessungtext}\n")

fenster = Tk()
fenster.title("Begrüßung-App")

entry = Entry(fenster)
entry.grid(row=0, column=1, padx=10, pady=10)
#entry.pack()

label = Label(master=fenster, text = '', font=('Arial', 16))
label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
#label.pack()

button = Button(master=fenster, font=('Arial', 16), command=begruessung, text='Begrüßen')
button.grid(row=0, column=2, padx=10, pady=10)
#button.pack()

zeit_var = StringVar() # Kontrollvarialble für Radiobutton
zeit_var.set("Guten Tag")

Radiobutton(master=fenster, text="Guten Morgen", variable=zeit_var, value="Guten Morgen").grid(row=2, column=0)
Radiobutton(master=fenster, text="Guten Tag", variable=zeit_var, value="Guten Tag").grid(row=2, column=1)
Radiobutton(master=fenster, text="Guten Abend", variable=zeit_var, value="Guten Abend").grid(row=2, column=2)

log = Text(master=fenster, height=10, width=50)
log.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

fenster.mainloop()