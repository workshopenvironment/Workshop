from tkinter import Tk, Label, Button, Radiobutton, StringVar, filedialog, Text, WORD
from threading import Thread


def datei_hochladen():
    pfad = filedialog.askopenfilename()
    stream = open(pfad, encoding='utf-8')
    text.insert(1.0, stream.read())
    stream.close()

def bestaetigen():
    wahl = var.get()
    if wahl == "Äpfel":
        label.config(text="Äpfel")
    elif wahl == "Bananen":
        label.config(text="Bananen")
    elif wahl == "Orangen":
        label.config(text="Orangen") 
                   
def schliessen():
    fenster.destroy()

fenster = Tk()
fenster.title("Obstauswahl und Dateiöffner")

text = Text(master=fenster, width=40, height=10, wrap=WORD, font=('Arial', 10))
text.grid(row=2, column=1, padx=15, pady=15)

label = Label(master=fenster, font=('Arial', 16), background='white', width=15, text='')
label.grid(row=0, column=1, padx=15, pady=15)

var = StringVar()
var.set("Äpfel")

Radiobutton(master=fenster, text="Äpfel", variable=var, value="Äpfel").grid(row=1, column=0)
Radiobutton(master=fenster, text="Bananen", variable=var, value="Bananen").grid(row=1, column=1)
Radiobutton(master=fenster, text="Orangen", variable=var, value="Orangen").grid(row=1, column=2)

button = Button(master=fenster, font=('Arial', 16), command=bestaetigen, text='Bestätigen')
button.grid(row=3, column=0, padx=5, pady=5)

button_laden = Button(master=fenster, font=('Arial', 16), command=datei_hochladen, text="Laden")
button_laden.grid(row=3, column=1, padx=5, pady=5)

button_1 = Button(master=fenster, font=('Arial', 16), command=schliessen, text="Schließen")
button_1.grid(row=3, column=2, padx=5, pady=5)

fenster.mainloop()

# andere Möglichkeit mit Thread

import tkinter as tk
from tkinter import filedialog
from threading import Thread

def datei_laden():
    def laden():
        pfad = filedialog.askopenfilename()
        if pfad:
            with open(pfad, "r", encoding="utf-8") as file:
                text = file.read()
                text_widget.delete('1.0', tk.END)
                text_widget.insert('1.0', text)
    thread = Thread(target=laden)
    thread.start()

def auswahl_anzeigen():
    ausgewaehlte_obstsorte = obst_var.get()
    auswahl_label.config(text="Ausgewählt: " + ausgewaehlte_obstsorte)

fenster = tk.Tk()
fenster.title("Obstauswahl und Dateiöffner")

obst_var = tk.StringVar()
radiobuttons = [("Äpfel", "Äpfel"), ("Bananen", "Bananen"), ("Orangen", "Orangen")]
for obst, value in radiobuttons:
    rb = tk.Radiobutton(fenster, text=obst, variable=obst_var, value=value, command=auswahl_anzeigen)
    rb.pack(anchor=tk.W)

auswahl_label = tk.Label(fenster, text="Bitte wähle eine Obstsorte.")
auswahl_label.pack()

oeffnen_button = tk.Button(fenster, text="Datei öffnen", command=datei_laden)
oeffnen_button.pack()

text_widget = tk.Text(fenster, height=10, width=50)
text_widget.pack()

schliessen_button = tk.Button(fenster, text="Schließen", command=fenster.destroy)
schliessen_button.pack()

fenster.mainloop()




