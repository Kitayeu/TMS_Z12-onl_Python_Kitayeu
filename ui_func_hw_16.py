from class_hw_16 import (adding_brand, updating_brand, deleting_brand, reading_brand, adding_car,
                         updating_car, deleting_car, reading_car)


def ex():
    while True:
        print("If you want to stop the program, enter '0'\n"
              "If you want to work with the 'cars' table, enter 'c'\n"
              "If you want to work with the 'brands' table, enter 'b'")
        letter = str(input("Enter letter: "))
        if letter == 'c':
            try:
                print("If you want to stop the program, enter '0',for support enter '5'")
                number = int(input("Enter number: "))
            except ValueError:
                print("Invalid number")
            else:
                if number == 1:
                    try:
                        model = str(input("Enter model: "))
                        release_year = int(input("Enter release year: "))
                        brand_id = int(input("Enter brand id: "))
                    except ValueError:
                        print("Incorrect value")
                    else:
                        adding_car(model, release_year, brand_id)
                elif number == 2:
                    reading_car()
                elif number == 3:
                    try:
                        id = int(input("Enter id: "))
                        model = str(input("Enter model: "))
                        release_year = int(input("Enter release year: "))
                        brand_id = int(input("Enter brand id: "))
                    except ValueError:
                        print("Incorrect value")
                    else:
                        updating_car(id, model, release_year, brand_id)
                elif number == 4:
                    try:
                        id = int(input("Enter id: "))
                    except ValueError:
                        print("Incorrect value")
                    else:
                        deleting_car(id)
                elif number == 0:
                    break
                elif number == 5:
                    print("1 - Creating a new row in the 'cars' table\n"
                          "2 - Reading all rows from the 'cars' table\n"
                          "3 - Updating car data by 'id' from the 'cars' table\n"
                          "4 - Deleting a car by 'id' from the 'cars' table")
        elif letter == 'b':
            try:
                print("If you want to stop the program, enter '0',for support enter '5'")
                number = int(input("Enter number: "))
            except ValueError:
                print("Invalid number")
            else:
                if number == 1:
                    name = str(input("Enter name: "))
                    adding_brand(name)
                elif number == 2:
                    reading_brand()
                elif number == 3:
                    try:
                        id = int(input("Enter id: "))
                        name = str(input("Enter name: "))
                    except ValueError:
                        print("Incorrect value")
                    else:
                        updating_brand(id, name)
                elif number == 4:
                    try:
                        id = int(input("Enter id: "))
                    except ValueError:
                        print("Incorrect value")
                    else:
                        deleting_brand(id)
                elif number == 0:
                    break
                elif number == 5:
                    print("1 - Creating a new row in the 'brands' table\n"
                          "2 - Reading all rows from the 'brands' table\n"
                          "3 - Updating brand data by 'id' from the 'brands' table\n"
                          "4 - Deleting a brand by 'id' from the 'brands' table")
        elif letter == '0':
            break
