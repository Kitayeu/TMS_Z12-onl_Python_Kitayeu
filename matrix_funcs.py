from matrix_classes import Matrix


def max_element(matrix: Matrix):
    """Function searches for the maximum element of 'matrix'

    :param matrix: an object of the 'Matrix' class
    """
    element_max = matrix[0][0]
    for row in matrix:
        if max(row) > element_max:
            element_max = max(row)
    print(f"Maximum element of matrix: {element_max}")


def min_element(matrix: Matrix):
    """Function searches for the minimum element of the 'matrix'

    :param matrix: an object of the 'Matrix' class
    """
    element_min = matrix[0][0]
    for row in matrix:
        if min(row) < element_min:
            element_min = min(row)
    print(f"Minimum element of matrix: {element_min}")


def amount(matrix: Matrix):
    """Function searches for the sum of all the elements of 'matrix'

    :param matrix: an object of the 'Matrix' class
    """
    result: int = 0
    for row in matrix:
        result += sum(row)
    print(f"Sum of all elements: {result}")
