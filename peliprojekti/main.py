from esineet import Esine
from pelaaja import Pelaaja
from maailma import Osoite

inventori = [
    {"nimi": "Kivi", "määrä": 0},
    Esine("Puu-Hakku", 1)
]

def kerro_tutoriaali(nimi):
    print(f"\n> Pelaaja {nimi}, sinun tarkoituksesi on päivittää hakkusi timanttiseksi, jotta pääset takaisin maanpinnalle.")

nimi = input('Oma Nimi: ')
ikä = int(input('Oma Ikä: '))

print(f"Pelaaja: {nimi}.\nIkä: {ikä}-Vuotta.")

if ikä < 12:
    print("Olet alaikäinen, ohjelma suljetaan.")

else:
    kerro_tutoriaali(nimi)

    pelaaja = Pelaaja(nimi, Osoite("kaivos"))
    pelaaja.esineet = inventori

    while True:

        if pelaaja.sijainti.osoite == "kaivos":
            print("\n--- KAIVOS ---\n")
            print("1. kaiva     - Kaiva kiveä")
            print("2. kauppa    - Mene kauppaan")
            print("3. inventori - Katso inventori")
            print("4. lopeta    - Lopeta peli")

        elif pelaaja.sijainti.osoite == "kauppa":
            print(f"\n--- KAUPPA ---\n\nNykyinen hakku: {inventori[1].nimi}\n\nSinulla on {inventori[0]['määrä']} kiveä.\n")

            if inventori[1].nimi == "Puu-Hakku":
                print("1. päivitä   - Rauta-Hakku (25 kiveä)")
                print("2. kaivos    - Palaa kaivokseen")
                print("3. inventori - Katso inventori")
                print("4. lopeta    - Lopeta peli")

            elif inventori[1].nimi == "Rauta-Hakku":
                print("1. päivitä   - Timantti-Hakku (250 kiveä)")  
                print("2. kaivos    - Palaa kaivokseen")
                print("3. inventori - Katso inventori")
                print("4. lopeta    - Lopeta peli")

            else:
                print("1. pakene    - Pakene kaivoksesta (3000 kiveä)")
                print("2. kaivos    - Palaa kaivokseen")
                print("3. inventori - Katso inventori")
                print("4. lopeta    - Lopeta peli")


        komento = input("\nSyötä komento: ").strip().lower()

        if komento == "kaivos" and pelaaja.sijainti.osoite == "kauppa":
            pelaaja.liikkuminen(Osoite("kaivos"))

        elif komento == "kauppa" and pelaaja.sijainti.osoite == "kaivos":
            pelaaja.liikkuminen(Osoite("kauppa"))

        elif komento == "kaiva":
            pelaaja.kaiva()

        elif komento == "päivitä":
            pelaaja.päivitä()

        elif komento == "inventori":
            print("\n INVENTORI ")
            print(f"- {inventori[0]['nimi']}: {inventori[0]['määrä']}")
            print(f"- {inventori[1].nimi}")

        elif komento == "lopeta":
            print("\nLopetit pelin.")
            break

        elif komento == "pakene" and pelaaja.sijainti.osoite == "kauppa" and inventori[1].nimi == "Timantti-Hakku" and inventori[0]["määrä"] >= 3000:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nOnnistuit pakenemaan maanpinnalle!")
            print("Voitit pelin!\n\n\n\n")
            break

        else:
            print("\nTuntematon komento. Yritä uudelleen.")