"""
Найти в данном списке количество не уникальных элементов:
my_list = [1, 1.0, 2, 2, 5.0, "python", "python3", "python3"]
"""

my_list = [1, 1.0, 2, 2, 5.0, "python", "python3", "python3"]

amount_of_non_unique_elements = len(my_list) - len(set(my_list))
print(amount_of_non_unique_elements)    # 3
