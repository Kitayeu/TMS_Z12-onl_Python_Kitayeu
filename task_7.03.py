try:
    n = int(input("Enter number: "))
except ValueError:
    print("Invalid number")
else:
    if n > 0:
        result: int = 1
        for i in range(1, n + 1):
            result *= i
        print(f"Factorial of number: {result}")
    else:
        print("The number must be greater than zero")
