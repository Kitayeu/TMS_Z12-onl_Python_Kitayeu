from random import randint

a = [randint(-100, 100) for _ in range(30)]
print(f"Array: {a}")


def func(d: list):
    """The function finds sum of positive and negative elements of the array 'd'

    :param d: array of integers
    """
    sum_positive: int = 0
    sum_negative: int = 0
    for i in d:
        if i > 0:
            sum_positive += i
        else:
            sum_negative += i
    print(f"Sum of positive array elements: {sum_positive}, sum of negative array elements: {sum_negative}")


func(a)
