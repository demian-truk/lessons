"""
# 1:
Создать программу, которая создает таблицы для моделей в базе данных и запустить её, проверить наличие таблиц.

# 2:
Написать функции генераторы данных для различных моделей.
"""

from faker import Faker
from sqlalchemy.orm import sessionmaker, Session
from models import Base, User, Profile, Address, Product, Purchase
from utils import setup_db_engine, create_database_if_not_exists

fake = Faker()


def generate_user(session: Session) -> User:
    user = User(email=fake.email(), password=fake.word())
    profile = Profile(user=user, phone=fake.phone_number(), age=fake.pyint(min_value=18, max_value=50))
    address = Address(user=user, city=fake.city(), address=fake.address())

    session.add_all([user, profile, address])
    session.commit()

    return user


if __name__ == "__main__":
    engine = setup_db_engine()
    create_database_if_not_exists(engine=engine)

    Base.metadata.create_all(engine)
    CurrentSession = sessionmaker(bind=engine)
    current_session = CurrentSession()

    for _ in range(10):
        generate_user(current_session)
