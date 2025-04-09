max_kapazität = 10
aktuelle_belegung = 0

while aktuelle_belegung <= max_kapazität:
    print(f">>> Info: aktuelle Belegung: {aktuelle_belegung}")
    name = input("Hallo, wie ist dein Name? ")
    gewünscht = int(input("Wie viele Plätze möchtest du reservieren? "))
    
    noch_frei = max_kapazität - aktuelle_belegung
    
    if gewünscht < noch_frei:

        aktuelle_belegung = aktuelle_belegung + gewünscht
        # aktuelle_belegung += gewünscht  -> äquivalent zu Z. 12
        print("Passt, wir freuen uns auf deinen Besuch!")  
    else: 
        print("Sorry, leider keine Plätze mehr frei :(")
