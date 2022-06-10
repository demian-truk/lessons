"""
Дан список стран и городов каждой страны, где ключи это названия стран, а значения - списки городов в этих странах.
Написать функцию, которая осуществляет поиск по городу и возвращает страну.
Оформить в виде программы, которая считывает название города и выводит на печать страну.
"""


def city_to_country(city):
    countries_and_cities = {
        "USA": ["Detroit", "Chicago", "Dallas"],
        "Italy": ["Milan", "Rome", "Turin"],
        "Spain": ["Madrid", "Barcelona", "Valencia"],
        "France": ["Paris", "Lyon", "Marseille"],
        "Belarus": ["Minsk", "Brest", "Kobrin"],
    }
    for country, cities_list in countries_and_cities.items():
        if city in cities_list:
            return country


if __name__ == "__main__":
    print(city_to_country("Rome"))    # Italy
