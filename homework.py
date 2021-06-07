# task 3.01

name: str = "Ivan"
print("Hello, {}!".format(name))

# task 3.02

first_number = input("Input the first integer number: ")
second_number = input("Input the second integer number: ")
first_number = int(first_number)
second_number = int(second_number)
sum_of_numbers = first_number + second_number
print("{} плюс {} равно {}".format(first_number, second_number, sum_of_numbers))

# task 3.03

string: str = "Hello World"
string_list = string.split(" ")
string_list = string_list[::-1]
string_list = " ".join(string_list)
print("! {} !".format(string_list))

# task 3.04

string_one: str = "good mood"
if len(string_one) % 3 == 0:
    print(string_one + "!")
else:
    print(string_one)

# task 3.05

string_two: str = "secret code"
meaning: str = "code"
if meaning.upper() in string_two.upper():
    print("Yes")
else:
    print("No")

# task 3.06

age = input("Input your age: ")
age = float(age)
if age < 0:
    print("Wrong input")
elif age < 18:
    print("CocaCola")
else:
    print("Beer")

# task 3.07

string_three: str = "homework - 03"
length = len(string_three)
if length > 5:
    print(length)
elif length < 5:
    print("Need more")
else:
    print("It is five")

# task 3.08

number = 7
if type(number) == int or type(number) == float:
    print(number**2)
else:
    pass

# task 3.09

print("Input the coefficients for the equation")
print("ax2 + bx + c = 0")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
discriminant = float((b**2) - (4*a*c))
print("D = {}".format(discriminant))
if discriminant > 0:
    x1 = float(((-b) + (discriminant**(1/2))) / (2*a))
    x2 = float(((-b) - (discriminant**(1/2))) / (2*a))
    print("X1 = {}, X2 = {}".format(x1, x2))
elif discriminant == 0:
    x = (-b) / (2*a)
    print("X = {}".format(x))
else:
    print("No roots")

# task 3.10

ruble = input("Input number of rubles: ")
kopeck = input("Input number of kopecks: ")
if ruble == '':
    pass
else:
    ruble = int(ruble)
    rubles = ruble % 10
    if rubles == 0 or rubles >= 5 or (10 <= ruble <= 19):
        print("{} рублей".format(ruble))
    elif rubles == 1:
        print("{} рубль".format(ruble))
    else:
        print("{} рубля".format(ruble))
if kopeck == '':
    pass
else:
    kopeck = int(kopeck)
    kopecks = kopeck % 10
    if kopecks == 0 or kopecks >= 5 or (10 <= kopeck <= 19):
        print("{} копеек".format(kopeck))
    elif kopecks == 1:
        print("{} копейка".format(kopeck))
    else:
        print("{} копейки".format(kopeck))

# task 3.11

mail_name = input("Input mail name: ")
if "gmail.com" in mail_name:
    print(mail_name)
else:
    print("DOMAIN NAME is not supported")

# Homework 03

# task_3_1
number = int(input("Input number: "))
if number % 1000 == 0:
    print("millennium")
else:
    pass

# task_3_2
number_of_people = int(input("Input number of people: "))
if number_of_people > 50:
    print("ресторан")
elif 20 <= number_of_people <= 50:
    print("кафе")
else:
    print("дом")

# task_3_3
string_value = input("Input string: ")
if len(string_value) >= 10:
    print("{}!!!".format(string_value))
else:
    print(string_value[1])

# task_3_4
string_value_one = input("Input string: ")
middle_letter = string_value_one[int(len(string_value_one)/2)]
print(middle_letter)
if middle_letter == string_value_one[0]:
    resulting_string = string_value_one[1:len(string_value_one)-1:]
    print(resulting_string)
