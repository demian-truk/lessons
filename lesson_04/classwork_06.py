"""
Вывести в порядке возрастания все простые числа, расположенные между n и m (включая сами числа n и m).
Также вывести количество x этих чисел.
"""

n = int(input("Введите первое число: "))
m = int(input("Введите второе число: "))
new_list = []

# find prime numbers

for number in range(n, m+1):
    if number > 1:
        for num in range(2, number):
            if number % num == 0:
                break
        else:
            new_list.append(number)
print("Список всех простых чисел в диапазоне:", new_list)

# output amount of prime numbers

x = len(new_list)
print("Количество простых чисел:", x)
