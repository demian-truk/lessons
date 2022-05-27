"""
Пользователь вводит с клавиатуры числа до тех пор, пока не введет любой строчный символ.
Из этих чисел необходимо составить первый список. Далее таким же образом вводятся второй и третий списки.
Вывести на экран список, элементы которого есть в первых двух списках, но отсутствуют в третьем.
"""

list1 = []
list2 = []
list3 = []

# create a list of numbers

while True:
    n = input("Введите числа для 1-го списка (введите строку, чтобы закончить): ")
    if not n.isdigit():
        break
    else:
        list1.append(n)
print("1-ый список:", list1)

while True:
    n = input("Введите числа для 2-го списка (введите строку, чтобы закончить): ")
    if not n.isdigit():
        break
    else:
        list2.append(n)
print("2-ой список:", list2)

while True:
    n = input("Введите числа для 3-го списка (введите строку, чтобы закончить): ")
    if not n.isdigit():
        break
    else:
        list3.append(n)
print("3-ий список:", list3)

# print a list of numbers in the first two lists but missing in the third

new_list = set(list1) & set(list2)
new_list = set(new_list) - set(list3)
print("Новый список:", list(new_list))
