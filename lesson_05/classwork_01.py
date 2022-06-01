"""
Написать функцию, которая получает на вход имя и выводит строку вида: f"Hello, {name}".
Создать список из 5 имен. Вызвать функцию для каждого элемента списка в цикле.
"""

my_names = ["Alex", "Sandra", "Ben", "Johnny", "Pit"]

def format_string(name):
    print(f"Hello, {name}")

for name in my_names:
    format_string(name)
