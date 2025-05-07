def lese_datei(dateiname:str) -> list:
    with open(dateiname, encoding="utf-8") as f:
        zeilen = f.read().splitlines()
    return zeilen