"""
В школе решили набрать три новых класса по программированию.
Так как занятия у них проходят в одно и то же время, было решено выделить кабинет для каждого класса.
В каждый класс также необходимо купить новые парты. За каждой партой может сидеть не больше двух учеников.
Известно количество учащихся в каждом из трёх классов.
Сколько всего нужно закупить парт, чтобы их хватило на всех учеников?
Программа получает на вход три натуральных числа: количество учащихся в каждом из трех классов.
"""

class_01 = int(input("Enter number of students in class: "))
class_02 = int(input("Enter number of students in class: "))
class_03 = int(input("Enter number of students in class: "))
classes = [class_01, class_02, class_03]


def number_of_desks(classes):
    desks = 0
    for desk in classes:
        desks += desk // 2
        if desk % 2 == 1:
            desks += 1
    return desks


print(number_of_desks(classes))
