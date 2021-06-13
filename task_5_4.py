n = int(input("Enter the number: "))
i: int = 1
s: int = 0
while i <= n:
    s += 1 / i
    i += 1
print(f"Sum of numbers: {s}")
