# Frage vom Nutzer eine Zahl k ab
# Generiere von 1 bis k, Tupel der Form (1, "x"), (2, "xx") ... 
# Speichere alles in einer Menge / (einem Set)

k = int(input("Gib ein k ein:"))

# Variante 1: Set schrittweise aufbauen
menge = set() # das Gleiche wie set([]), {} wäre hier ein Dict ...
for i in range(1, k+1):
    naechstes_tupel = (i, "x"*i)
    menge.add(naechstes_tupel) # nicht append, da Mengen keine seq. Datentypen

print(menge)

# Variante 2: Set-Comprehension wie List-Comprehension
menge2 = { (i, i*"x") for i in range(1, k+1)}
print(menge2)