# Erstelle einen 3x3 Ziffernblock für Buttons von 1 bis 9
import tkinter as tk
import tkinter.messagebox as msg 
from functools import partial

# Hauptfenster
haupt_fenster = tk.Tk() 
# erstelle ein Canvas mit 3x3 
leinwand = tk.Canvas(haupt_fenster, width=200, height=200)
leinwand.grid(row=0, column=0, rowspan=3, columnspan=3)

def callback(ziffer: int):
    msg.showinfo("THI WI - SWD", f"Ziffer {ziffer} gedrückt")

aktuelle_ziffer = 1
for zeilenindex in range(3):
    for spaltenindex in range(3):
        neuer_button = tk.Button(haupt_fenster)
        neuer_button.config(command = partial(callback, aktuelle_ziffer))
        neuer_button.config(width=10, height=5)
        neuer_button.config(text = aktuelle_ziffer)
        neuer_button.grid(row=zeilenindex, column=spaltenindex)
        aktuelle_ziffer += 1

haupt_fenster.mainloop()