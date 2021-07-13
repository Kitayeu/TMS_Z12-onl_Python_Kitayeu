import os
import sys

file_path = os.path.realpath(__file__)
dir_name = os.path.dirname(file_path)
os.mkdir(sys.argv[1])
