from classes import *

j = Point(0, 0)
k = Point(6, 0)
h = Point(6, 6)
print(j)

circle = Circle(j, k)
print(circle)
print(Circle.perimeter(circle))
print(Circle.area(circle))

triangle = Triangle(j, k, h)
print(Triangle.perimeter(triangle))
print(Triangle.area(triangle))
print(triangle)

square = Square(h, j)
print(Square.perimeter(square))
print(Square.area(square))
print(square)

all_area = sum([shape.area() for shape in Figure.list_obj])
print(all_area)
