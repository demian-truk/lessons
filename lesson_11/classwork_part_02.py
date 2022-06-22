"""
# 4:
Создать функцию для поиска всех пользователей с определенным именем.
Запустить функцию и найти хотя бы одного пользователя по имени.

# 5:
Создать функцию для поиска всех пользователей в возрасте от X до Y лет.

# 6:
Создать программу, позволяющую осуществлять поиск по имени или возрасту, оба параметра вводятся с клавиатуры.
"""

import sqlite3


def select_user(firstname: str):
    with sqlite3.connect("my_database.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            SELECT *
            FROM user
            WHERE firstname = ?;
            """,
            (firstname,)
        )
        session.commit()
        return cursor.fetchone()


if __name__ == "__main__":
    print(select_user("Levi"))
