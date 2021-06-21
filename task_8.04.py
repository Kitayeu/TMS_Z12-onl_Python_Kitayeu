from random import randint

numbers = [randint(1, 10) for _ in range(10)]
print(f"List of numbers {numbers}")


def func(x: list):
    """The function counts how many times each number occurs in the list 'x'

    :param x: list with numbers
    """
    new_dict = dict()
    for number in x:
        result = x.count(number)
        new_dict.update({number: result})
    print(new_dict)


func(numbers)
