from random import randint

numbers = [randint(0, 20) for _ in range(10)]
print(f"List of numbers: {numbers}")
string = map(lambda x: str(x), numbers)
print(list(string))
