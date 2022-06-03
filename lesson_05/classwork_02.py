"""
Создать функцию, которая принимает на вход неопределенное количество аргументов.
Данная функция возвращает их сумму и максимальное из них.
"""


def sum_and_max(*args):
    result_sum = 0
    max_number = args[0]
    for number in args:
        result_sum += number
        if number > max_number:
            max_number = number
    return result_sum, max_number


my_list = [10, 15, 1, 13, 7, 5, 100, 4]

print(sum_and_max(*my_list))
