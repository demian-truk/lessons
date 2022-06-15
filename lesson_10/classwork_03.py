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
        if self.current_value <= self.limit:
            self.current_value *= self.power
            return previous_value
        else:
            raise StopIteration

    def __iter__(self):
        self.current_value = 1
        return self


if __name__ == "__main__":
    my_geom = GeomProgIterator(power=2, limit=16)
    for item in my_geom:
        print(item)
