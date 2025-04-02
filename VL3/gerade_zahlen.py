# Frage nach einer Zahl k
# Zähle von 1 bis k (k inklusive)
# Gebe nur die geraden Zahlen aus 

k = int(input("Gebe Zahl k ein:"))

for i in range(1, k+1):
    # prüfe ob die Zahl gerade ist
    if i % 2 == 0:
        print(i)