def f(a: int) -> float:
    """The function calculates the equation with the variable 'a'

    :param a: numeric variable
    :return: the result of a mathematical equation
    """
    result = (a**0.5 + a) / 2
    return result


x = f(5) + f(12) + f(19)
print(x)
