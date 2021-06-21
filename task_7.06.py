def func(*args: float) -> str:
    """The function takes an indefinite number of arguments '*args' as input and
    returns their sum 'result' and maximum number 'maximum_number'

    :param args: undefined number of arguments for the function
    :return: sum of numbers 'result' and maximum number 'maximum_number'
    """
    result: float = 0
    maximum_number: float = 0
    for i in args:
        result += i
        if i > maximum_number:
            maximum_number = i
    return f"Sum of numbers: {result}, maximum number: {maximum_number}"


print(func(4, 3, 2, 1, 9, 5.5))
