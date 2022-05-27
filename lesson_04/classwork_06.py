"""
Вывести в порядке возрастания все простые числа, расположенные между n и m (включая сами числа n и m).
Также вывести количество x этих чисел.
"""

n = int(input("Введите первое число: "))
m = int(input("Введите второе число: "))
result = []

# find prime numbers

for number in range(n, m+1):
    if number > 1:
        for num in range(2, number):
            if number % num == 0:
                break
        else:
            result.append(number)
print("Список всех простых чисел в диапазоне:", result)

# output amount of prime numbers

x = len(result)
print("Количество простых чисел:", x)
