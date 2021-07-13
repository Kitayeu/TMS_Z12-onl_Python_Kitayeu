import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("-fld", "--folder_name", required=True)
parser.add_argument("-fl", "--file_name", required=True, help="Name of the file with extension")
args = parser.parse_args()
file_path = os.path.realpath(__file__)
dir_name = os.path.dirname(file_path)
os.mkdir(args.folder_name)
end = args.file_name.split('.')[-1]
if end == "py":
    with open(f"{dir_name}\\{args.folder_name}\\{args.file_name}", "w") as new_file:
        new_file.writelines(["def main():\n", "    pass\n", "\n", "\n", "if __name__ == '__main__':\n", "    main()",
                             "\n"])
else:
    my_file = open(f"{dir_name}\\{args.folder_name}\\{args.file_name}", "w")
    my_file.close()
