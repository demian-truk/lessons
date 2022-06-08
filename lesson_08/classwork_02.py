"""
Добавить в класс Dog метод change_name. Метод принимает на вход новое имя и меняет атрибут имени у объекта.
Создать один объект класса. Вывести имя. Вызвать метод change_name. Вывести имя.
"""

from classwork_01 import Dog


class NewDog(Dog):

    def change_name(self, new_name):
        self.name = new_name


if __name__ == "__main__":
    dog_1 = NewDog(10, 5, "Bruce", 2)
    print(f"Old name: {dog_1.name}")    # Old name: Bruce
    dog_1.change_name("Turbo")
    print(f"New name: {dog_1.name}")    # New name: Turbo
