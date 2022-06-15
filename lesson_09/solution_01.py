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

from math import pi, sqrt


class Point:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Circle:

    def __init__(self, centre: Point, radius: int):
        self.centre = centre
        self.radius = radius

    def perimeter(self) -> float:
        return pi * 2 * self.radius

    def area(self) -> float:
        return pi * self.radius * self.radius


class Triangle:

    def __init__(self, point_a: Point, point_b: Point, point_c: Point):
        self.point_a = point_a
        self.point_b = point_b
        self.point_c = point_c

    @staticmethod
    def triangle_side_length(point_a: Point, point_b: Point):
        return sqrt(abs(point_a.x - point_b.x) ** 2 + abs(point_a.y - point_b.y) ** 2)

    def perimeter(self):
        side_ab = Triangle.triangle_side_length(point_a=self.point_a, point_b=self.point_b)
        side_bc = Triangle.triangle_side_length(point_a=self.point_b, point_b=self.point_c)
        side_ca = Triangle.triangle_side_length(point_a=self.point_c, point_b=self.point_a)
        return (side_ab + side_bc + side_ca) / 2


class Square:

    def __init__(self, side_a: Point, side_b: Point):
        self.side_a = side_a
        self.side_b = side_b


if __name__ == "__main__":
    circle_01 = Circle(Point(4, 7), 3)
    print(f"Circle perimeter: {circle_01.perimeter()}")    # Circle perimeter: 18.84955592153876

    triangle_01 = Triangle(Point(2, 2), Point(6, 2), Point(6, 5))
    print(f"Triangle perimeter: {triangle_01.perimeter()}")    # Triangle perimeter: 6.0
