"""
Написать программу, которая будет выводить на экран случайные числа от 1 до 10 до тех пор, пока не выпадет 7.
"""

import random

# use "break"
while True:
    number = random.randint(1, 10)
    if number == 7:
        break
    print(number)

# alternative
while number != 7:
    print(number)
    number = random.randint(1, 10)
