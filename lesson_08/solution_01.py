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

    def increase_speed(self):
        self.speed += 5

    def decrease_speed(self):
        self.speed -= 5

    def car_stop(self):
        while self.speed != 0:
            self.speed -= 5

    def display_speed(self):
        print(f"Current car speed: {self.speed}")

    def car_reverse(self):
        max_reverse_speed: int = -40
        if self.speed <= 0:
            if self.speed > max_reverse_speed:
                self.speed -= 5
