import random
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

    pelaaja = Pelaaja(nimi, Osoite("pääalue"))
    pelaaja.esineet = inventori

    while True:
         
        if pelaaja.sijainti.osoite == "pääalue":
            print("\n--- PÄÄALUE ---")
            print("1. kaivos    - Mene kaivokselle")
            print("2. kauppa    - Mene kauppaan")
            print("3. inventori - Katso inventori")
            print("4. lopeta    - Lopeta peli")

        elif pelaaja.sijainti.osoite == "kaivos":
            print("\n--- KAIVOS ---")
            print("1. kaiva     - Kaiva kiveä")
            print("2. pääalue   - Palaa pääalueelle")
            print("3. inventori - Katso inventori")
            print("4. lopeta    - Lopeta peli")

        elif pelaaja.sijainti.osoite == "kauppa":
            print(f"\n--- KAUPPA ---\n\nNykyinen hakku: {inventori[1].nimi}\n\nSinulla on {inventori[0]['määrä']} kiveä.\n")

            if inventori[1].nimi == "Puu-Hakku":
                print("1. päivitä   - Rauta-Hakku (25 kiveä)")
                print("2. pääalue   - Palaa pääalueelle")
                print("3. inventori - Katso inventori")
                print("4. lopeta    - Lopeta peli")

            elif inventori[1].nimi == "Rauta-Hakku":
                print("1. päivitä   - Timantti-Hakku (250 kiveä)")  
                print("2. pääalue   - Palaa pääalueelle")
                print("3. inventori - Katso inventori")
                print("4. lopeta    - Lopeta peli")

            else:
                print("1. pakene    - Pakene kaivoksesta (3000 kiveä)")
                print("2. pääalue   - Palaa pääalueelle")
                print("3. inventori - Katso inventori")
                print("4. lopeta    - Lopeta peli")


        komento = input("\nSyötä komento: ").strip().lower()

        if komento == "kaivos" and pelaaja.sijainti.osoite == "pääalue":
            pelaaja.liikkuminen(Osoite("kaivos"))

        elif komento == "kauppa" and pelaaja.sijainti.osoite == "pääalue":
            pelaaja.liikkuminen(Osoite("kauppa"))

        elif komento == "pääalue":
            pelaaja.liikkuminen(Osoite("pääalue"))

        elif komento == "kaiva":
            pelaaja.kaiva()

        elif komento == "päivitä":
            pelaaja.päivitä()

        elif komento == "inventori":
            print("\n INVENTORI ")
            print(f"- {inventori[0]['nimi']}: {inventori[0]['määrä']}")
            print(f"- {inventori[1].nimi}")

        elif komento == "lopeta":
            print("Lopetit pelin.")
            break

        elif komento == "pakene" and pelaaja.liikkuminen(Osoite("kauppa")) and inventori[1].nimi == "Timantti-Hakku" and inventori[0]["määrä"] >= 3000:
            print("\nOnnistuit pakenemaan maanpinnalle!")
            print("Voitit pelin!")
            break

        else:
            print("\nTuntematon komento. Yritä uudelleen.")