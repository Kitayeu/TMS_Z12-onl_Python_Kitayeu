from random import randint

number = int(input("Enter dimension of matrix: "))
min_number: int = 0
max_number: int = 100
meaning = ""
sum_two = 0
for i in range(number):
    for e in range(number):
        meaning = randint(min_number, max_number)
        if meaning % 3 == 0:
            sum_two += meaning
        print(meaning, end=" ")
    print()
print(f"Sum of numbers multiples '3': {sum_two}")
