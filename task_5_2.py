x = str(input("Enter the number: "))
list_x = list(x)
amount = 0
multiplication = 1
for i in list_x:
    multiplication *= int(i)
    amount += int(i)
print(f"Sum of numbers: {amount}, multiplying of numbers equals to: {multiplication}")
