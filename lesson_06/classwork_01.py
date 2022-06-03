"""
Дан словарь, где в качестве ключей английские слова, а значений - их перевод на русский язык.
Написать две функции, одна переводит слово с английского на русский, где слово - это входной параметр.
Вторая функция - с русского на английский.
"""

my_dict = {
    "Apple": "Яблоко",
    "House": "Дом",
    "Bear": "Медведь",
    "Road": "Дорога",
    "Pig": "Поросенок",
}


def eng_to_rus(word):
    return my_dict[word]


def rus_to_eng(word):
    for key, value in my_dict.items():
        if value == word:
            return key


print(eng_to_rus("Pig"))
print(rus_to_eng("Дорога"))
