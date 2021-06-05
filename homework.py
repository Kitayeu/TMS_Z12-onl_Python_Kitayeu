# Задание 1.1
a: int = 5
print(type(a))
print(a)
b: float = 2.5
print(type(b))
print(b)
c: str = "Hello world"
print(type(c))
print(c)
d: bool = True
print(type(d))
print(d)

# Задание 1.2
example_one = ((17/2)*3) + 2
print(example_one)
example_two = 2 + ((17/2)*3)
print(example_two)
example_three = (19 % 4) + ((15/2)*3)
print(example_three)
example_four = (15+6) - (10*4)
print(example_four)
example_five = ((17/2) % 2) * (3**3)
print(example_five)

# Задание 1.3
neighbour_one: int = 41
neighbour_two: int = 38
neighbour_three: int = 54
print(neighbour_one + neighbour_two + neighbour_three)
middle_of_ages = (neighbour_one + neighbour_two + neighbour_three) / 3
print(middle_of_ages)

# homework - 01
# task_1_1
a: int = 56
b: float = 4.5
print(a+b)
print(a-b)
print(a*b)

# task_1_2
x: int = -3
y: int = 1
print((abs(x) - abs(y)) / (1 + abs(x*y)))

# task_1_3
side_of_cube: int = 35
volume_of_cube = side_of_cube**3
area_of_sides = (side_of_cube**2) * 4
print(volume_of_cube)
print(area_of_sides)

# task_1_4
a: float = 9.5
b: float = 4.8
middle_of_sum = (a+b) / 2
middle_of_geometric = (a*b) ** (1/2)
print(middle_of_sum)
print(middle_of_geometric)

# task_1_5
catheter_one: int = 25
catheter_two: int = 82
hypotenuse = ((catheter_one**2) + (catheter_two**2)) ** (1/2)
area_of_triangle = (catheter_one*catheter_two) / 2
print(hypotenuse)
print(area_of_triangle)
