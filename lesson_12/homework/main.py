"""
# 1:
Реализовать следующие функции для продуктов: создание, чтение, обновление по id, удаление по id.

# 2:
Реализовать покупку продукта, вывод всех покупок пользователя, фильтрацию по произвольным параметрам.
"""

from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.sql import and_
from models import Base, User, Product, Purchase
from lesson_12.classwork.utils import setup_db_engine, create_database_if_not_exists


def create_product(session: Session, name: str, price: int, amount: int, comment: str) -> Product:
    product = Product(name=name, price=price, amount=amount, comment=comment)

    session.add(product)
    session.commit()

    return product


def select_products(session: Session):
    products = session.query(Product)
    for product in products:
        print(
            f"Product name: {product.name}, "
            f"Price: {product.price}, "
            f"Amount: {product.amount}, "
            f"Color: {product.comment}"
        )


def update_product_by_id(
        session: Session, product_id: int, new_name: str, new_price: int, new_amount: int, new_comment: str
):
    session.query(Product).filter_by(id=product_id).update({
        "name": new_name, "price": new_price, "amount": new_amount, "comment": new_comment
    })

    session.commit()


def delete_product_by_id(session: Session, product_id: int):
    session.query(Product).filter_by(id=product_id).delete()

    session.commit()


def product_purchase(session: Session, user_id: int, product_id: int, amount: int) -> Purchase:
    purchase = Purchase(user_id=user_id, product_id=product_id, amount=amount)

    session.add(purchase)
    session.commit()

    return purchase


def select_user_purchases(session: Session, email: str):
    user_purchases = session.query(Purchase).join(Product).join(User).filter(User.email == email).all()
    for purchase in user_purchases:
        print(
            f"User: {purchase.user.email}, "
            f"Product purchase name: {purchase.product.name}, "
            f"Amount: {purchase.amount}, "
            f"Color: {purchase.product.comment}"
        )


def filter_users(session: Session):
    while True:
        choice = input("Perform a filter by sum of purchase [1] or purchases of a specific product [2]: ")
        if choice == "1":
            sum_of_purchase = int(input("Enter sum of purchase to filter: "))
            users = session.query(Purchase).join(Product).join(User).filter(
                Product.price * Purchase.amount > sum_of_purchase).all()
            for user in users:
                print(user.user.email)
        elif choice == "2":
            users = session.query(Purchase).join(Product).join(User).filter(
                and_(Product.name == input("Enter product to filter: "), Purchase.amount >= 1)).all()
            for user in users:
                print(user.user.email)
        else:
            break


if __name__ == "__main__":
    engine = setup_db_engine()
    create_database_if_not_exists(engine=engine)

    Base.metadata.create_all(engine)
    CurrentSession = sessionmaker(bind=engine)
    current_session = CurrentSession()
