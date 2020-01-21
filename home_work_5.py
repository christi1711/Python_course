import csv
import argparse
import sys
import json

parser = argparse.ArgumentParser()
parser.add_argument('csv', help='path to input CSV file')
parser.add_argument('json', help='path to output JSON file')
arg = parser.parse_args(sys.argv[1:])

def CSVtoJSON():
        with open(arg.csv, 'r', newline='') as csv_file :
            data = csv.DictReader(csv_file, delimiter=',')
            json_file = open(str(arg.json), 'w')
            for row in data:
                    row = dict(row)
                    for key in row.keys():
                        if key == 'password':
                            row[key] = '*********'
                            break;
                    json.dump(row, json_file, indent = 4)
            json_file.write('\n')
            json_file.close()
            print("JSON parsed!")
if __name__ == '__main__' :
    CSVtoJSON()
