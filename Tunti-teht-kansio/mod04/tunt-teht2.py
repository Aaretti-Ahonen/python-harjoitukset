pituus = int(input('Pituutesi senttimetreinä: '))
if pituus > 140:
    ikä = int(input('Ikä: '))
if pituus < 100:
    print("Et pääse mihinkään laitteeseen")
elif 100 <= pituus <= 140:
    print("Pääset lasten laitteisiin")
elif 140 < pituus <= 195 and ikä > 9:
    print("pääset kaikkiin laitteisiin")
elif 140 < pituus <= 195 and ikä < 9:
    print("pääset kaikkiin laitteisiin paitsi tulirekeen")
elif pituus > 195 and ikä < 9:
    print("pääset kaikkiin laitteisiin paitsi kirnuun ja tulirekeen")
else:
    print("pääset kaikkiin laitteisiin paitsi kirnuun")