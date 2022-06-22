"""
Создать таблицу продуктов. Атрибуты продукта: id, название, цена, количество, комментарий.
Реализовать следующие функции для продуктов: создание, чтение, обновление по id, удаление по id.
"""

import sqlite3


def create_product(name: str, price: int, amount: int, comment: str):
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


def select_product(name: str):
    with sqlite3.connect("products.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            SELECT *
            FROM my_products
            WHERE name == ?;
            """,
            (name,),
        )
        session.commit()
        return cursor.fetchall()


def update_product(product_id: int, name: str, price: int, amount: int, comment: str):
    with sqlite3.connect("products.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            UPDATE my_products
            SET name == ?,
            amount == ?,
            price == ?,
            comment == ?
            WHERE id == ?;
            """,
            (name, amount, price, comment, product_id),
        )
        session.commit()
        return cursor.fetchone()


def delete_product(product_id: int):
    with sqlite3.connect("products.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            DELETE FROM my_products
            WHERE id == ?;
            """,
            (product_id,),
        )
        session.commit()
        return cursor.fetchone()
