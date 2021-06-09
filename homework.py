import random

# task 4.01

list_one = [2, 20, 6.5, 10, 11, 30, 45, 18]
sum_one = 0
for i in list_one:
    if i > 10:
        sum_one += i
    else:
        continue
print(sum_one)

# task 4.02

sum_two = 0
while True:
    number_two = input("Input number: ")
    print("If you want to stop? Input 'стоп'")
    if number_two != "стоп":
        number_two = float(number_two)
        sum_two += number_two
    else:
        break
print(sum_two)

# task 4.03

sum_three = 0
while True:
    number_three = input("Input number: ")
    print("If you want to stop? Input 'стоп'")
    if number_three != "стоп":
        number_three = float(number_three)
        if number_three % 5 == 0:
            continue
        else:
            sum_three += number_three
    else:
        break
print(sum_three)

# task 4.04

number_four = int(input("Input number: "))
sum_four = 0
meaning: int = 1
while meaning <= number_four:
    sum_four += meaning**3
    meaning += 1
print(sum_four)

# task 4.05

min_five: int = 1
max_five: int = 10
number_five = ""
while number_five != 7:
    number_five = random.randint(min_five, max_five)
    print(number_five)

# task 4.06

first_number = int(input("Input first number: "))
second_number = int(input("Input second number: "))
sum_six = 0
for d in range(first_number, second_number+1):
    sum_six += d**3
print(sum_six)

# task 4.07

number_first = int(input("Input first number: "))
numbers_second = int(input("Input second number: "))
if number_first < numbers_second:
    list_seven = list(range(number_first, numbers_second + 1))
    length = len(list_seven)
    print(list_seven)
    print(f"Number of digits {length}")
else:
    print("Wrong")

# Homework 04

# task_4_1

# cycle "while" is used
new_list = [2, 12, 6, 10, 11, 38, 54, 18]
index = 0
while index < len(new_list):
    new_list[index] = new_list[index] * (-2)
    index += 1
print(new_list)
# cycle "for" is used
new_list_one = [21, 2, 16, 1, 12, 8, 24, 81]
for q in range(len(new_list_one)):
    new_list_one[q] = new_list_one[q] * (-2)
print(new_list_one)

# task_4_2

# cycle "while" is used
list_two = [2, 4, 6, 11, 31, 38, 54, 17]
index_two = 0
quantity = 0
while index_two < len(list_two):
    if list_two[index_two] % 2 == 0:
        quantity += 1
    index_two += 1
print(quantity)
# cycle "for" is used
quantity_one = 0
for t in range(len(list_two)):
    if list_two[t] % 2 == 0:
        quantity_one += 1
print(quantity_one)

# task_4_3

# cycle "while" is used
dict_example = {"test": "test_value", "europe": "eur", "dollar": "usd", "ruble": "rub"}
list_three = list(dict_example.keys())
index_three = 0
long = ""
name_key = ""
while index_three < len(list_three):
    long = str(len(list_three[index_three]))
    name_key = list_three[index_three] + long
    dict_example[name_key] = dict_example.pop(list_three[index_three])
    index_three += 1
print(dict_example)
# cycle "for" is used
dict_example_one = {"test": "test_value", "europe": "eur", "dollar": "usd", "ruble": "rub"}
list_three_one = list(dict_example_one.keys())
name_key_one = ""
long_one = ""
for k in range(len(list_three_one)):
    long_one = str(len(list_three_one[k]))
    name_key_one = list_three_one[k] + long_one
    dict_example_one[name_key_one] = dict_example_one.pop(list_three_one[k])
print(dict_example_one)

# task_4_4

# cycle "while" is used
list_four = [5, 2, 4, 6, 11, 31, 38, 54, 17]
index_four = 0
position = 0
list_four_new = []
while index_four < len(list_four):
    position = index_four - len(list_four) + 1
    list_four_new += [list_four[position]]
    index_four += 1
print(list_four_new)
# cycle "for" is used
list_four = [5, 2, 4, 6, 11, 31, 38, 54, 17]
position_one = 0
list_four_one_new = []
for u in range(len(list_four)):
    position_one = u - len(list_four) + 1
    list_four_one_new += [list_four[position_one]]
print(list_four_one_new)

# task_4_5

# cycle "while" is used
digital_five = int(input("Input first number: "))
step = 14
index_five = 0
list_five = []
while index_five <= step:
    if index_five == 0 or index_five == 1:
        list_five.append(digital_five)
    else:
        list_five.append(list_five[index_five - 1] + list_five[index_five - 2])
    index_five += 1
print(list_five)
# cycle "for" is used
digital_five_new = int(input("Input first number: "))
list_five_new = []
for j in range(0, 15):
    if j == 0 or j == 1:
        list_five_new.append(digital_five_new)
    else:
        list_five_new.append(list_five_new[j - 1] + list_five_new[j - 2])
print(list_five_new)
