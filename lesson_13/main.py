"""
# 1:
Добавить функцию вывода всех товаров, купленных определенным пользователем.

# 2:
Добавить фильтрацию пользователей по купленным товарам.
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


def select_user_by_sum_of_purchase(sum_of_purchase: int):
    users = current_session.query(Purchase).join(Product).join(User).filter(
        Product.price * Purchase.amount > sum_of_purchase).all()
    for user in users:
        print(user.user.email)


def select_user_by_purchase_of_product():
    users = current_session.query(Purchase).join(Product).join(User).filter(
            and_(Product.name == input("Enter product for select: "), Purchase.amount >= 1)).all()
    for user in users:
        print(user.user.email)


if __name__ == "__main__":
    engine = setup_db_engine()
    create_database_if_not_exists(engine=engine)

    Base.metadata.create_all(engine)
    CurrentSession = sessionmaker(bind=engine)
    current_session = CurrentSession()
