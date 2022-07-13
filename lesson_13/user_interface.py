from sqlalchemy.orm import sessionmaker
from models import Base, User
from utils import setup_db_engine, create_database_if_not_exists
from main import \
    create_user, \
    generate_user, \
    update_or_create_user_address, \
    select_users_by_age, \
    create_product, \
    select_products, \
    update_product_by_id, \
    delete_product_by_id, \
    product_purchase, \
    generate_purchase, \
    select_user_purchases, \
    filter_users

TEMPLATE = """
    Choose one of options:
    1. Create new user
    2. Generate new random user
    3. Update or create user address
    4. Select users by age
    5. Create new product
    6. Output products information
    7. Update product
    8. Delete product
    9. Product purchase
    10. Generate new random user and purchase (don't work!)
    11. Output user purchases
    12. Filter users purchases
"""


def user_interface():
    while True:
        try:
            user_choice = int(input(TEMPLATE))
        except ValueError:
            user_choice = None

        if user_choice == 1:
            print("Enter information to create a new user")
            email = input("Enter email of user: ")
            password = input("Enter password of user: ")
            phone = input("Enter phone of user: ")
            age = int(input("Enter age of user: "))
            city = input("Enter city of user: ")
            address = input("Enter address of user: ")
            create_user(
                session=current_session,
                email=email,
                password=password,
                phone=phone,
                age=age,
                city=city,
                address=address
            )
        elif user_choice == 2:
            generate_user(session=current_session)
        elif user_choice == 3:
            email = input("Enter user email to update or create user address: ")
            user = current_session.query(User).filter_by(email=email).first()
            city = input("Enter city of user: ")
            address = input("Enter address of user: ")
            update_or_create_user_address(session=current_session, user=user, email=email, city=city, address=address)
        elif user_choice == 4:
            age = int(input("Enter age to select users: "))
            select_users_by_age(session=current_session, age=age)
        elif user_choice == 5:
            print("Enter information to create a new product")
            name = input("Enter name of product: ")
            price = int(input("Enter price of product: "))
            amount = int(input("Enter amount of product: "))
            comment = input("Enter some comment of product: ")
            create_product(session=current_session, name=name, price=price, amount=amount, comment=comment)
        elif user_choice == 6:
            select_products(session=current_session)
        elif user_choice == 7:
            product_id = int(input("Enter product ID to update: "))
            name = input("Enter new name of current product: ")
            price = int(input("Enter new price of current product: "))
            amount = int(input("Enter new amount of current product: "))
            comment = input("Enter new comment of current product: ")
            update_product_by_id(
                session=current_session,
                product_id=product_id,
                new_name=name,
                new_price=price,
                new_amount=amount,
                new_comment=comment
            )
        elif user_choice == 8:
            print("Enter product ID to delete: ")
            product_id = int(input())
            delete_product_by_id(session=current_session, product_id=product_id)
        elif user_choice == 9:
            user_id = int(input("Enter user ID to product purchase: "))
            product_id = int(input("Enter product ID to purchase: "))
            amount = int(input("Enter amount of product to purchase : "))
            product_purchase(session=current_session, user_id=user_id, product_id=product_id, amount=amount)
        elif user_choice == 10:
            pass
        elif user_choice == 11:
            email = input("Enter user email to output his purchases: ")
            select_user_purchases(session=current_session, email=email)
        elif user_choice == 12:
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
