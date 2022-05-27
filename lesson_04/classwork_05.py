"""
Получить сумму кубов натуральных чисел от n до m, используя цикл for, числа n и m вводятся с клавиатуры.
"""

n = int(input("Enter first natural number: "))
m = int(input("Enter second natural number: "))
sum_of_cubes_of_numbers = 0

for number in range(n, m):
    sum_of_cubes_of_numbers += number ** 3
print(sum_of_cubes_of_numbers)
