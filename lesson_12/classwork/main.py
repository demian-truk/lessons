"""
# 1:
Создать программу, которая создает таблицы для моделей в базе данных и запустить её.

# 2:
Создать функцию, которая позволяет создавать пользователя, его профиль и адрес.
Добавить 6 различных записей пользователей.

# 3:
Создать функции для добавления нового и обновления существующего адреса пользователя.

# 4:
Создать функцию для поиска всех пользователей с определенным возрастом.
"""

from sqlalchemy.orm import sessionmaker, Session
from models import Base, User, Profile, Address
from utils import setup_db_engine, create_database_if_not_exists


def create_user(session: Session, email: str, password: str, phone: str, age: int, city: str, address: str) -> User:
    user = User(email=email, password=password)
    profile = Profile(user=user, phone=phone, age=age)
    address = Address(user=user, city=city, address=address)

    session.add_all((user, profile, address))
    session.commit()

    return user


def create_or_update_address(session: Session, user: User, city: str, address: str) -> Address:
    if len(user.addresses):
        current_address = user.addresses[0]
        current_address.city = city
        current_address.address = address
    else:
        current_address = Address(user=user, city=city, address=address)

    session.add(current_address)
    session.commit()

    return current_address


def select_users_by_age(session: Session, age: int):
    users = session.query(Profile).join(User).filter(Profile.age == age).all()
    for user in users:
        print(user.user.email)


if __name__ == "__main__":
    engine = setup_db_engine()
    create_database_if_not_exists(engine=engine)

    Base.metadata.create_all(engine)
    CurrentSession = sessionmaker(bind=engine)
    current_session = CurrentSession()
