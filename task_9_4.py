def my_decorator(f):
    """The decorator changes order of arguments of function 'f' to opposite"""
    def wrapped(*args):
        response = f(*args[::-1])
        return response
    return wrapped


@my_decorator
def subtraction(a, b):
    """The function subtracts 'b' from 'a' """
    return a - b


print(subtraction(10, 15))
