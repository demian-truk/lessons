"""
Получить сумму кубов натуральных чисел от n до m, используя цикл for, числа n и m вводятся с клавиатуры.
"""

n = int(input("Введите первое натуральное число: "))
m = int(input("Введите второе натуральное число: "))
sum_of_cubes_of_numbers = 0

for number in range(n, m):
    sum_of_cubes_of_numbers += number ** 3
print(sum_of_cubes_of_numbers)
