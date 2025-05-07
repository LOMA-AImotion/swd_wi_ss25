import tkinter as tk
import tkinter.messagebox as msg

def sag_servus():
    msg.showerror("WI", "Servus WI")
    btn.config(text="Schönen Tag noch")
    #print("Servus auf die Konsole")
    # kein return benötigt

haupt = tk.Tk()
btn = tk.Button(haupt, text="Sag Servus", command = sag_servus)
btn.pack()

haupt.mainloop()