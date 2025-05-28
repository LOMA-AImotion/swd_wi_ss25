import tkinter
from tkinter import messagebox
import functools

# Mockup-Fragen zum Testen
alle_fragen = [("Was ist 2+2?",["2", "3", "4", "5"], 2),
               ("Was ist 2+3?",["2", "3", "4", "5"], 3),
               ("Warum brauch ich partial?",["Um Argumente zu speichern", "Damit ich eine lokale Variable ersetzen kann", "Überhaupt nicht", "Mir egal"], 0)]
aktuelle_frage = 0
aktuell_richtige_antwort_index = -1 # sollte überschrieben werden!

def erzeuge_GUI() -> tkinter.Tk:
    haupt_fenster = tkinter.Tk()
    leinwand = tkinter.Canvas(haupt_fenster, width=600, height=400)
    leinwand.grid(row=0, column=0, columnspan=2, rowspan=4)

    # Label für die eigentliche Frage
    frage_label = tkinter.Label(haupt_fenster, text="DUMMY_TEXT")
    frage_label.grid(row=1, column=0, columnspan=2)
    frage_label.configure(font=("Arial 14"))

    def button_geklickt(button_id: int):
        print(f"Button {button_id} geklickt")
        # Wenn ich hier nicht global schreibe, denkt Python, dass ich eine neue *lokale* Variable
        # aktuelle_frage schreiben möchte - und die ist noch nicht definiert
        global aktuelle_frage
        # das wird ein Grund für OOP ... 

        # wenn richtig
        if button_id == aktuell_richtige_antwort_index:
            messagebox.showinfo("Richtig!", "Antwort korrekt!")
            #   ziehe nächste Frage -> aktuelle_frage += 1

            # ich rechne modulo len(alle_fragen) damit ich nach dem Ende wieder vorne anfange
            aktuelle_frage = (aktuelle_frage + 1) % len(alle_fragen)
            # bei len(alle_fragen) brauche ich kein global, weil ich nur lese!
            #   beschrifte Widgets neu
            beschrifte_neu()    
        else:
            messagebox.showerror("Falsch!", "Probier's nochmal")

    def beschrifte_neu():
        global aktuell_richtige_antwort_index
        nächste_frage = alle_fragen[aktuelle_frage]
        frage, alternativen, korrekter_index = nächste_frage
        frage_label.config(text=frage)
        aktuell_richtige_antwort_index = korrekter_index
        # Antwortalternativen an Buttons zuweisen:
        for index, alternative in enumerate(alternativen):
            buttons[index].config(text=alternative)

    # erzeuge 4 Buttons # hätten wir auch über zwei For-Schleifen über Zeilen und Spalten hinbekommen
    buttons = []
    for i in range(4):
        spalte = i % 2 # gerade Zahlen linke Spalte, ungerade rechte Spalte
        if i <= 1:
            zeile = 0
        else:
            zeile = 1
        # zeile = i // 2 (Ganzzahldivision)
        neuer_button = tkinter.Button(haupt_fenster, text=i)
        neuer_button.grid(row = zeile+2, column=spalte)
        neuer_button.config(command=functools.partial(button_geklickt, i))
        buttons.append(neuer_button)

    beschrifte_neu()
    return haupt_fenster

# mit den Mockup-Fragen nur im Test-Modus (Wenn dieses Modul thi_quiz_gui gestartet wird)
if __name__ == "__main__":
    haupt_fenster = erzeuge_GUI()
    haupt_fenster.mainloop()