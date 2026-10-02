class Lentokone:
    def __init__(self, nimi, id, bensatankin_maksimi = 100.0, bensatankin_nykyinen = 0.0):
        self.nimi = nimi
        self.id = id
        self.bensatankin_maksimi = bensatankin_maksimi
        self.bensatankin_nykyinen = bensatankin_nykyinen

    def tankkaa(self):
        mahtui = self.bensatankin_maksimi - self.bensatankin_nykyinen
        self.bensatankin_nykyinen = self.bensatankki_maksimi
        print(f"Tankki täytettiin. Bensaa mahtui {mahtui:.1f} litraa.")

    def tulosta_tiedot(self):
        print(f"nimi: {self.nimi}")
        print(f"id: {self.id}")
        print(f"bensatankki: {self.bensatankin_nykyinen:.1f} {self.bensatankin_maksimi:.1f} ")

class Lentokenttä:
    def __init__(self, nimi, id, lentokoneet=None):
        self.nimi = nimi
        self.id = id
        self.lentokoneet = lentokoneet if lentokoneet is not None  else []

    def tulosta_koneet(self):
        print(f"Lentokentän {self.nimi} (ID: {self.id}) lentokoneet:")
        if not self.lentokoneet:
            print("  Ei lentokoneita kentällä.")
        else:
            for kone in self.lentokoneet:
                kone.tulosta_tiedot()
                print("")
