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
print(os.path.dirname(__file__))
print(quiz_datei)
fragen = thi_quiz_data.lade_fragen(quiz_datei)
print("In Main: ", fragen)
# Ziehe eine Frage daraus
# Starte GUI
# Zeige die gewählte Frage in der GUI
