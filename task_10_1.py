from csv_utils import write, read
import csv

filename = "F:/Python/lesson_08/society.csv"
fields = ['First name', 'Last name', 'Age']
rows = [
    ['Виктор', 'Шершуков', 5],
    ['Анастасия', 'Битова', 13],
    ['Валентин', 'Кириллов', 20],
    ['Игорь', 'Игнатьев', 28],
    ['Наталия', 'Самохвалова', 45],
    ['Лариса', 'Павлова', 11],
    ['Андрей', 'Баршев', 15],
    ['Захар', 'Оверченков', 20],
    ['Оксана', 'Бодалян', 32],
    ['Александр', 'Герасимов', 60],
    ['Софья', 'Леденева', 33],
    ['Светлана', 'Ватолкина', 38],
    ['Борис', 'Волик', 24],
    ['Яков', 'Архипов', 18],
    ['Екатерина', 'Гусева', 8],
]
write(filename, fields, rows)
read(filename)


def cheap(link: str) -> None:
    """Function creates a report file "F:/Python/lesson_08/report.csv" with information
    on number of people in age group from 'link' file

    :param link: address of сsv file
    """
    with open(link, newline='') as f:
        ignore = f.readline()
        reader = csv.reader(f)
        products = [int(row[2]) for row in reader]
        one = 0
        two = 0
        three = 0
        four = 0
        five = 0
        for i in products:
            if 1 <= i <= 12:
                one += 1
            elif 13 <= i <= 18:
                two += 1
            elif 19 <= i <= 25:
                three += 1
            elif 26 <= i <= 40:
                four += 1
            elif i > 40:
                five += 1
    with open("F:/Python/lesson_08/report.csv", "w", newline="") as csv_file:
        header = ['Age group', 'Number of people']
        lines = [
            ['1-12', one],
            ['13-18', two],
            ['19-25', three],
            ['26-40', four],
            ['40+', five],
        ]
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(header)
        csv_writer.writerows(lines)


cheap(filename)
read("F:/Python/lesson_08/report.csv")
