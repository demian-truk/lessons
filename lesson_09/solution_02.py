"""
Создать список фигур, в цикле подсчитать и вывести площади всех фигур на экран.
"""

from solution_01 import Point, Circle, Triangle, Square

figures = [
    Circle(Point(4, 7), 3),
    Triangle(Point(2, 2), Point(6, 2), Point(6, 5)),
    Square(Point(2, 2), Point(7, 2)),
]

for figure in figures:
    print(f"Area of {figure.__class__.__name__}: {figure.area()}")
    # Area of Circle: 28.274333882308138
    # Area of Triangle: 6.0
    # Area of Square: 25.0
