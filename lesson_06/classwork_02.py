"""
Доработать первое задание так, чтобы словарь читался из текстового CSV файла.
При этом, на каждой строке пары слов вида: apple,яблоко.
"""

import csv

my_dict = {}

with open("new_dictionary.csv", "r") as file:
    my_dict = {row[0]: row[1] for row in csv.reader(file)}


def eng_to_rus(word):
    return my_dict[word]


def rus_to_eng(word):
    for key, value in my_dict.items():
        if value == word:
            return key


print(eng_to_rus("House"))    # Дом
print(rus_to_eng("Яблоко"))    # Apple
