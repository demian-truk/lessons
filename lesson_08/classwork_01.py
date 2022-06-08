""""
Создать класс Dog. Класс имеет четыре атрибута: height, weight, name, age.
Класс имеет три метода: jump, run, bark. Каждый метод выводит сообщение на экран.
Создать объект класса Dog, вызвать все методы объекта и вывести на экран все его атрибуты.

# Upd - Программа имеет другой вид, получившийся после решения задания №4.
"""

from classwork_04 import Animal


class Dog(Animal):

    def talk(self):
        print(f"{self.name} is barking")


if __name__ == "__main__":
    dog_1 = Dog(10, 5, "Bruce", 2)
    dog_1.jump()
    dog_1.run()
    dog_1.talk()
    print(f"Name: {dog_1.name}, height: {dog_1.height}, weight: {dog_1.weight}, age: {dog_1.age}")
