import lese_datei
import random
import os 

adjektive_pfad = os.path.join(os.path.dirname(__file__), 'adjektive.txt')
nomen_pfad = os.path.join(os.path.dirname(__file__), 'nomen.txt')

adjektive = lese_datei.lese_datei(adjektive_pfad)
nomen = lese_datei.lese_datei(nomen_pfad)

def ziehe_passwort():
    adjektiv = random.choice(adjektive)
    gew_nomen = random.choice(nomen)
    zahl = random.randint(0, 100)
    sonderzeichen = random.choice("*?-/%&#~§")
    passwort = adjektiv + gew_nomen + str(zahl) + sonderzeichen
    return passwort


if __name__ == "__main__": # wird nur ausgeführt, wenn ich pwgen.py *direkt* ausführe
    print(ziehe_passwort())