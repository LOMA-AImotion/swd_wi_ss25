import tkinter
haupt_fenster = tkinter.Tk()
haupt_fenster.title("SWD WI SS25")
leinwand = tkinter.Canvas(haupt_fenster, width=600, height=300)
leinwand.grid(row=0, column=0, columnspan=2, rowspan=4)

label = tkinter.Label(haupt_fenster, text="Servus WI")
label.grid(row=0, column=0)

button = tkinter.Button(haupt_fenster, text="OK")
button.grid(row=1, column=1)

haupt_fenster.mainloop()