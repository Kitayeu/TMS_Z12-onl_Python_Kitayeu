m = int(input("Enter the first number: "))
n = int(input("Enter the second number: "))
divisor = ""
while m <= n:
    for i in range(2, m):
        if m % i == 0:
            divisor += f" {str(i)}"
    print(f"{m}: {divisor}")
    m += 1
    divisor = ""
