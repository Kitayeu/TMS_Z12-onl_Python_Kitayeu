import numpy

rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
min_number: int = 0
max_number: int = 10
list_meaning = numpy.random.randint(min_number, max_number, size=(rows, columns))
sum_four = numpy.sum(list_meaning)
answer = 0
quantity = numpy.size(list_meaning)
arithmetic_mean = sum_four / quantity
for i in range(rows):
    for j in range(columns):
        if list_meaning[i][j] > arithmetic_mean and (i + j) % 2 == 0:
            answer += 1
print(list_meaning)
print(f"Number of elements {answer}")
