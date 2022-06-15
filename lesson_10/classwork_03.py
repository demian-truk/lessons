"""
Создать генератор и/или итератор простой геометрической прогрессии.
"""


class GeomProgIterator:

    def __init__(self, power, limit):
        self.power = power
        self.limit = limit
        self.current_value = 1

    def __next__(self):
        previous_value = self.current_value
        self.current_value *= self.power
        if self.current_value < self.limit:
            return previous_value
        else:
            raise StopIteration


if __name__ == "__main__":
    pass
