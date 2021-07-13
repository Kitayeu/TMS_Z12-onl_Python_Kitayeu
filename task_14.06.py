import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("-fld", "--folder_name", required=True)
parser.add_argument("-fl", "--file_name", required=True)
args = parser.parse_args()
file_path = os.path.realpath(__file__)
dir_name = os.path.dirname(file_path)
os.mkdir(args.folder_name)
my_file = open(f"{dir_name}\\{args.folder_name}\\{args.file_name}", "w")
my_file.close()
