from random import randint

list_five = []
quantity: int = 19
min_number: int = 1
max_number: int = 10
number: int = 0
for _ in range(quantity):
    list_five.append(randint(min_number, max_number))
print(f"Massif: {list_five}")
list_sorted = sorted(list_five)
max_element = list_sorted[-1]
while number <= quantity:
    list_five[number] = max_element
    number += 2
print(f"New massif: {list_five}")
