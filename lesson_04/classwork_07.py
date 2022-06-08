"""
Пользователь вводит с клавиатуры числа до тех пор, пока не введет любой строчный символ.
Из этих чисел необходимо составить первый список. Далее таким же образом вводятся второй и третий списки.
Вывести на экран список, элементы которого есть в первых двух списках, но отсутствуют в третьем.
"""

list1 = []
list2 = []
list3 = []

# create list of numbers
while True:
    number = input("Enter numbers for 1st list (enter string to stop): ")
    if not number.isdigit():
        break
    else:
        list1.append(number)

while True:
    number = input("Enter numbers for 2nd list (enter string to stop): ")
    if not number.isdigit():
        break
    else:
        list2.append(number)

while True:
    number = input("Enter numbers for 3rd list (enter string to stop): ")
    if not number.isdigit():
        break
    else:
        list3.append(number)

# output list of numbers in first two lists but missing in third
new_list = set(list1) & set(list2)
new_list = set(new_list) - set(list3)
print(f"New list: {list(new_list)}")
