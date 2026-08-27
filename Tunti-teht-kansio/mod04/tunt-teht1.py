vuosi = int(input('Ilmoita vuosiluku: '))
if vuosi < 1896:
    print('Olympialaisia ei järjestetty')
elif vuosi > 2024:
    print('vuosi ei ole vielä tapahtunut')
elif vuosi == 2020:
    print("Olympialaisia ei järjestetty koronan takia.")
elif vuosi == 2021: 
    print("Olympialaiset järjestettiin poikkeuksellisesti koronan takia.")
elif vuosi % 4 == 0:
    print("Olympialaiset järjestettiin.")
else:
    print("Olympialaisia ei järjestetty")