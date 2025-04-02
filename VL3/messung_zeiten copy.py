# Nimm eine Liste von Messzeitpunkten,
# z.B. [0, 1, 4, 5, 7, 8]
# bilde mit einer List-Comprehension die Liste der Differenzen
# [1, 3, 1, 2, 1]

# i
zeiten = [0, 1, 4, 5, 7, 8]
# zeiten[i+1] - zeiten[i]
mess_differenzen = [zeiten[i] - zeiten[i-1] for i in range(0, len(zeiten) )]
print(mess_differenzen)