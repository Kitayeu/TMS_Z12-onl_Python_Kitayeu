from random import randint

list_six = []
quantity: int = 19
min_number: int = 1
max_number: int = 10
number: int = 1
answer = 0
for _ in range(quantity):
    list_six.append(randint(min_number, max_number))
print(f"Massif: {list_six}")
for number in range(quantity):
    if list_six[number - 1] == list_six[number] - 1:
        if list_six[number - 2] == list_six[number - 1] - 1 == list_six[number] - 2:
            pass
        else:
            answer += 1
print(f"Number of sections: {answer}")
