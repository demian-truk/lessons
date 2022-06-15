"""
Создать класс Point, описывающий точку (атрибуты: x, y). Создать класс Figure.
Создать три дочерних класса Circle, Triangle, Square.
Класс Circle:
    -атрибуты: координаты центра, длина радиуса;
    -методы: нахождение периметра и площади окружности.
Класс Triangle:
    -атрибуты: три точки;
    -методы: нахождение периметра и площади треугольника.
Класс Square:
    -атрибуты: две точки;
    -методы: нахождение периметра и площади квадрата.
При потребности создавать все необходимые методы не описанные в задании.
"""

from math import pi, sqrt


class Point:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Figure:

    def perimeter(self) -> float:
        raise NotImplementedError

    def area(self) -> float:
        raise NotImplementedError

    @staticmethod
    def side_length(point_a: Point, point_b: Point) -> float:
        return sqrt(abs(point_a.x - point_b.x) ** 2 + abs(point_a.y - point_b.y) ** 2)


class Circle(Figure):

    def __init__(self, centre: Point, radius: int):
        self.centre = centre
        self.radius = radius

    def perimeter(self) -> float:
        return pi * 2 * self.radius

    def area(self) -> float:
        return pi * self.radius * self.radius


class Triangle(Figure):

    def __init__(self, point_a: Point, point_b: Point, point_c: Point):
        self.point_a = point_a
        self.point_b = point_b
        self.point_c = point_c
        self.side_ab = self.side_length(self.point_a, self.point_b)
        self.side_bc = self.side_length(self.point_b, self.point_c)
        self.side_ca = self.side_length(self.point_c, self.point_a)

    def perimeter(self) -> float:
        return self.side_ab + self.side_bc + self.side_ca

    def area(self) -> float:
        half_per = self.perimeter() / 2
        return sqrt(half_per * (half_per - self.side_ab) * (half_per - self.side_bc) * (half_per - self.side_ca))


class Square(Figure):

    def __init__(self, point_a: Point, point_b: Point):
        self.point_a = point_a
        self.point_b = point_b
        self.side_ab = self.side_length(self.point_a, self.point_b)

    def perimeter(self) -> float:
        return self.side_ab * 4

    def area(self) -> float:
        return self.side_ab * self.side_ab


if __name__ == "__main__":
    circle_01 = Circle(Point(4, 7), 3)
    print(f"Circle perimeter: {circle_01.perimeter()}")    # Circle perimeter: 18.84955592153876

    triangle_01 = Triangle(Point(2, 2), Point(6, 2), Point(6, 5))
    print(f"Triangle perimeter: {triangle_01.perimeter()}")    # Triangle perimeter: 12.0

    square_01 = Square(Point(2, 2), Point(7, 2))
    print(f"Square perimeter: {square_01.perimeter()}")    # Square perimeter: 20.0
