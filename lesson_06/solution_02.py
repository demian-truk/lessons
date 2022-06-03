"""
В школе решили набрать три новых класса по программированию.
Так как занятия у них проходят в одно и то же время, было решено выделить кабинет для каждого класса.
В каждый класс также необходимо купить новые парты. За каждой партой может сидеть не больше двух учеников.
Известно количество учащихся в каждом из трёх классов.
Сколько всего нужно закупить парт, чтобы их хватило на всех учеников?
Программа получает на вход три натуральных числа: количество учащихся в каждом из трех классов.
"""


def amount_of_desks(class_01, class_02, class_03):
    desks = 0
    for desk in class_01, class_02, class_03:
        desks += desk // 2
        if desk % 2 == 1:
            desks += 1
    return desks


print(amount_of_desks(11, 13, 14))    # 20