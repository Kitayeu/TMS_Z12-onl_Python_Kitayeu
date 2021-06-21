def func(a: float, b: float, c: float) -> str:
    """The function solves quadratic equations of the type 'ax2 + bx + c = 0'

    :param a: numerical coefficient of the equation
    :param b: numerical coefficient of the equation
    :param c: numerical coefficient of the equation
    :return: the result of solving the equation
    """

    discriminant = float((b**2) - (4*a*c))
    print("D = {}".format(discriminant))
    if discriminant > 0:
        x1 = float(((-b) + (discriminant**(1/2))) / (2*a))
        x2 = float(((-b) - (discriminant**(1/2))) / (2*a))
        return "X1 = {}, X2 = {}".format(x1, x2)
    elif discriminant == 0:
        x = (-b) / (2*a)
        return "X = {}".format(x)
    else:
        return "No roots"


print(func(1, 17, -18))
