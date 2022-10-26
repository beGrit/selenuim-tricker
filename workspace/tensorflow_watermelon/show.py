import csv

from numpy import ndarray


def loading_data() -> ndarray:
    with open('./datas/input.csv', 'r') as file:
        csv_reader = csv.reader(file)
        for idx, row in enumerate(csv_reader):
            if idx == 0:
                continue
            else:
                pass
