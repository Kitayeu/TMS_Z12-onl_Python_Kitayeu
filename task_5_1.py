while True:
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    sign = str(input("Enter sign, if you want to stop the program, enter '0': "))
    if sign == "+":
        z = x + y
        print(f"{x} {sign} {y} = {z}")
    elif sign == "-":
        z = x - y
        print(f"{x} {sign} {y} = {z}")
    elif sign == "/":
        if y == 0:
            print("Division by zero is impossible")
        else:
            z = x / y
            print(f"{x} {sign} {y} = {z}")
    elif sign == "*":
        z = x * y
        print(f"{x} {sign} {y} = {z}")
    elif sign == "0":
        break
    else:
        print("Incorrect sign")
