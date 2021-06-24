from random import randint
from functools import reduce

numbers = [randint(0, 20) for _ in range(10)]
print(f"List of numbers: {numbers}")
try:
    result = reduce(lambda a, x: a * x, filter(lambda x: x != 0 and not x % 3, numbers))
    print(result)
except TypeError:
    print("There are no numbers that are multiples of '3'")
