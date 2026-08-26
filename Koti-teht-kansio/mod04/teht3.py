sukupuoli = input('Sukupuolesi ilman isoja kirjaimia: ')
hemo = int(input('Hemoglobiini arvosi (g/l): '))
if sukupuoli == "mies" and hemo < 134:
    print("Hemoglobiini arvo on alhainen")
elif sukupuoli == "mies" and 134 <= hemo <= 195:
    print("Hemoglobiinisi on normaali.")
elif sukupuoli == "mies" and hemo > 195:
    print("Hemoglobiinisi on korkea.")
elif sukupuoli == "nainen" and hemo < 117:
    print("Hemoglobiinisi on alhainen.")
elif sukupuoli == "nainen" and 117 <= hemo <= 175:
    print("Hemoglobiinisi on normaali.")
elif sukupuoli == "nainen" and hemo > 175:
    print("Hemoglobiinisi on korkea.")
else:
    print("Virheellinen sukupuoli.")