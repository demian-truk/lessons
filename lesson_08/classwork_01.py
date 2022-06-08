""""
Создать класс Dog. Класс имеет четыре атрибута: height, weight, name, age.
Класс имеет три метода: jump, run, bark. Каждый метод выводит сообщение на экран.
Создать объект класса Dog, вызвать все методы объекта и вывести на экран все его атрибуты.
"""


class Dog:

    def __init__(self, height: int, weight: int, name: str, age: int):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age

    def jump(self):
        print(f"{self.name} is jumping")

    def run(self):
        print(f"{self.name} is running")

    def bark(self):
        print(f"{self.name} is barking")


if __name__ == "__main__":
    dog_1 = Dog(10, 5, "Bruce", 2)
    dog_1.jump()
    dog_1.run()
    dog_1.bark()
    print(f"Name: {dog_1.name}, height: {dog_1.height}, weight: {dog_1.weight}, age: {dog_1.age}")
