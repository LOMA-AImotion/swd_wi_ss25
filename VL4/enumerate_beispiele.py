angestellte = [("Hans", "Müller", 21), ("Peter", "Schmidt", 22), ("Anna", "Meier", 23)]
# this works
for i, (vorname, nachname, alter) in enumerate(angestellte):
    print(f"{i}: {vorname} {nachname} ({alter})")

for index, value in enumerate(angestellte):
    print(f"{value}")

for index, value in enumerate(angestellte):
    print(f"Angestellter #{index+1}{value}")

for index, value, vorname in enumerate(angestellte):
    print(f"{index}")
