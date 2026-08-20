grammaa = input('Grammojen määrä: ')
print("Määrä kiloina ja grammoina: " + str(float(grammaa) // 1000) + ("kg ") + str(float(grammaa) % 1000) + ("g"))
#print(f"Määrä kiloina ja grammoina: {grammaa // 1000} kg {grammaa % 1000} g")