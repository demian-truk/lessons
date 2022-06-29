"""
# 1:
Создать программу, которая создает таблицы для моделей в базе данных и запустить её, проверить наличие таблиц.

# 2:
Написать функции генераторы данных для различных моделей.

# 3:
Создать функцию для поиска пользователей, у которых были покупки стоимостью более Х у.е.

# 4:
Создать функцию для поиска пользователей, которые покупали определенный товар (по названию товара).
"""

from faker import Faker
from sqlalchemy.sql import and_
from sqlalchemy.orm import sessionmaker, Session
from models import Base, User, Profile, Address, Product, Purchase
from utils import setup_db_engine, create_database_if_not_exists

fake = Faker()


def generate_user(session: Session) -> User:
    user = User(email=fake.email(), password=fake.word())
    profile = Profile(user=user, phone=fake.phone_number(), age=fake.pyint(min_value=18, max_value=50))
    address = Address(user=user, city=fake.city(), address=fake.address())

    session.add_all((user, profile, address))
    session.commit()

    return user


def generate_purchase(session: Session):
    user = generate_user(session)
    product = Product(name=fake.company(), price=fake.pyint(min_value=20, max_value=200))
    purchase = Purchase(user=user, product=product, amount=fake.pyint(min_value=1, max_value=5))

    session.add_all((product, purchase))
    session.commit()


def select_user(all_users):
    for user in all_users:
        print(user.user.email)


if __name__ == "__main__":
    engine = setup_db_engine()
    create_database_if_not_exists(engine=engine)

    Base.metadata.create_all(engine)
    CurrentSession = sessionmaker(bind=engine)
    current_session = CurrentSession()

    select_user_by_sum_of_purchase = \
        current_session.query(Purchase).join(Product).join(User).filter(Product.price * Purchase.amount > 400).all()
    select_user(select_user_by_sum_of_purchase)

    select_user_by_purchase_of_product = \
        current_session.query(Purchase).join(Product).join(User).filter(
            and_(Product.name == "Sushi", Purchase.amount > 2)).all()
    select_user(select_user_by_purchase_of_product)
