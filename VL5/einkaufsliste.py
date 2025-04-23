# Frage Benutzer, solange er ja sagt, nach Gegenständen
# Füge Gegenstände in ein Dictionary ein 
# Gib Dictionary, Keys, und Values aus 

mehr_gegenstaende = input("Gegenstand hinzufügen (ja|nein)")
einkaufsliste = {}
while mehr_gegenstaende != "nein":
    gegenstand = input("Gegenstand?")
    anzahl = int(input("Wie viele?"))
    einkaufsliste[gegenstand] = anzahl
    mehr_gegenstaende = input("Gegenstand hinzufügen (ja|nein)")

print("Dein Einkauf:", einkaufsliste)
print("Schlüssel: ", einkaufsliste.keys())
print("Werte: ", einkaufsliste.values())