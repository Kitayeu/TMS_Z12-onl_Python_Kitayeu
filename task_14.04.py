import sys
import argparse
import csv

parser = argparse.ArgumentParser()
parser.add_argument("-fn", "--first_name", required=True)
parser.add_argument("-ln", "--last_name", required=True)
parser.add_argument("-ag", "--age", required=True)
args = parser.parse_args()
filename = "F:/Python/lesson_11/data_list.csv"
field = ["First name", "Last name", "Age"]
row = sys.argv[2::2]


def done(link: str, line: list, fields: list) -> None:
    """Function takes first name, last name and age from 'line' and adds them to the csv file 'link'.
     If there is no file, it creates it using 'link'

    :param link: address of сsv file
    :param line: data to be added
    :param fields: column names
    """
    try:
        with open(link) as csv_file:
            lines = csv_file.readlines()
        new_str = ','.join(line)
        lines.append(f"{new_str}\n")
        with open(link, "w") as csv_file:
            csv_file.writelines(lines)
    except FileNotFoundError:
        with open(link, "w", newline="") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(fields)
            csv_writer.writerow(line)


done(filename, row, field)
