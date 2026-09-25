lentoasemat = {}

while True:
    print("\nValitse toiminto:")
    print("1 = Syötä uusi lentoasema")
    print("2 = Hae lentoaseman tiedot")
    print("3 = Lopeta")

    valinta = input("Valintasi (1-3): ")

    if valinta == "1":
        icao = input("Syötä ICAO-koodi: ")
        nimi = input("Syötä lentoaseman nimi: ")
        lentoasemat[icao] = nimi
        print(f"Lentoasema {nimi} ({icao}) tallennettu.")

    elif valinta == "2":
        icao = input("Syötä haettavan lentoaseman ICAO-koodi: ")
        if icao in lentoasemat:
            print(f"Lentoaseman nimi: {lentoasemat[icao]}")
        else:
            print("Virheellinen ICAO-koodi.")

    elif valinta == "3":
        print("Lopetit!")
        break

    else:
        print("Virheellinen valinta yritä uudelleen.")