"""
Создать программу с пользовательским интерфейсом, позволяющим выбирать определенную функцию и вводить требуемые данные.
"""

from sqlalchemy.orm import sessionmaker
from models import Base
from lesson_12.classwork.utils import setup_db_engine, create_database_if_not_exists
from main import \
    create_product, \
    select_products, \
    update_product_by_id, \
    delete_product_by_id, \
    product_purchase, \
    select_user_purchases, \
    filter_users

TEMPLATE = """
    Choose one of options:
    1. Create new product
    2. Output products information
    3. Update product
    4. Delete product
    5. Product purchase
    6. Output user purchases
    7. Filter purchases
"""


def user_interface():
    while True:
        try:
            user_choice = int(input(TEMPLATE))
        except ValueError:
            user_choice = None

        if user_choice == 1:
            print("Enter information to create a new product")
            name = input("Enter name of product: ")
            price = int(input("Enter price of product: "))
            amount = int(input("Enter amount of product: "))
            comment = input("Enter color of product: ")
            create_product(session=current_session, name=name, price=price, amount=amount, comment=comment)
        elif user_choice == 2:
            select_products(session=current_session)
        elif user_choice == 3:
            product_id = int(input("Enter product ID to update: "))
            name = input("Enter new name of current product: ")
            price = int(input("Enter new price of current product: "))
            amount = int(input("Enter new amount of current product: "))
            comment = input("Enter new color of current product: ")
            update_product_by_id(
                session=current_session,
                product_id=product_id,
                new_name=name,
                new_price=price,
                new_amount=amount,
                new_comment=comment
            )
        elif user_choice == 4:
            print("Enter product ID to delete: ")
            product_id = int(input())
            delete_product_by_id(session=current_session, product_id=product_id)
        elif user_choice == 5:
            user_id = int(input("Enter user ID to product purchase: "))
            product_id = int(input("Enter product ID to purchase: "))
            amount = int(input("Enter amount of product to purchase : "))
            product_purchase(session=current_session, user_id=user_id, product_id=product_id, amount=amount)
        elif user_choice == 6:
            email = input("Enter user email to output his purchases: ")
            select_user_purchases(session=current_session, email=email)
        elif user_choice == 7:
            filter_users(session=current_session)
        else:
            break


if __name__ == "__main__":
    engine = setup_db_engine()
    create_database_if_not_exists(engine=engine)

    Base.metadata.create_all(engine)
    CurrentSession = sessionmaker(bind=engine)
    current_session = CurrentSession()

    user_interface()
