import tkinter as tk
import pwgen

haupt = tk.Tk()
leinwand = tk.Canvas(haupt, width=500, height=300)
leinwand.grid(row=0, column=0, rowspan=2, columnspan=1)

pwgen_button = tk.Button(haupt, text="Generiere Passwort")
pwgen_button.grid(row=0, column=0)

pwlabel = tk.Label(haupt, text="Generiertes Password:")
pwlabel.grid(row=1, column=0)

def gen_passwort_UI():
    pw = pwgen.ziehe_passwort()
    pwlabel.config(text=f"Generiertes Passwort:{pw}")    
pwgen_button.config(command=gen_passwort_UI)

haupt.mainloop()