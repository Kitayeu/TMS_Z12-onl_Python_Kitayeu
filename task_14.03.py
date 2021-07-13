import sys

# Script takes an indefinite number of arguments at startup and calculates the sum of those that are digits
result: int = 0
for i in sys.argv[1:]:
    try:
        meaning = float(i)
    except TypeError:
        meaning = 0
    except ValueError:
        meaning = 0
    else:
        result += meaning
print(f"Sum of numbers: {result}")
