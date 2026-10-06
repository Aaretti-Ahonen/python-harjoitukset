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

def heita_noppaa():
    tulos = random.randint(1, 6)
    if tulos == 6:
        print("\n> Heitit noppaa ja sait lukeman: 6 eli natural six.")
    else:
        print(f"\n> Heitit noppaa ja sait lukeman: {tulos}")

def lisaa_esine():
    esine = input("\nMitä haluat lisätä inventoriin? ").strip()
    if esine:
        inventori.append(esine)
        print(f"> Lisäsit esineen '{esine}' inventoriin.")
    else:
        print("> Et lisännyt mitään.")

def nayta_inventori():
    print("\n INVENTORI ")
    if not inventori:
        print("Inventori on tyhjä.")
    else:
        for esine in inventori:
            print(f"- {esine}")

nimi = input('Oma Nimi: ')
ikä = int(input('Oma Ikä: '))

print(f"Pelaaja: {nimi}.\nIkä: {ikä}-Vuotta.")

if ikä < 12:
    print("Olet alaikäinen, ohjelma suljetaan.")

else:
    print("Tervetuloa peliin!")

    pelaaja = Pelaaja(nimi, Osoite("pääalue"))
    pelaaja.esineet = inventori

    while True:
         
        if pelaaja.sijainti.osoite == "pääalue":
            print("\n--- PÄÄALUE ---")
            print("1. kaivos - Mene kaivokselle")
            print("2. kauppa - Mene kauppaan")
            print("3. inventori - Katso inventori")
            print("4. lopeta - Lopeta peli")

        elif pelaaja.sijainti.osoite == "kaivos":
            print("\n--- KAIVOS ---")
            print("1. kaiva - Kaiva kiveä")
            print("2. pääalue - Palaa pääalueelle")
            print("3. inventori - Katso inventori")

        elif pelaaja.sijainti.osoite == "kauppa":
            print("\n--- KAUPPA ---")
            print("1. pääalue - Palaa pääalueelle")
            print("2. inventori - Katso inventori")

        komento = input("\nSyötä komento: ").strip().lower()

        if komento == "tutoriaali":
            kerro_tutoriaali(nimi)

        elif komento == "noppa":
            heita_noppaa()

        elif komento == "lisaa":
            lisaa_esine()

        elif komento == "inventori":
            nayta_inventori()

        elif komento == "lopeta":
            print("Lopetit pelin.")
            break

        else:
            print("\nTuntematon komento. Yritä uudelleen.")