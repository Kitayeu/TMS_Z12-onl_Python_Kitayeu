from random import randint

rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
min_number: int = 0
max_number: int = 10
meaning = ""
sum_three = 0
for i in range(rows):
    for e in range(columns):
        meaning = randint(min_number, max_number)
        if meaning == 7:
            sum_three += 1
        print(meaning, end=" ")
    print()
print(f"The number '7' occurs {sum_three} time")
