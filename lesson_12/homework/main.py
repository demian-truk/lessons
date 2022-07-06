"""
# 1:
Реализовать следующие функции для продуктов: создание, чтение, обновление по id, удаление по id.

# 2:
Реализовать покупку продукта, вывод всех покупок пользователя, фильтрацию по произвольным параметрам.
"""

from sqlalchemy.orm import sessionmaker, Session
from models import Base, Product
from lesson_12.classwork.utils import setup_db_engine, create_database_if_not_exists


def create_product(session: Session, name: str, price: int, amount: int, comment: str) -> Product:
    product = Product(name=name, price=price, amount=amount, comment=comment)

    session.add(product)
    session.commit()

    return product


def select_products():
    all_products = current_session.query(Product)
    for prod in all_products:
        print(f"Name: {prod.name}, price: {prod.price}, amount: {prod.amount}, comment: {prod.comment}")


def delete_product_by_id(session: Session, id_number: int):
    current_session.query(Product).filter_by(id=id_number).delete()

    session.commit()


if __name__ == "__main__":
    engine = setup_db_engine()
    create_database_if_not_exists(engine=engine)

    Base.metadata.create_all(engine)
    CurrentSession = sessionmaker(bind=engine)
    current_session = CurrentSession()
