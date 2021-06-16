# Homework - 07
# task_6_1

def one(i: float) -> str:
    """Converting 'i' inches to centimeters"""
    result = i * 2.54
    return f"In {i} inches {result} centimeters"


def two(i: float) -> str:
    """Converting 'i' centimeters to inches"""
    result = i / 2.54
    return f"In {i} centimeters {result} inches"


def three(i: float) -> str:
    """Converting 'i' miles to kilometers"""
    result = i * 1.61
    return f"In {i}  miles {result} kilometers"


def four(i: float) -> str:
    """Converting 'i' kilometers to miles"""
    result = i / 1.61
    return f"In {i} kilometers {result} miles"


def five(i: float) -> str:
    """Converting 'i' pounds to kilograms"""
    result = i / 2.2046226
    return f"In {i} pounds {result} kilograms"


def six(i: float) -> str:
    """Converting 'i' kilograms to pounds"""
    result = i * 2.2046226
    return f"In {i} kilograms {result} pounds"


def seven(i: float) -> str:
    """Converting 'i' ounces to grams"""
    result = i * 28.35
    return f"In {i} ounces {result} grams"


def eight(i: float) -> str:
    """Converting 'i' grams to ounces"""
    result = i / 28.35
    return f"In {i} grams {result} ounces"


def nine(i: float) -> str:
    """Converting 'i' gallons to liters"""
    result = i * 4.5461
    return f"In {i} gallons {result} liters"


def ten(i: float) -> str:
    """Converting 'i' liters to gallons"""
    result = i / 4.5461
    return f"In {i} liters {result} gallons"


def eleven(i: float) -> str:
    """Converting 'i' pints to liters"""
    result = i * 0.5683
    return f"In {i} pints {result} liters"


def twelve(i: float) -> str:
    """Converting 'i' liters to pints"""
    result = i / 0.5683
    return f"In {i} liters {result} pints"


# task_6_2

print("Choose conversion option: ")
print("1. Inches to centimeters")
print("2. Centimeters to inches")
print("3. Miles to kilometers")
print("4. Kilometers to miles")
print("5. Pounds to kilograms")
print("6. Kilograms to pounds")
print("7. Ounces to grams")
print("8. Grams to ounces")
print("9. Gallons to liters")
print("10. Liters to gallons")
print("11. Pints to liters")
print("12. Liters to pints")
print("If you want to exit, enter '0'")
functions = {
    '1': one,
    '2': two,
    '3': three,
    '4': four,
    '5': five,
    '6': six,
    '7': seven,
    '8': eight,
    '9': nine,
    '10': ten,
    '11': eleven,
    '12': twelve,
}
programs = str(input("Enter convert number: "))
while programs != "0":
    if programs in functions.keys():
        try:
            number = float(input("Enter the number to convert: "))
        except ValueError:
            number = 0
        fun = functions[programs]
        print(fun(number))
        programs = str(input("Enter convert number, if you want to exit, enter '0': "))
    else:
        programs = str(input("Wrong choice, try again, if you want to exit, enter '0': "))
