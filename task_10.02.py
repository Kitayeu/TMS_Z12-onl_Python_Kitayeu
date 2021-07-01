try:
    my_file = open("F:/Python/lesson_08/new_file.txt", "x+")
    for i in range(6):
        line = input("Enter string:")
        if i == 0:
            my_file.write(line)
        else:
            my_file.write(f"\n{line}")
    my_file.close()
except FileExistsError:
    print("File with this name already exists")
