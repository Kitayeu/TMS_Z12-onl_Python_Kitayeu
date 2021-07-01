from csv_utils import write, read
import csv

filename = "F:/Python/lesson_08/weather.csv"
fields = ['Date', 'Place', 'Degrees', 'Wind speed']
rows = [
    ['15/06/2021', 'Minsk', 23, 5],
    ['16/06/2021', 'Minsk', 22, 5],
    ['17/06/2021', 'Minsk', 25, 4],
    ['18/06/2021', 'Minsk', 26, 5],
    ['19/06/2021', 'Minsk', 27, 5],
    ['20/06/2021', 'Minsk', 29, 6],
    ['21/06/2021', 'Minsk', 28, 6],
    ['22/06/2021', 'Minsk', 31, 6],
    ['23/06/2021', 'Minsk', 31, 5],
    ['24/06/2021', 'Minsk', 32, 4],
    ['25/06/2021', 'Minsk', 28, 10],
    ['26/06/2021', 'Minsk', 25, 7],
    ['27/06/2021', 'Minsk', 23, 6],
    ['28/06/2021', 'Minsk', 24, 7],
    ['29/06/2021', 'Minsk', 24, 6],
    ['30/06/2021', 'Minsk', 27, 3],
]
write(filename, fields, rows)
read(filename)


def average_weather(link: str):
    """Function calculates average weather (wind speed and degrees) for city for last 7 days from 'link' file

    :param link: address of сsv file
    """
    with open(link, newline='') as f:
        ignore = f.readline()
        reader = csv.reader(f)
        data = [[row[2], row[3], row[1]] for row in reader]
        wind = 0
        temperature = 0
        for x in data[-7:]:
            temperature += int(x[0]) / 7
            wind += int(x[1]) / 7
        print(f"Average wind speed {wind} and average temperature {temperature} for {data[-1][2]} for last 7 days")


average_weather(filename)
