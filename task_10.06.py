with open("F:/Python/lesson_08/second_file.txt", "r") as second_file, open("F:/Python/lesson_08/third_file.txt", "r") \
            as third_file:
    line_second = second_file.readlines()
    line_third = third_file.readlines()
    flag: bool = True
    for i in range(len(line_second)):
        if line_second[i] != line_third[i]:
            print(f"The first line that differs in files is {i + 1}")
            flag: bool = False
            break
    if flag is True:
        print("All lines in files are the same")
