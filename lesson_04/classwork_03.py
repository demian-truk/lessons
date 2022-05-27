"""
Ввести с клавиатуры целое число n. Получить сумму кубов всех целых чисел от 1 до n (включая n), используя цикл while.
"""

n = int(input("Enter any integer: "))
sum_of_cubes_of_numbers = 0

while n > 0:
    sum_of_cubes_of_numbers += n ** 3
    n -= 1
print(sum_of_cubes_of_numbers)
