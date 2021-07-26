from class_hw_15 import adding, reading, updating, deleting


def ex():
    while True:
        print("If you want to stop the program, enter '0' for number, for support enter '5'")
        try:
            number = int(input("Enter number: "))
        except ValueError:
            print("Invalid number")
        else:
            if number == 1:
                try:
                    name = str(input("Enter name: "))
                    price = float(input("Enter price: "))
                    amount = int(input("Enter amount: "))
                    note = str(input("Enter note: "))
                except ValueError:
                    print("Incorrect value")
                else:
                    adding(name, price, amount, note)
            elif number == 2:
                reading()
            elif number == 3:
                try:
                    id = int(input("Enter id: "))
                    name = str(input("Enter name: "))
                    price = float(input("Enter price: "))
                    amount = int(input("Enter amount: "))
                    note = str(input("Enter note: "))
                except ValueError:
                    print("Incorrect value")
                else:
                    updating(id, name, price, amount, note)
            elif number == 4:
                try:
                    id = int(input("Enter id: "))
                except ValueError:
                    print("Incorrect value")
                else:
                    deleting(id)
            elif number == 0:
                break
            elif number == 5:
                print("1 - Creating a new row in the 'products' table\n"
                      "2 - Reading all rows from the 'products' table\n"
                      "3 - Updating product data by 'id' from the 'products' table\n"
                      "4 - Deleting a product by 'id' from the 'products' table")
