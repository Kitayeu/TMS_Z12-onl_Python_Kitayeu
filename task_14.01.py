from time import sleep
from random import randint


def repeat():
    """Infinite random number generator

    :return: random number
    """
    while True:
        yield randint(0, 100)
        sleep(1)


for i in repeat():
    print(i)
