"""
Создайте функцию three_args(), которая принимает 1, 2 или 3 ключевых параметра.
В результате ее работы на печать выводятся значения переданных переменных, но только если они не равны None.
Получим, например, следующее сообщение: Переданы аргументы: var1 = 2, var3 = 10.
"""


def three_args(**kwargs):
    result = []
    for key, value in kwargs.items():
        if value is not None:
            result.append(f"{key} = {value}")
    print(f"Arguments passed: {result}")


three_args(var1=88, var2=None, var3=92)    # Arguments passed: ['var1 = 88', 'var3 = 92']
