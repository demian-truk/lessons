"""
Создать класс Point, описывающий точку (атрибуты: x, y). Создать класс Figure.
Создать три дочерних класса Circle, Triangle, Square.
Класс Circle:
    -атрибуты: координаты центра, длина радиуса;
    -методы: нахождение периметра и площади окружности.
Класс Triangle:
    -атрибуты: три точки;
    -методы: нахождение площади и периметра.
Класс Square:
    -атрибуты: две точки;
    -методы: нахождение площади и периметра.
При потребности создавать все необходимые методы не описанные в задании.
"""


class Point:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Circle:

    def __init__(self, centre: Point, radius: int):
        self.centre = centre
        self.radius = radius


class Triangle:

    def __init__(self):
        pass


class Square:

    def __init__(self):
        pass
