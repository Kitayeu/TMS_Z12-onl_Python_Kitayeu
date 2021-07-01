with open("F:/Python/lesson_08/new_file.txt", "a") as my_file:
    for _ in range(3):
        line = input("Enter string:")
        my_file.writelines(f"\n{line}")
