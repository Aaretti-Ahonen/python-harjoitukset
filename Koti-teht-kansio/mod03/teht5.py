leiviska = input('anna leiviskät: ')
naula = input('anna naulat: ')
luoti = input('anna luodit: ')
massa = float(leiviska) * 8512 + float(naula) * 425.6 + float(luoti) * 13.3
print("Massa nykymittojen mukaan: " + str(massa // 1000) + (" kilogrammaa ja ") + str(round(massa % 1000)) + (" grammaa."))