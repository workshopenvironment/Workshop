from tkinter import Tk, Label, Button, Radiobutton, StringVar, Canvas

def name_aendern():
    inhalt = var.get()
    label.config(text=f"Ausgewählte Farbe: {inhalt}")
    canvas.config(background=inhalt)

# def name_aendern():
#     inhalt = var.get()
#     text = 'Wähle deine Lieblingsfarbe'
#     nachricht = f"{text} : {inhalt}"
#     label.config(text=nachricht)
#     canvas.config(background=inhalt)

fenster = Tk()
fenster.title("Farben ändern")

label = Label(master=fenster, font=('Arial',20), text='Wähle deine Lieblingsfarbe:', background='White')
label.grid(row=0, column=0, columnspan=3, padx=15, pady=15) # columnspan = 2 Label, das sich über zwei Spalten erstesckt

var = StringVar()
var.set("Blue")
radiobutton_1 = Radiobutton(master=fenster, text="Rot", variable=var, value="Red").grid(row=1, column=0, columnspan=1)
radiobutton_2 = Radiobutton(master=fenster, text="Grün", variable=var, value="Green").grid(row=1, column=1, columnspan=1)
radiobutton_3 = Radiobutton(master=fenster, text="Blau", variable=var, value="Blue").grid(row=1, column=2, columnspan=1)

button = Button(master=fenster, font=('Arial', 20), text="Bestätigen", command=name_aendern)
button.grid(row=2, column=1, padx=5, pady=5)

canvas = Canvas(master=fenster, width=200, height=150, background='white')
canvas.grid(row=3, column=1, padx=5, pady=5)

fenster.mainloop()