"""
Ввести с клавиатуры строку, проверить является ли строка палиндромом и вывести результат (yes/no) на экран.
Палиндром - это слово или фраза, которые одинаково читаются слева направо и справа налево.
"""

my_str = str(input("Введите слово или фразу: "))
new_str = my_str.replace(" ", "")
new_str = my_str.lower()

# check for palindrome using construction [::-1]

if new_str == new_str[::-1]:
    print("Строка", new_str, "является палиндромом")
else:
    print("Строка", new_str, "не является палиндромом")

# check for palindrome using function "reversed"

if new_str == "".join(reversed(new_str)):
    print("Строка", new_str, "является палиндромом")
else:
    print("Строка", new_str, "не является палиндромом")
