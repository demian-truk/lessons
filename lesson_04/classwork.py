# Exercise 1
"""
Дан произвольный список, содержащий только числа. Выведите результат сложения всех чисел больше 10.
"""

numbers = [1, 3, 15, 7, 25, 34, 11, 4]
result = 0

for number in numbers:
    if number > 10:
        result += number
print(result)

# Exercise 2
"""
Написать программу, которая выведет на экран все числа от 1 до 100, которые кратные n (n вводится с клавиатуры).
"""

n = int(input("Введите любое число: "))

for number in range(1, 101):
    if number % n == 0:
        print(number)

# Exercise 3
"""
Ввести с клавиатуры целое число n. Получить сумму кубов всех целых чисел от 1 до n (включая n) используя цикл while.
"""

n = int(input("Введите любое целое число: "))
result = 0

while n > 0:
    result += n ** 3
    n -= 1
print(result)

# Exercise 4
"""
Написать программу, которая будет выводить на экран случайные числа от 1 до 10 до тех пор, пока не выпадет 7.
"""

import random

while True:
    n = random.randint(1, 10)
    if n == 7:
        break
    print(n)

while n != 7:
    print(n)
    n = random.randint(1, 10)

