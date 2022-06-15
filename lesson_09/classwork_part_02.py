"""
# 1:
Добавить новый класс MyDateTime, унаследованный от MyTime.
В конструктор добавить новые атрибуты: day, month, year. “Исправить” все магические методы для этого класса.

# 2:
Создать объект класса MyDateTime, умножить его на 2 и вывести на печать результат.
"""

from __future__ import annotations
from classwork_part_01 import MyTime


class MyDateTime(MyTime):

    def __init__(self, year: int, month: int, day: int, hours: int, minutes: int, seconds: int):
        super().__init__(hours, minutes, seconds)
        self.year = year
        self.month = month
        self.day = day

    def to_seconds(self) -> int:
        return sum([
            self.seconds,
            self.minutes * 60,
            self.hours * 60 * 60,
            self.day * 60 * 60 * 24,
            self.month * 60 * 60 * 24 * 30,
            self.year * 60 * 60 * 24 * 30 * 12,
        ])

    @staticmethod
    def seconds_to_time(seconds) -> MyDateTime:
        year = seconds // (60 * 60 * 24 * 30 * 12)
        seconds -= 60 * 60 * 24 * 30 * 12 * year
        month = seconds // (60 * 60 * 24 * 30)
        seconds -= 60 * 60 * 24 * 30 * month
        day = seconds // (60 * 60 * 24)
        seconds -= 60 * 60 * 24 * day
        hours = seconds // (60 * 60)
        seconds -= 60 * 60 * hours
        minutes = seconds // 60
        seconds -= 60 * minutes
        return MyDateTime(year=year, month=month, day=day, hours=hours, minutes=minutes, seconds=seconds)

    def __mul__(self, other: int) -> MyDateTime:
        seconds = self.to_seconds() * other
        return MyDateTime.seconds_to_time(seconds)

    def __str__(self) -> str:
        return f"Year: {self.year}, month: {self.month}, day: {self.day}," \
               f" time: {self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"


if __name__ == "__main__":
    date_time_01 = MyDateTime(1, 9, 2, 12, 22, 17)
    result_mul = date_time_01 * 2
    print(result_mul)    # Year: 3, month: 6, day: 5, time: 00:44:34
