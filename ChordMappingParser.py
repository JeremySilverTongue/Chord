import csv

import Fingers

COLUMNS_TO_FINGERS_MAPPING = {
    1 : Fingers.INDEX,
    2 : Fingers.MIDDLE,
    3 : Fingers.RING,
    4 : Fingers.PINKY,
    5 : Fingers.THUMB1,
    6 : Fingers.THUMB2
}

INDICATOR = "x"

def parse_mapping_CSV(csv_file_name):
    mapping = {}
    with open(csv_file_name) as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            parse_row(row, mapping)
    return mapping

def parse_row(row, mapping):
    if len(row) == 7:
        output_char = row[0]
        chord = set()
        for index in range(1,7):
            if row[index] == INDICATOR:
                chord.add(COLUMNS_TO_FINGERS_MAPPING[index])
        mapping[frozenset(chord)] = output_char

def main():
    print parse_mapping_CSV("mapping.csv")


if __name__ == '__main__':
    main()


# 31 - 4 = 27

