hytti = input('Laivasi hyttiluokka: ')
hyttisi = str(input('Laivasi hyttiluokka: '))
if hyttisi == "LUX":
     print("LUX on parvekkeellinen hytti yläkannella.")
elif hyttisi == "A":
     print("A on ikkunallinen hytti autokannen yläpuolella.")
elif hyttisi == "B":
     print("B on ikkunaton hytti autokannen yläpuolella.")
elif hyttisi == "C":
     print("C on ikkunaton hytti autokannen alapuolella.")
else:
     print("Virheellinen Hyttiluokka.")