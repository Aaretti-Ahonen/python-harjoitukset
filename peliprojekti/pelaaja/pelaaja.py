from peliprojekti import inventori, random, Hakku

class Pelaaja:
    def __init__(self, nimi, sijainti):
        self.nimi = nimi
        self.sijainti = sijainti
        self.esineet = []

    def liikkuminen(self, liiku):
        self.liiku = liiku

    def kaiva(self):
        if self.osoite == "kaivos":
            inventori['Kivi'] = inventori['Kivi'] + 1 * random.randint(1,10) * Hakku['Arvo']
            print(f"Sinulla on nyt{inventori['Kivi']} Kiveä.")
        else: 
            print("Täällä ei voi kaivaa")