import random
from esineet import Esine

class Pelaaja:
    def __init__(self, nimi, sijainti):
        self.nimi = nimi
        self.sijainti = sijainti
        self.esineet = []

    def liikkuminen(self, liiku):
        self.sijainti = liiku

    def kaiva(self):
        if self.sijainti.osoite == "kaivos":
            self.esineet[0]["määrä"] = self.esineet[0]["määrä"] + random.randint(1, 10) * self.esineet[1].paino
            print(f"Sinulla on nyt {self.esineet[0]['määrä']} kiveä.")
        else:
            print("Täällä ei voi kaivaa.")

    def päivitä(self):
            if self.esineet[1].nimi == "Puu-Hakku":
                hinta = 25

            elif self.esineet[1].nimi == "Rauta-Hakku":
                hinta = 250

            else:
                print("Päivitys ei mahdollinen")
                return

            if self.sijainti.osoite == "kauppa" and self.esineet[0]["määrä"] >= hinta:
                Esine.päivitys(self.esineet, hinta)

            else:
                print("Ei tarpeeksi kiveä.")