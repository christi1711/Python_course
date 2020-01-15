import csv
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-path_csv')
parser.add_argument('-col_name')
arg = parser.parse_args(sys.argv[1:])

try:
    with open (arg.path_csv, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        result = [row[arg.col_name.replace('_', ' ')] for row in reader]
        print('\n'.join(result))
except IOError:
    print("File not exist")



