"""
Написать функцию month_to_season(), которая принимает 1 аргумент - номер месяца.
Функция возвращает название сезона, к которому относится этот месяц.
Например, передаем 2, на выходе получаем "Winter".
"""

def month_to_season(month):
    mapping = {
        "Winter": [1, 2, 12],
        "Spring": [3, 4, 5],
        "Summer": [6, 7, 8],
        "Autumn": [9, 10, 11],
    }
    for season, month_list in mapping.items():
        if month in month_list:
            return season

print(month_to_season(7))
