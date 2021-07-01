new_file = open("F:/Python/lesson_08/new_file.txt")
while True:
    writing_text = []
    line = new_file.readline()
    if not line:
        break
    for i in line:
        if i == "1":
            writing_text.append("0")
        elif i == "0":
            writing_text.append("1")
        else:
            writing_text.append(i)
    with open("F:/Python/lesson_08/another_file.txt", "a") as another_file:
        another_file.write("".join(writing_text))
new_file.close()
