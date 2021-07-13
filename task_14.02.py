from time import sleep
from random import randint

a: int = 0
b: int = 10
diff: int = 10


def repeat(x, y, shift):
    """Infinite random number generator

    :param x: the beginning of random number range
    :param y: the end of the random number range
    :param shift: random number range offset
    :return: random number
    """
    while True:
        yield randint(x, y)
        sleep(1)
        x = x + shift
        y = y + shift


for i in repeat(a, b, diff):
    print(i)
