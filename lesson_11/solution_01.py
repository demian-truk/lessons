"""
Создать таблицу продуктов. Атрибуты продукта: id, название, цена, количество, комментарий.
Реализовать следующие функции для продуктов: создание, чтение, обновление по id, удаление по id.
"""

import sqlite3


def create_product(name: str, price: int, amount: int, comment):
    with sqlite3.connect("products.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            INSERT INTO my_products (name, price, amount, comment)
            VALUES (?, ?, ?, ?);
            """,
            (name, price, amount, comment),
        )
        session.commit()
