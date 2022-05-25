"""
Найти в списке ниже количество не уникальных элементов:
my_list = [1, 1.0, 2, 2, 5.0, "python", "python3", "python3"]
"""

my_list = [1, 1.0, 2, 2, 5.0, "python", "python3", "python3"]
result = len(my_list) - len(set(my_list))
print(result)
