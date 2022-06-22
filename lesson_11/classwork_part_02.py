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


def select_user_by_firstname(firstname: str):
    with sqlite3.connect("user.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            SELECT *
            FROM user
            WHERE firstname = ?;
            """,
            (firstname,),
        )
        session.commit()
        return cursor.fetchone()


def select_user_by_age(from_age: int, to_age: int):
    with sqlite3.connect("user.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            SELECT *
            FROM user
            WHERE age > ? and age < ?;
            """,
            (from_age, to_age),
        )
        session.commit()
        return cursor.fetchall()


def select_user_by_firstname_or_age(firstname: str, age: int):
    with sqlite3.connect("user.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            SELECT *
            FROM user
            WHERE firstname == ? or age == ?;
            """,
            (firstname, age),
        )
        session.commit()
        return cursor.fetchall()


if __name__ == "__main__":
    print(select_user_by_firstname("Levi"))
    print(select_user_by_age(22, 34))
    select_name = input("Enter firstname for select: ")
    select_age = int(input("Enter age to select: "))
    print(select_user_by_firstname_or_age(select_name, select_age))
