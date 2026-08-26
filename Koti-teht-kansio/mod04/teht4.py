vuosi = int(input('Ilmoita vuosiluku: '))
vuosikarkaus = vuosi/4
vuosisata = vuosi/400
vuosisaas = vuosi/100
if vuosisata.is_integer():
    print("Vuotesi on karkaus vuosi")
elif vuosisaas.is_integer():
    print("Vuotesi ei ole karkaus vuosi")
elif vuosikarkaus.is_integer():
    print("Vuotesi on karkaus vuosi")
else:
    print("Vuotesi ei ole karkaus vuosi")
