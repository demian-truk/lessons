"""
Доработать первое задание так, чтобы словарь читался из текстового CSV файла.
При этом на каждой строке пары слов вида: apple,яблоко.
"""

import csv

my_dict = {}

with open("dictionary.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        my_dict[row[0]] = row[1]

print(my_dict)
