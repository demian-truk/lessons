"""
Переопределить магические методы сложения, вычитания, умножения на число.
"""

from classwork_01 import MyTime


class NewTime(MyTime):

    def __add__(self, other: MyTime):
        return self.to_seconds() + other.to_seconds()

    def __sub__(self, other: MyTime):
        return self.to_seconds() - other.to_seconds()

    def __mul__(self, other: MyTime):
        return self.to_seconds() * other.to_seconds()