"""
Создать новый класс Cat, который имеет все те же атрибуты что и Dog, только заменить метод bark на meow.
"""

from classwork_01 import Dog


class Cat(Dog):

    def talk(self):
        print(f"{self.name} is meowing")


if __name__ == "__main__":
    cat_1 = Cat(7, 4, "Barsik", 1)
    cat_1.talk()
