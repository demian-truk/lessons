"""
# 1:
Создать класс MyTime. Атрибуты: hours, minutes, seconds.
Методы: переопределить магические методы сравнения (==, !=, >=, <=, <, >).

# 2:
Переопределить магические методы сложения, вычитания, умножения на число.

# 3:
Создать метод, который выводит на экран отформатированное время (HH:MM:SS).

# 4:
Создать объект класса MyTime, умножить его на 2 и вывести на печать результат.

# 5:
Создать второй объект класса MyTime.
Найти разницу с первым объектом, добавить к нему 7 часов и 45 минут, вывести на печать результат.
"""

from __future__ import annotations


class MyTime:

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def to_seconds(self) -> int:
        return self.seconds + self.minutes * 60 + self.hours * 60 * 60

    @staticmethod
    def seconds_to_time(seconds) -> MyTime:
        hours = seconds // (60 * 60)
        minutes = (seconds % (60 * 60)) // 60
        seconds = seconds % 60
        return MyTime(hours=hours, minutes=minutes, seconds=seconds)

    def __eq__(self, other: MyTime):
        return self.to_seconds() == other.to_seconds()

    def __ne__(self, other: MyTime):
        return self.to_seconds() != other.to_seconds()

    def __ge__(self, other: MyTime):
        return self.to_seconds() >= other.to_seconds()

    def __le__(self, other: MyTime):
        return self.to_seconds() <= other.to_seconds()

    def __lt__(self, other: MyTime):
        return self.to_seconds() < other.to_seconds()

    def __gt__(self, other: MyTime):
        return self.to_seconds() > other.to_seconds()

    def __add__(self, other: MyTime) -> MyTime:
        seconds = self.to_seconds() + other.to_seconds()
        return MyTime.seconds_to_time(seconds)

    def __sub__(self, other: MyTime) -> MyTime:
        seconds = self.to_seconds() - other.to_seconds()
        return MyTime.seconds_to_time(seconds)

    def __mul__(self, other: int) -> MyTime:
        seconds = self.to_seconds() * other
        return MyTime.seconds_to_time(seconds)

    def __str__(self) -> str:
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"


if __name__ == "__main__":
    time_01 = MyTime(1, 36, 15)
    result_mul = time_01 * 2
    print(result_mul)    # 03:12:30

    time_02 = MyTime(2, 48, 26)
    result_sub = time_02 - time_01
    print(result_sub)    # 01:12:11

    time_03 = MyTime(7, 45, 0)
    result_add = time_02 + time_03
    print(result_add)    # 10:33:26
