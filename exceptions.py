from func import amount, subtraction, multiplication, division


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
        print(amount(a, b))
    elif sign == "-":
        print(subtraction(a, b))
    elif sign == "/":
        if b == 0:
            print("Division by zero is impossible")
        else:
            print(division(a, b))
    elif sign == "*":
        print(multiplication(a, b))
    elif sign == "0":
        return "break"
    else:
        print("Incorrect sign")
