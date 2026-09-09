import random

inventory = []

def lue_tarina(nimi):
    print(f"\n> Pelaaja {nimi}, sinun tarinasi on vasta alkamassa.")

def heita_noppaa():
    tulos = random.randint(1, 6)
    if tulos == 6:
        print("\n> Heitit noppaa ja sait lukeman: 6 eli natural six.")
    else:
        print(f"\n> Heitit noppaa ja sait lukeman: {tulos}")

def lisaa_esine():
    esine = input("\nMitä haluat lisätä inventoriin? ").strip()
    if esine:
        inventory.append(esine)
        print(f"> Lisäsit esineen '{esine}' inventoriin.")
    else:
        print("> Et lisännyt mitään.")

def nayta_inventory():
    print("\n INVENTORY ")
    if not inventory:
        print("Inventory on tyhjä.")
    else:
        for esine in inventory:
            print(f"- {esine}")

nimi = input('Oma Nimi: ')
ikä = int(input('Oma Ikä: '))
print(f"Pelaaja: {nimi}.\nIkä: {ikä}-Vuotta.")

if ikä < 12:
    print("Olet alaikäinen, ohjelma suljetaan.")
else:
    print("Tervetuloa peliin!")
    
    while True:
        print("\n--- PÄÄVALIKKO ---")
        print("Komennot:")
        print("1. tarina    - Lue lyhyt tarina")
        print("2. noppa     - Heitä noppaa")
        print("3. lisaa     - Lisää esine inventoriin")
        print("4. inventory - Katso inventoryn sisältö")
        print("5. lopeta    - Sulje ohjelma")

        komento = input("\nSyötä komento: ").strip().lower()
        
        
        if komento == "tarina":
         lue_tarina(nimi)
        elif komento == "noppa":
            heita_noppaa()
        elif komento == "lisaa":
            lisaa_esine()
        elif komento == "inventory":
            nayta_inventory()
        elif komento == "lopeta":
            print("Lopetit pelin.")
            break
        else:
            print("\nTuntematon komento. Yritä uudelleen.")