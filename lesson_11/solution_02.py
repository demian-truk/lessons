"""
Создать программу с пользовательским интерфейсом, позволяющим выбирать определенную функцию и вводить требуемые данные.
"""

from solution_01 import create_product, select_product, update_product, delete_product

TEMPLATE = """
    Choose one of options:
    1. Create new product
    2. Output products information
    3. Update by ID
    4. Delete by ID
"""


def user_menu():
    while True:
        try:
            user_choice = int(input(TEMPLATE))
        except ValueError:
            user_choice = None

        if user_choice == 1:
            print("Enter name, price, amount and comment separated by commas: ")
            name, price, amount, comment = input().split(',')
            create_product(name, int(price), int(amount), comment)
        elif user_choice == 2:
            for product in select_product():
                print(product)
        elif user_choice == 3:
            print("Enter product_id, name, price, amount and comment by commas for update: ")
            product_id, name, price, amount, comment = input().split(',')
            update_product(int(product_id), name, int(price), int(amount), comment)
        elif user_choice == 4:
            print("Enter product_id for delete: ")
            product_id = int(input())
            delete_product(product_id)
        else:
            break


if __name__ == "__main__":
    user_menu()
