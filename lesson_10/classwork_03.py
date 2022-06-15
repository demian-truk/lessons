"""
Создать генератор и/или итератор простой геометрической прогрессии.
"""


class GeoProgIterator:

    def __init__(self, power, limit):
        self.power = power
        self.limit = limit
        self.current_value = 1

    def __next__(self):
        if self.current_value < self.limit:
            self.current_value *= self.power
            return 1
        else:
            raise StopIteration