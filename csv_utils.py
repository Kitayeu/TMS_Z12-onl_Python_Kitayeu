import csv


def read(link: str) -> None:
    """Function reads csv file at the specified address 'link'

    :param link: address of сsv file
    """
    with open(link, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)


def write(link: str, field: list, row: list) -> None:
    """Function writes data 'field' and 'row' to address 'link' in csv file

    :param link: address of сsv file
    :param field: column names
    :param row: data in rows
    """
    with open(link, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(field)
        csv_writer.writerows(row)


def add_line(link: str, line: list, index=None) -> None:
    """Adding 'line' entry to csv file 'link' by position 'index', by default at the end

    :param link: address of сsv file
    :param line: line to be added
    :param index: position of added line, by default at end
    """
    with open(link) as csv_file:
        lines = csv_file.readlines()
    if index is None:
        index = len(lines)
    new_str = ','.join(line)
    lines.insert(index, f"{new_str}\n")
    with open(link, "w") as csv_file:
        csv_file.writelines(lines)


def delete_line(link: str, index=None) -> None:
    """Deleting "line" entry in the csv file "link" by 'index' position, by default at the end

    :param link: address of сsv file
    :param index: position of delete line, by default at the end
    """
    with open(link) as csv_file:
        lines = csv_file.readlines()
    try:
        if index is None:
            index = len(lines) - 1
        del lines[index]
    except IndexError:
        print("List assignment index out of range")
    except TypeError:
        print("Index of list must be a number")
    with open(link, "w") as csv_file:
        csv_file.writelines(lines)


def amount(link: str):
    """Function calculates total sum of all products in the file 'link'

    :param link: address of сsv file
    """
    with open(link, newline='') as f:
        ignore = f.readline()
        reader = csv.reader(f)
        cost_product = 0
        for row in reader:
            cost_product += int(row[1]) * int(row[2])
        print(f"Total sum of all products: {cost_product}")


def expensive(link: str):
    """Function searches for the most expensive product in the file "link"

    :param link: address of сsv file
    """
    with open(link, newline='') as f:
        ignore = f.readline()
        reader = csv.reader(f)
        products = [[row[0], int(row[1])] for row in reader]
        product = int(products[0][1])
        for i in range(len(products)):
            if products[i][1] > product:
                product = products[i][1]
                name = products[i][0]
        print(f"The most expensive product is {name} with price {product}")


def cheap(link: str):
    """Function searches for the cheapest product in the file "link"

    :param link: address of сsv file
    """
    with open(link, newline='') as f:
        ignore = f.readline()
        reader = csv.reader(f)
        products = [[row[0], int(row[1])] for row in reader]
        product = int(products[0][1])
        for i in range(len(products)):
            if products[i][1] < product:
                product = products[i][1]
                name = products[i][0]
        print(f"The cheapest product is {name} with price {product}")


def reducing_number(link: str, product: str, number=None) -> None:
    """Function of reducing quantity of product "product" by "number" in "link" file by default by 1

    :param link: address of сsv file
    :param product: name of the product that needs to be reduced
    :param number: how much to reduce the quantity of goods
    """
    with open(link) as csv_file:
        ignore = csv_file.readline()
        lines = csv_file.readlines()
        file = [line.split(",") for line in lines]
        try:
            if number is None:
                number = 1
            for x in file:
                x[3] = x[3][:-1:1]
                if product in x:
                    x[2] = int(x[2]) - number
        except TypeError:
            print("Must be a number")
    with open(link, "w", newline="") as csv_file:
        csv_file.write(ignore)
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(file)
