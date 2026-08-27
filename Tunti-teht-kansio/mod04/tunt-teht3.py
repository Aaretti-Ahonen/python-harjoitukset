nimi = input('Syötä hahmon nimi: ')
valinta = input('Onko hahmosi nainen vai mies: ')
if valinta == "nainen" or valinta == "mies":
    print(f"{nimi} Kuvittelee olevansa {valinta}")
else: 
    print("virheellinen sukupuoli.")