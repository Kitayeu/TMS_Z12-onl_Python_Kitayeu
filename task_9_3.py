from random import randint

numbers = [randint(0, 20) for _ in range(10)]
print(numbers)


def my_decorator(f):
    """The decorator performs a preliminary data check and removes all even elements from the list 'd'"""
    def wrapped(d: list):
        s = []
        for i in d:
            if not i % 2 == 0:
                s.append(i)
        response = f(s)
        return response
    return wrapped


@my_decorator
def func(x: list):
    """The function calculates sum of elements of 'x' list"""
    result = sum(x)
    print(result)


func(numbers)
