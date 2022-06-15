"""
Создать функцию при помощи регулярных выражений.
Функция проверяет является ли строка валидным телефонным номером в формате +375 (29) 299-29-29.
"""

import re


def is_mobile_phone(string):
    return re.search(r"^\+\d{3}\s\(\d{2}\)\s\d{3}-\d{2}-\d{2}$", string)


if __name__ == "__main__":
    assert is_mobile_phone("+375 (29) 299-29-29") is not None
