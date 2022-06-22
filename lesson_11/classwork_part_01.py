"""
# 1:
Установить библиотеку sqlite3 в операционную систему.

# 2:
Используя консоль, создать базу sqlite3.
В базе создать таблицу user, для примера использовать слайд №12, добавить новую запись, прочитать её и изменить.
Подключить базу в PyCharm.

# 3:
Создать функцию, которая позволяет добавлять данные в таблицу user. Добавить 5 различных записей.
"""

import sqlite3


def create_user(firstname: str, lastname: str, email: str, password: str, age: int):
    with sqlite3.connect("my_database.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            INSERT INTO user (firstname, lastname, email, password, age)
            VALUES (?, ?, ?, ?, ?);
            """,
            (firstname, lastname, email, password, age),
        )
        session.commit()


if __name__ == "__main__":
    create_user("Levi", "Ackerman", "levilevilevi@gmail.com", "TestPass2", 31)
    create_user("Mikasa", "Ackerman", "cutemikasssa@gmail.com", "TestPass3", 22)
    create_user("Historia", "Reiss", "reissispower@gmail.com", "TestPass4", 20)
    create_user("Reiner", "Braun", "fatfatreinr25@gmail.com", "TestPass5", 25)
    create_user("Armin", "Arlert", "arminarlert-anime@gmail.com", "TestPass6", 21)
