def arithmetic_mean(x: tuple) -> str:
    """The function calculates the arithmetic mean of the numbers in tuple 'x'

    :param x: indefinite number of arguments in tuple 'x'
    :return: arithmetic mean 'result' in the tuple 'x'
    """
    result = sum(x) / len(x)
    return f"Arithmetic mean: {result}"


def geometric_mean(x: tuple) -> str:
    """The function calculates the geometric mean of the numbers in tuple 'x'

    :param x: indefinite number of arguments in tuple 'x'
    :return: geometric mean 'result' in the tuple 'x'
    """
    multiplication: int = 1
    for i in x:
        multiplication *= i
    result = multiplication ** (1 / len(x))
    return f"Geometric mean: {result}"


def func(*args: float, mean_type: str):
    """The function accepts an indefinite number of arguments '*args' and a named
    argument 'mean_type'. Depending on 'mean_type', return the arithmetic mean or the geometric mean '*args'

    :param args: an undefined number of arguments
    :param mean_type: takes two values. If "среднеарифметическое" calls the function 'arithmetic_mean',
    if "среднегеометрическое" calls the function 'geometric_mean'
    """
    if mean_type == "среднеарифметическое":
        print(arithmetic_mean(args))
    elif mean_type == "среднегеометрическое":
        print(geometric_mean(args))
    else:
        print("Incorrect 'mean_type'")


func(5, 2, 6, 4, 7, 8, mean_type="среднеарифметическое")
func(5, 2, 6, 4, 7, 8, mean_type="среднегеометрическое")
func(1, 2, 3, 4, 5, 6, mean_type="средне")
