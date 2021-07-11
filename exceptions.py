from classes import Math


def ex():
    try:
        a = float(input("Enter the first number: "))
        sign = str(input("Enter sign: "))
        b = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid number")
        a = 0
        b = 0
        sign = "+"
    if sign == "+":
        obj = Math(a, b)
        print(Math.amount(obj))
    elif sign == "-":
        obj = Math(a, b)
        print(Math.subtraction(obj))
    elif sign == "/":
        if b == 0:
            print("Division by zero is impossible")
        else:
            obj = Math(a, b)
            print(Math.division(obj))
    elif sign == "*":
        obj = Math(a, b)
        print(Math.multiplication(obj))
    elif sign == "0":
        return "break"
    else:
        print("Incorrect sign")
