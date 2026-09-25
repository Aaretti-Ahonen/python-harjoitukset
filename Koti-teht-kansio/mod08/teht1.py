vuodenajat = ("talvi", "talvi", "kevät", "kevät", "kevät", "kesä", "kesä", "kesä", "syksy", "syksy", "syksy", "talvi")
kuukausi = int(input("Syötä kuukauden numero (1-12): "))

if 1 <= kuukausi <= 12:
    vastaus = vuodenajat[kuukausi - 1]
    print(f"Kuukausi {kuukausi} kuuluu vuodenaikaan: {vastaus}")
else:
    print("Virheellinen kuukauden numero! Syötä luku väliltä 1-12.")