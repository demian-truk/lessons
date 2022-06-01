"""
Написать функцию, которая используя модуль requests скачивает файл и сохраняет его на файловой системе.
Функция имеет два параметра: ссылка на файл и имя на файловой системе.
В качестве примера ссылки на файл можно использовать лицензию из ГитХаба из вашего репозитория.
"""

import requests

def download_and_save(link, name):
    with open(name, "wb") as file:
        link = requests.get(link)
        file.write(link.content)

download_and_save("https://raw.githubusercontent.com/demian-truk/lessons/master/LICENSE", "License")
