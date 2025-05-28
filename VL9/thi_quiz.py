# -*- coding: utf-8 -*-
"""
thi_quiz.py

Created on Tue Nov 23 22:27:53 2021

@author: 
"""

import thi_quiz_data
import thi_quiz_gui

# Lade Fragen aus einer Datei von Datenschicht, ich erwarte eine Liste von Tupel
quiz_datei = "quiz_functions.txt"
import os
quiz_datei = os.path.join(os.path.dirname(__file__), quiz_datei)
#print(os.path.dirname(__file__))
#print(quiz_datei)
alle_fragen = thi_quiz_data.lade_fragen(quiz_datei)
print("In Main: ", alle_fragen)

# Setze die Fragen in thi_quiz_gui auf die geladenen
thi_quiz_gui.alle_fragen = alle_fragen

# Starte GUI
haupt_fenster = thi_quiz_gui.erzeuge_GUI()
haupt_fenster.mainloop()
# Zeige die gewählte Frage in der GUI
