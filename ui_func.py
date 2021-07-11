from exceptions import ex


def calculator():
    while True:
        print("If you want to stop the program, enter '0' for sign")
        if ex() == "break":
            break
