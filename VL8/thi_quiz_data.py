# -*- coding: utf-8 -*-
"""
thi_quiz_data.py

Created on Tue Nov 23 22:27:53 2021

@author: 
"""
def lese_datei(datei_name:str) -> list:
    with open(datei_name, encoding="utf-8") as f:
        zeilen = f.read().splitlines()
    return zeilen

ANZAHL_FRAGEN = 4
def lade_fragen(datei_name: str) -> list:
    zeilen = lese_datei(datei_name)
    anz_fragen = int(zeilen[0])
    liste_fragen = []

    lese_index = 1
    # frage_index wird nicht benutzt -> man könnte _ nehmen
    for frage_index in range(anz_fragen):
        frage = zeilen[lese_index]
        lese_index += 1
        alternativen = []
        # setze auf -1, damit wir überprüfen können, ob korrekter_index wirklich neu gesetzt wurde
        korrekter_index = -1 

        # besser noch: In Funktion auslagern -> kognitive Belastung
        for alternative_index in range(ANZAHL_FRAGEN):
            alternative = zeilen[lese_index]
            if "CORRECT:" in alternative:
                korrekter_index = alternative_index
                alternative = alternative.replace("CORRECT:", "")
            alternativen.append(alternative)
            lese_index += 1

        # In der Realität: Prüfen ob korrekter_index nicht -1 ist!
        liste_fragen.append( (frage, alternativen, korrekter_index) )
    
    return liste_fragen