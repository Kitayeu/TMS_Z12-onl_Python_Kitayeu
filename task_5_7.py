import numpy

dimension = int(input("Enter dimension of matrix: "))
min_number: int = 0
max_number: int = 10
list_meaning = numpy.random.randint(min_number, max_number, size=(dimension, dimension))
print(list_meaning)
position_max = numpy.argmax(list_meaning, axis=1)
diagonal = numpy.diagonal(list_meaning)
new_list = numpy.copy(list_meaning)
for i in range(len(list_meaning)):
    new_list[i][i] = list_meaning[i][position_max[i]]
    new_list[i][position_max[i]] = list_meaning[i][i]
print("Matrix with modified diagonal: ")
print(new_list)
