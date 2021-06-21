from random import randint


def create_matrix(n: int, random_from: int=1, random_to: int=9) -> list:
    """The function creates a matrix of dimension 'n' with random numbers from 'random_from' to 'random_to'

    :param n: dimension of the matrix
    :param random_from: the minimum number from the range of random numbers, by default '1'
    :param random_to: the maximum number from the range of random numbers, by default '9'
    :return: created matrix
    """
    matrix = [[randint(random_from, random_to) for _ in range(n)] for _ in range(n)]
    return matrix


print(create_matrix(4))
