from random import randint
from numpy import argmin, argmax

try:
    rows = int(input("Enter number of rows: "))
    columns = int(input("Enter number of columns: "))
    min_element = int(input("Enter the minimum number: "))
    max_element = int(input("Enter the maximum number: "))
except ValueError:
    print("Invalid number")
else:
    if rows > 0 and columns > 0:
        if max_element > min_element:
            matrix = [[randint(min_element, max_element) for _ in range(columns)] for _ in range(rows)]
            print(f"Matrix: {matrix}")
            result: int = 0
            for x in matrix:
                result += sum(x)
            print(f"Sum of all elements: {result}")
            element_max = matrix[0][0]
            max_index = (0, 0)
            for index_max, row_mat in enumerate(matrix):
                if max(row_mat) > element_max:
                    element_max = max(row_mat)
                    max_index = (index_max, argmax(row_mat))
            print(f"Maximum element of matrix: {element_max}, position of the maximum element: {max_index}")
            element_min = matrix[0][0]
            min_index = (0, 0)
            for index, row in enumerate(matrix):
                if min(row) < element_min:
                    element_min = min(row)
                    min_index = (index, argmin(row))
            print(f"Minimum element of matrix: {element_min}, position of the minimum element: {min_index}")
        else:
            print("The maximum number must be greater than the minimum number")
    else:
        print("The number of rows and columns must be greater than zero")
