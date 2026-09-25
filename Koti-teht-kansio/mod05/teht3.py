pienin = 0
suurin = 0

while True:
    syöte = input("Syötä luku (tyhjä lopettaa): ")
    if syöte == "":
        break

    luku = float(syöte)

    if pienin is 0 and suurin is 0:
        pienin = luku
        suurin = luku
    else:
        if luku < pienin:
            pienin = luku
        if luku > suurin:
            suurin = luku

if pienin != 0:
    print(f"Pienin luku: {pienin}")
    print(f"Suurin luku: {suurin}")
else:
    print("Et syöttänyt yhtään lukua.")