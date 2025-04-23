def flaeche(breite : int, hoehe : int) -> int:
    """berechnet den Flächeninhalt eines Rechtecks

    Args:
        breite (int): die Breite des Rechtecks
        hoehe (int): die Höhe des Rechtecks

    Returns:
        int: den Flächeninhalt
    """
    print("In Funktion Fläche")
    # print(breite*hoehe)  <- so nicht in der Klausur
    return breite*hoehe

print("In Hauptprogramm")
a = flaeche(5, 10)
print(f"Außerhalb wieder: Fläche = {a}")