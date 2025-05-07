import lese_datei
import os 

adjektive_pfad = os.path.join(os.path.dirname(__file__), 'adjektive.txt')
nomen_pfad = os.path.join(os.path.dirname(__file__), 'nomen.txt')

adjektive = lese_datei.lese_datei(adjektive_pfad)
nomen = lese_datei.lese_datei(nomen_pfad)
print(adjektive)
print(nomen)