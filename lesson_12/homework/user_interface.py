"""
^^Создать программу с пользовательским интерфейсом, позволяющим выбирать определенную функцию и вводить требуемые данные.^^
"""

from main import create_product, select_products, delete_product_by_id

TEMPLATE = """
    Choose one of options:
    1. Create new product
    2. Output products information
    3. Update by ID
    4. Delete by ID
"""


def user_interface():
    while True:
        try:
            user_choice = int(input(TEMPLATE))
        except ValueError:
            user_choice = None

        if user_choice == 1:
            pass
        elif user_choice == 2:
            pass
        elif user_choice == 3:
            pass
        elif user_choice == 4:
            pass
        else:
            break


if __name__ == "__main__":
    user_interface()
