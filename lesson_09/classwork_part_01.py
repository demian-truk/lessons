"""
1. Создать класс MyTime. Атрибуты: hours, minutes, seconds.
Методы: переопределить магические методы сравнения (==, !=, >=, <=, <, >).

2. Переопределить магические методы сложения, вычитания, умножения на число.
"""

from __future__ import annotations


class MyTime:

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def to_seconds(self) -> int:
        return self.seconds + self.minutes * 60 + self.hours * 60 * 60

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

    @staticmethod
    def seconds_to_time(seconds) -> MyTime:
        hours = seconds // (60 * 60)
        minutes = (seconds % (60 * 60)) // 60
        seconds = seconds % 60
        return MyTime(hours=hours, minutes=minutes, seconds=seconds)

    def __add__(self, other: MyTime) -> MyTime:
        seconds = self.to_seconds() + other.to_seconds()
        return MyTime.seconds_to_time(seconds)

    def __sub__(self, other: MyTime) -> MyTime:
        seconds = self.to_seconds() - other.to_seconds()
        return MyTime.seconds_to_time(seconds)

    def __mul__(self, other: MyTime) -> MyTime:
        seconds = self.to_seconds() * other.to_seconds()
        return MyTime.seconds_to_time(seconds)