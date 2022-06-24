"""
Написать функции генераторы данных для различных моделей.
"""

from faker import Faker
from sqlalchemy.orm import sessionmaker
from models import Base, User, Profile, Address, Product, Purchase
from utils import setup_db_engine, create_database_if_not_exists

fake = Faker()


def generate_user(session):
    pass


if __name__ == "__main__":
    engine = setup_db_engine()
    create_database_if_not_exists(engine=engine)

    Base.metadata.create_all(engine)
    CurrentSession = sessionmaker(bind=engine)
    current_session = CurrentSession()
