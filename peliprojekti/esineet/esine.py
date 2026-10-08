class Esine:
    def __init__(self, nimi, paino):
        self.nimi = nimi
        self.paino = paino

    def päivitys(inventori, hinta):
        if inventori[1].nimi == "Puu-Hakku":
            inventori[1].nimi = "Rauta-Hakku"
            inventori[1].paino = 10
            inventori[0]["määrä"] = inventori[0]["määrä"] - hinta

        elif inventori[1].nimi == "Rauta-Hakku":
            inventori[1].nimi = "Timantti-Hakku"
            inventori[1].paino = 100
            inventori[0]["määrä"] = inventori[0]["määrä"] - hinta

        else:
            print("\nPäivitys ei mahdollinen")