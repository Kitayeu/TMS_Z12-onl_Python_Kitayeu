numbers = [36, 8, 243, 256, 625, 343, 100, 90, 80, 14]


def is_power_n(k: int, n: int) -> bool:
    """Boolean type function, returns 'True' if the integer parameter 'k' (> 0)
    is a power of 'n' (> 1), otherwise 'False'

    :param k: number 'k' is checked whether it is a power of 'n'
    :param n: number 'n' is checked to see if the number 'k' is its power
    :return: boolean value of the validity of the expression
    """
    while True:
        k /= n
        if k == 1:
            return True
        elif k < 1:
            return False


n = int(input("Enter number: "))
result: int = 0
for number in numbers:
    if is_power_n(number, n):
        result += 1
print(result)
