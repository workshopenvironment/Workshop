from tkinter import Tk, Label, Button

def button_geklickt():
    label.config(text='Button wurde geklickt!')

fenster = Tk()
fenster.title("Mein GUI")
fenster.resizable(False, False) # Fenster kann vom Benutzer nicht vergrößern oder verkleinern
label = Label(master=fenster, font=('Arial', 16), foreground='blue', text = 'Willkommen zu deinem GUI', background='yellow')
button = Button(master=fenster, text='Klick mich!', command=button_geklickt)
label.pack(pady=20)
button.pack(pady=10)
fenster.mainloop() #Endlossschleife zur Anzeige des Fensters