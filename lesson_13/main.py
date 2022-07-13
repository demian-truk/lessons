import logging
from faker import Faker
from sqlalchemy.sql import and_
from sqlalchemy.orm import sessionmaker, Session
from models import Base, User, Profile, Address, Product, Purchase
from utils import setup_db_engine, create_database_if_not_exists

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

fake = Faker()


def create_user(session: Session, email: str, password: str, phone: str, age: int, city: str, address: str) -> User:
    user = User(email=email, password=password)
    profile = Profile(user=user, phone=phone, age=age)
    address = Address(user=user, city=city, address=address)

    session.add_all((user, profile, address))
    session.commit()

    return user


def generate_user(session: Session) -> User:
    user = User(email=fake.email(), password=fake.word())
    profile = Profile(user=user, phone=fake.phone_number(), age=fake.pyint(min_value=18, max_value=50))
    address = Address(user=user, city=fake.city(), address=fake.address())

    session.add_all((user, profile, address))
    session.commit()

    return user


def update_or_create_user_address(session: Session, user: User, email: str, city: str, address: str) -> Address:
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
        logger.info(user.user.email)


def create_product(session: Session, name: str, price: int, amount: int, comment: str) -> Product:
    product = Product(name=name, price=price, amount=amount, comment=comment)

    session.add(product)
    session.commit()

    return product


def select_products(session: Session):
    products = session.query(Product)
    for product in products:
        logger.info(
            f"Product name: {product.name}, "
            f"Price: {product.price}, "
            f"Amount: {product.amount}, "
            f"Comment: {product.comment}"
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


def generate_purchase(session: Session) -> Purchase:
    user = generate_user(session)
    product = Product(name=fake.company(), price=fake.pyint(min_value=20, max_value=200))
    purchase = Purchase(user=user, product=product, amount=fake.pyint(min_value=1, max_value=5))

    session.add_all((product, purchase))
    session.commit()

    return purchase


def select_user_purchases(session: Session, email: str):
    user_purchases = session.query(Purchase).join(Product).join(User).filter(User.email == email).all()
    for purchase in user_purchases:
        logger.info(
            f"User: {purchase.user.email}, "
            f"Product purchase name: {purchase.product.name}, "
            f"Amount: {purchase.amount}"
        )


def filter_users(session: Session):
    while True:
        choice = input(
            "Perform a filter by: \
            sum of purchase [1] or purchases of a specific product [2] or amount of product purchases [3]: "
        )
        if choice == "1":
            sum_of_purchase = int(input("Enter sum of purchase to filter: "))
            users = session.query(Purchase).join(Product).join(User).filter(
                Product.price * Purchase.amount > sum_of_purchase).all()
            for user in users:
                logger.info(user.user.email)
        elif choice == "2":
            users = session.query(Purchase).join(Product).join(User).filter(
                and_(Product.name == input("Enter product to filter: "), Purchase.amount >= 1)).all()
            for user in users:
                logger.info(user.user.email)
        elif choice == "3":
            amount_of_product_purchases = int(input("Enter amount of product purchases to filter: "))
            users = session.query(Purchase).join(Product).join(User).filter(
                Purchase.amount >= amount_of_product_purchases).all()
            for user in users:
                logger.info(user.user.email)
        else:
            break


if __name__ == "__main__":
    engine = setup_db_engine()
    create_database_if_not_exists(engine=engine)

    Base.metadata.create_all(engine)
    CurrentSession = sessionmaker(bind=engine)
    current_session = CurrentSession()
