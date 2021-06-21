# Homework - 08

def fact2(n: int):
    """The function calculates the double factorial :n!! = 1·3·5·...·n,
     if 'n' is odd; n!! = 2·4·6·...·n, if 'n' is even

    :param n: the function calculates the double factorial of this number
    """
    if n > 0:
        result_one: int = 1
        result_two: int = 1
        for i in range(1, n + 1):
            if i % 2 != 0:
                result_one *= i
            else:
                result_two *= i
        print(f"Factorial of odd numbers of a given number: {result_one},"
              f"factorial of even numbers of a given number: {result_two}")
    else:
        print("The number must be greater than zero")


numbers = [3, 8, 4, 5, 7]
for number in numbers:
    fact2(number)
