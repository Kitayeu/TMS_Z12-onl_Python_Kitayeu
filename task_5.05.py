surnames = ["Смирнов", "Иванов", "Попова", "Петров", "Пономарёв", "Королёв", "Павлова"]
variable_five = 0
surname = ""
while variable_five < len(surnames):
    if surnames[variable_five][0].upper() == "П" and surnames[variable_five][-1].lower() == "а":
        surname += surnames[variable_five] + " "
    variable_five += 1
print(surname)
