valinta = input('Plus\nMiinus\nKerto\nLopeta\nKirjoita Valinta: ')

while valinta != "Lopeta":
    numero1 = (int(input('Ensimmäinen numero: ')))
    numero2 = (int(input('Toinen numero: ')))  
    if valinta == "plus":
        print(f"Tulos: {numero1 + numero2}")
        valinta = input('Plus\nMiinus\nKerto\nLopeta\nKirjoita Valinta: ')
    elif valinta == "Miinus":
        print(f"Tulos: {numero1 - numero2}")
        valinta = input('Plus\nMiinus\nKerto\nLopeta\nKirjoita Valinta: ')
    elif valinta == "Kerto":
        print(f"Tulos: {numero1 * numero2}")
        valinta = input('Plus\nMiinus\nKerto\nLopeta\nKirjoita Valinta: ')
    else:
        valinta = input('Plus\nMiinus\nKerto\nLopeta\nKirjoita Valinta: ')
print('Laskin Lopetettu.')