import tkinter
import functools

haupt_fenster = tkinter.Tk()
leinwand = tkinter.Canvas(haupt_fenster, width=600, height=400)
leinwand.grid(row=0, column=0, columnspan=2, rowspan=4)

# Label für die eigentliche Frage
frage_label = tkinter.Label(haupt_fenster, text="Was ist 2+2?")
frage_label.grid(row=1, column=0, columnspan=2)
frage_label.configure(font=("Arial 14"))

def button_geklickt(button_id: int):
    print(f"Button {button_id} geklickt")

# erzeuge 4 Buttons # hätten wir auch über zwei For-Schleifen über Zeilen und Spalten hinbekommen
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

haupt_fenster.mainloop()