from tkinter import Tk, messagebox, Label, Button, Radiobutton, StringVar, IntVar, filedialog
import json, time, os

class QuizApp():
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")

        self.question_index = 0
        self.correct_answers = 0
        self.timer = 30 # Timer in Seconds
        self.timer_running = False
        self.ergebnisse = "results.json"

        # Example questions and answers
        self.questions = [
            {"question": "Was ist die Hauptstadt von Kamerun?", "options": ["Yamoussokro", "Casablanca", "Jaunde", "Akkra"], "answer": 2},
            {"question": "Bis wann muss das Baby gestillt werden?", "options": ["12 Monaten", "5 Monaten", "5 Jahren", "30 Tagen"], "answer": 1},
            {"question": "Wie alt bist du?", "options": ["25", "67", "32", "15"], "answer": 1},
            {"question": "Welches der folgenden Konzepte ist ein Teilgebiet der Künstlichen Intelligenz?", "options": ["Relativitätstheorie", "Maschinelles Lernen", "Quantenmechanik", "Astronomie"], "answer": 1},
        ]

        # Question Label
        self.question_label = Label(self.root, text="", wraplength=400, font=('Arial', 14), justify='center')
        self.question_label.pack(pady=20)

        # Options (Radiobuttons)
        self.selected_option = IntVar()
        self.option_buttons = []
        for i in range(4):
            btn = Radiobutton(self.root, text="", variable=self.selected_option, value=i, font=('Arial', 12))
            btn.pack(anchor="w", padx=20, pady=5)
            self.option_buttons.append(btn)

        # Timer label
        self.timer_label = Label(self.root, text=f"Time left: {self.timer} s", font=('Arial', 12), foreground='red')
        self.timer_label.pack(pady=10)

        # Buttons
        self.next_button = Button(self.root, text="Nächste Frage", command=self.next_question, font=('Arial', 12))
        self.next_button.pack(pady=10)

        self.save_button = Button(self.root, text="Ergebnisse Speichern", command=self.save_results, font=('Arial', 12))
        self.save_button.pack(pady=10)

        self.load_button = Button(self.root, text="Datei laden", command=self.load_file, font=('Arial', 12))
        self.load_button.pack(pady=10)

        self.load_question()
        self.start_timer()

    def load_question(self):
        if self.question_index < len(self.questions):
            question_data = self.questions[self.question_index]
            self.question_label.config(text=question_data["question"])
            for  i, option in enumerate(question_data["options"]):
                self.option_buttons[i].config(text=option)
            self.selected_option.set(-1) # Reset selection
            #self.reset_timer()
        else:
            self.end_quiz()

    def start_timer(self):
        self.timer_running = True
        self.update_timer()

    def update_timer(self):
        if self.timer > 0:
            self.timer -= 1
            self.timer_label.config(text=f"Time left:  {self.timer} s")
            self.root.after(1000, self.update_timer)
        else:
            self.timer_running = False
            self.next_question()    

    def next_question(self):
        if self.selected_option.get() == -1:
            messagebox.showwarning("Warnung", "Bitte wählen Sie eine Antwort!")
            return

        correct_answer = self.questions[self.question_index]["answer"]
        if self.selected_option.get() == correct_answer:
            self.correct_answers += 1

        self.question_index += 1
        self.timer =  30 # Reset timer
        self.load_question()

    def save_results(self):
        results = {
            "Anzahl_Fragen": len(self.questions),
            "Korrekte_Antworten": self.correct_answers
        }
        try:
            with open(self.ergebnisse, "w") as datei:
                json.dump(results, datei, ensure_ascii=False, indent=4)
            messagebox.showinfo("Ergebnisse gespeichert", "Ihre Ergebnisse wurden in der Datei 'results.json' gespeichert!")
        except FileNotFoundError:
            messagebox.showwarning("Die Datei 'results.json' wurde nicht gefunden.")
        except Exception as e:
            messagebox.showerror(f"Ein Fehler beim Speichern der Datei ist aufgetreten: {e}")

    def load_file(self):
        if os.path.exists(self.ergebnisse):
            try:
                with open(self.ergebnisse, 'r') as datei:
                    letzte_ergebnisse = json.load(datei)
                messagebox.showinfo("Letzte Ergebnisse", f"Frühere Ergebnisse wurden geladen:\n{letzte_ergebnisse}")
            except FileNotFoundError:
                messagebox.showwarning("Die Datei 'results.json' wurde nicht gefunden.")    
            except Exception as e:
                messagebox.showerror(f"Ein Fehler beim Laden der Datei ist aufgetreten: {e}")        

    def end_quiz(self):
        messagebox.showinfo("Quiz zu Ende", f"Sie haben {self.correct_answers}/{len(self.questions)} erfolgreich geantwortet!")                                                    
        self.root.quit()            

if __name__ == "__main__":
    root = Tk()
    app = QuizApp(root)
    root.mainloop()        

