nimi = input('Oma Nimi: ')
ikä = (int(input('Oma Ikä: ')))
print("Pelaaja: " + nimi + (".") + "\nIkä: " + str(ikä) + "-Vuotta.")
if ikä < 12:
    print("Olet alaikäinen, ohjelma suljetaan.")
else:
    print("Tervetuloa peliin!")
    while True:
        print("\n--- PÄÄVALIKKO ---")
        print("Komennot:")
        print("1. tarina  - Lue lyhyt tarina")
        print("2. noppa   - Heitä noppaa")
        print("3. lopeta  - Sulje ohjelma")

        komento = input("\nSyötä komento: ").strip().lower()
        
        if komento == "lopeta":
            print("Kiitos pelaamisesta! Näkemiin.")
            break
            
        elif komento == "tarina":
            print("\n> Pelaaja sinun tarinasi on vasta alkamassa.")
        elif komento == "noppa":
            import random
            tulos = random.randint(1, 6)
            if tulos == 6:
                print(f"\n> Heitit noppaa ja sait lukeman: 6 eli natural six.")
            else:
                print(f"\n> Heitit noppaa ja sait lukeman: {tulos}")
        else:
            print("\nTuntematon komento. Yritä uudelleen.")
