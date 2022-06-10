"""
Создать класс Car. Атрибуты класса: марка, модель, год выпуска, скорость (по умолчанию 0).
Методы класса:
    a) увеличение скорости (скорость +5),
    b) уменьшение скорости (скорость -5),
    c) стоп (сброс скорости на 0),
    d) отображение скорости,
    f) задний ход (изменение знака скорости).
"""


class Car:

    def __init__(self, brand: str, model, year_of_manufacture: int):
        self.brand = brand
        self.model = model
        self.year_of_manufacture = year_of_manufacture
        self.speed = 0

    def change_speed(self):
        pass
