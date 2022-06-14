"""
1. Добавить новый класс MyDateTime унаследованный от MyTime.
В конструктор добавить новые атрибуты: day, month, year. “Исправить” все магические методы для этого класса.

2. Создать объект класса MyDateTime, умножить его на 2 и вывести на печать результат.
"""

from __future__ import annotations
from classwork_part_01 import MyTime


class MyDateTime(MyTime):

    def __init__(self, day, month, year, hours: int, minutes: int, seconds: int):
        super().__init__(hours, minutes, seconds)
        self.day = day
        self.month = month
        self.day = day

