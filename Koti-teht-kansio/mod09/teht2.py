class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, nopeuden_muutos):
        uusi_nopeus = self.nopeus + nopeuden_muutos

        if uusi_nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.nopeus = 0
        else:
            self.nopeus = uusi_nopeus


uusi_auto = Auto("ABC-123", 142)

print(f"Rekisteritunnus: {uusi_auto.rekisteritunnus}")
print(f"Huippunopeus: {uusi_auto.huippunopeus} km/h")
print(f"Tämänhetkinen nopeus: {uusi_auto.nopeus} km/h")
print(f"Kuljettu matka: {uusi_auto.kuljettu_matka} km")
print("-" * 30)

uusi_auto.kiihdyta(30)
uusi_auto.kiihdyta(70)
uusi_auto.kiihdyta(50)

print(f"Nopeus kiihdytysten jälkeen: {uusi_auto.nopeus} km/h")

uusi_auto.kiihdyta(-200)

print(f"Nopeus hätäjarrutuksen jälkeen: {uusi_auto.nopeus} km/h")