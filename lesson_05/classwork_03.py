"""
Написать функцию, которая принимает на вход неопределенным количеством аргументов и именованный аргумент func_type.
В зависимости от func_type вернуть минимальное либо максимальное значение.
Написать программу в виде трех функций.
"""

my_list = [10, 15, 1, 13, 7, 5, 100, 4]

def my_max(*args):
    max_number = args[0]
    for number in args:
        if number > max_number:
            max_number = number
    return max_number


def my_min(*args):
    min_number = args[0]
    for number in args:
        if number < min_number:
            min_number = number
    return min_number


def min_or_max(func_type, *args):
    if func_type == "min":
        result = my_min(*args)
    else:
        result = my_max(*args)
    return result

print(min_or_max("min", *my_list))
print(min_or_max("max", *my_list))
