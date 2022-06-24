"""
# 1:
Реализовать следующие функции для продуктов: создание, чтение, обновление по id, удаление по id.

# 2:
Реализовать покупку продукта, вывод всех покупок пользователя, фильтрацию по произвольным параметрам.
"""

from sqlalchemy.orm import sessionmaker, Session
from models import Base, User, Product, Purchase
from lesson_12.utils import setup_db_engine, create_database_if_not_exists


def create_product(
        session: Session, name: str, price: int, amount: int, comment: str
) -> Product:
    product = Product(name=name, price=price, amount=amount, comment=comment)

    session.add(product)
    session.commit()

    return product


# def update_or_create_address(
#         session: Session, user: User, city: str, address: str
# ) -> Address:
#     if len(user.addresses):
#         current_address = user.addresses[0]
#         current_address.city = city
#         current_address.address = address
#     else:
#         current_address = Address(user=user, city=city, address=address)
#
#     session.add(current_address)
#     session.commit()
#
#     return current_address


if __name__ == "__main__":
    engine = setup_db_engine()
    create_database_if_not_exists(engine=engine)

    Base.metadata.create_all(engine)
    CurrentSession = sessionmaker(bind=engine)
    current_session = CurrentSession()

    product1 = create_product(
        session=current_session,
        name="iPhone",
        price=300,
        amount=20,
        comment="Gold"
    )
