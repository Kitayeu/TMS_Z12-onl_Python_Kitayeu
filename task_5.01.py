from random import randint

number = int(input("Enter dimension of matrix: "))
min_number: int = 1
max_number: int = 9
meaning = ""
for i in range(number):
    for e in range(number):
        meaning = randint(min_number, max_number)
        print(meaning, end=" ")
    print()
