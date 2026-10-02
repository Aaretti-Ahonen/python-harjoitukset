import random
inventori = [
     {"nimi": "Kivi", "määrä": 0},
    {"nimi": "Puu-Hakku", "Voima": 1}
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
    
    while True:
        print("\n--- PÄÄVALIKKO ---")
        print("Komennot:")
        print("1. tutoriaali    - Pelin tutoriaali")
        print("2. noppa     - Heitä noppaa")
        #hakkaamaan  -  menee kaivamaan
        #kauppa -  osta vahvempi hakkuuväline
        #Vapaus  -  Kokeile onneasi
        print("3. lisaa     - Lisää esine inventoriin")
        print("4. inventori - Katso inventorin sisältö")
        print("5. lopeta    - Sulje ohjelma")

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