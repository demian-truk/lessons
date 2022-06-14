"""
Создать новый класс Cat, который имеет все те же атрибуты что и Dog, только заменить метод bark на meow.

# Upd - Программа имеет другой вид, получившийся после решения задания №4.
"""

from classwork_04 import Animal


class Cat(Animal):

    def talk(self):
        print(f"{self.name} is meowing")


if __name__ == "__main__":
    cat_1 = Cat(10, 5, "Elvis", 2)
    cat_1.jump()    # Elvis is jumping
    cat_1.run()    # Elvis is running
    cat_1.talk()    # Elvis is meowing
