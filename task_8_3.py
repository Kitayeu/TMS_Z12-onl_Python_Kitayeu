from math import factorial, pow, fabs


def sin1(x: float, eps: float):
    """The function of the real type (parameters 'x' , 'eps' — real, 'eps' > 0), finds the approximate value
     of the function sin(x):sin(x) = x – x^3 / (3!) + x^5 / (5!) – ... + (-1)^n · x^(2·n + 1) / ((2·n + 1)!)+ ...
     In total, we consider all the terms whose modulus is greater than 'eps'

    :param x: the variable whose sine is found by the function
    :param eps: accuracy of the entire calculation
    """
    if eps > 0:
        n: int = 0
        flag = True
        result: float = 0
        while flag is True:
            argument = (pow(-1, n) / factorial(2 * n + 1)) * pow(x, 2 * n + 1)
            if fabs(argument) > eps:
                result += argument
                n += 1
            else:
                print(f"sin({x}) = {result}")
                flag = False
    else:
        print("Epsilon should be greater than '0'")


epsilon = [0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001]
x: int = 5
for eps in epsilon:
    print(f"ε = {eps}")
    sin1(x, eps)
