from datetime import datetime
import csv


def earliest(link: str):
    """Function searches for the earliest date from file 'link'

    :param link: address of сsv file
    """
    with open(link, newline='') as f:
        ignore = f.readline()
        reader = csv.reader(f)
        dates = [datetime.strptime(row[0], "%d/%m/%Y") for row in reader]
        date = min(dates)
        print(f"The earliest date is {date}")


filename = "F:/Python/lesson_08/weather.csv"
earliest(filename)
