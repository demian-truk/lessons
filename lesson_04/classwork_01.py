"""
Дан произвольный список, содержащий только числа. Выведите результат сложения всех чисел больше 10.
"""

numbers = [1, 3, 15, 7, 25, 34, 11, 4]
result = 0

for number in numbers:
    if number > 10:
        result += number
print(result)
