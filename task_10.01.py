# point a)
try:
    my_file = open("F:/Python/lesson_08/example_test.txt")
    print(my_file.readline())
    my_file.close()
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("No access rights for the file")
except IsADirectoryError:
    print("You are trying to open a directory")

# point b)
try:
    my_file = open("F:/Python/lesson_08/example_test.txt")
    print(my_file.readlines()[4])
    my_file.close()
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("No access rights for the file")
except IsADirectoryError:
    print("You are trying to open a directory")
except IndexError:
    print("List index out of range")

# point c)
try:
    my_file = open("F:/Python/lesson_08/example_test.txt")
    line = my_file.readlines()
    for i in range(5):
        print(line[i], end="")
    my_file.close()
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("No access rights for the file")
except IsADirectoryError:
    print("You are trying to open a directory")
except IndexError:
    print("List index out of range")
finally:
    print()

# point d)
try:
    s1 = int(input("Enter the beginning of range to print: "))
    s2 = int(input("Enter the end of range to print: "))
    my_file = open("F:/Python/lesson_08/example_test.txt")
    line = my_file.readlines()
    for i in range(s1-1, s2):
        print(line[i], end="")
    my_file.close()
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("No access rights for the file")
except IsADirectoryError:
    print("You are trying to open a directory")
except IndexError:
    print("List index out of range")
except ValueError:
    print("Invalid range number")
finally:
    print()

# point e)
try:
    my_file = open("F:/Python/lesson_08/example_test.txt")
    print(my_file.read())
    my_file.close()
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("No access rights for the file")
except IsADirectoryError:
    print("You are trying to open a directory")
