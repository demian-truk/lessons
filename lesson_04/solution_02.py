"""
Ввести с клавиатуры строку, проверить является ли строка палиндромом и вывести результат (yes/no) на экран.
Палиндром - это слово или фраза, которые одинаково читаются слева направо и справа налево.
"""

my_str = str(input("Enter word or phrase: "))
new_str = my_str.replace(" ", "")

# check for palindrome using construction [::-1]
if new_str == new_str[::-1]:
    print("String", new_str, "is palindrome")
else:
    print("String", new_str, "is not palindrome")

# check for palindrome using function "reversed"
if new_str == "".join(reversed(new_str)):
    print("String", new_str, "is palindrome")
else:
    print("String", new_str, "is not palindrome")
