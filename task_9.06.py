from datetime import datetime


def my_decorator(func):
    """The decorator displays the execution time of the function 'func'"""
    time = datetime.now()
    print(f"Execution time of the '{func.__name__}' function {time}")
    return func


@my_decorator
def my_func():
    """Function for the presentation of the decorator's work"""
    print("Check")


my_func()
