from math import sqrt


class Point:
    def __init__(self, x, y):
        if x >= 0 and y >= 0:
            self._x = x
            self._y = y
        else:
            print("The coordinates must be greater than zero")

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        if x < 0:
            print("The coordinates must be greater than zero")
        else:
            self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        if y < 0:
            print("The coordinates must be greater than zero")
        else:
            self._y = y

    def __str__(self):
        return f"coordinates {self._x}:{self._y}"

    def __repr__(self):
        return f"{self.__class__} {self._x}:{self._y}"


class Figure:
    PI = 3.14
    list_obj = []

    def __init__(self):
        self.__class__.list_obj.append(self)


class Circle(Figure):
    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b
        self.ab = self.sides()
        # ab - is the radius, set by the coordinates of the center of the circle 'a' and the point on the circle 'b'

    def sides(self):
        x1 = self.a.x
        y1 = self.a.y
        x2 = self.b.x
        y2 = self.b.y
        ab = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return ab

    def __str__(self):
        return f"{self.a},{self.b}"

    def __repr__(self):
        return f"{self.__class__} and {self.a},{self.b}"

    def perimeter(self):
        return 2 * self.__class__.PI * self.ab

    def area(self):
        return self.__class__.PI * self.ab ** 2


class Triangle(Figure):
    def __init__(self, a, b, c):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c
        self.ab = self.sides()[0]
        self.bc = self.sides()[1]
        self.ca = self.sides()[2]

    def sides(self):
        x1 = self.a.x
        y1 = self.a.y
        x2 = self.b.x
        y2 = self.b.y
        x3 = self.c.x
        y3 = self.c.y
        ab = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        bc = sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
        ca = sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
        return ab, bc, ca

    def __str__(self):
        return f"{self.a},{self.b}, {self.c}"

    def __repr__(self):
        return f"{self.__class__} and {self.a},{self.b}, {self.c}"

    def perimeter(self):
        if self.ab <= self.bc + self.ca:
            return self.ab + self.bc + self.ca
        else:
            return "It is not a triangle"

    def area(self):
        if self.ab <= self.bc + self.ca:
            p = (self.ab + self.bc + self.ca) / 2
            return sqrt(p * (p - self.ab) * (p - self.bc) * (p - self.ca))
        else:
            return "It is not a triangle"


class Square(Figure):
    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b
        self.side1 = self.sides()[0]
        self.side2 = self.sides()[1]

    def __str__(self):
        return f"{self.a},{self.b}"

    def __repr__(self):
        return f"{self.__class__} and {self.a},{self.b}"

    def sides(self):
        x1 = self.a.x
        y1 = self.a.y
        x2 = self.b.x
        y2 = self.b.y
        side1 = abs(x1 - x2)
        side2 = abs(y1 - y2)
        return side1, side2

    def perimeter(self):
        return self.side1 * 2 + self.side2 * 2

    def area(self):
        return self.side1 * self.side2
