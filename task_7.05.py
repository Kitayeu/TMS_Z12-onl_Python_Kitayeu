def func(*args: float) -> float:
    """The function takes an indefinite number of arguments '*args' as input
    and returns the sum of args[i] * i. 'i' - ordinal index of a number

    :param args: undefined number of arguments for the function
    :return: amount of the type args[i] * i
    """
    result = 0
    for i, elem in enumerate(args):
        result += i*elem
    return result


print(func(4, 3, 2, 1))
