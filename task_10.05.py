with open("F:/Python/lesson_08/example_test.txt") as example_test:
    line = example_test.readlines()
    second_text = []
    third_text = []
    for i in range(len(line)):
        if not i % 2 == 0:
            second_text.append(line[i])
        else:
            third_text.append(line[i])
    with open("F:/Python/lesson_08/second_file.txt", "a") as second_file:
        second_file.write("".join(second_text))
    with open("F:/Python/lesson_08/third_file.txt", "a") as third_file:
        third_file.write("".join(third_text))
