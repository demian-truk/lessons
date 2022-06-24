"""
Создать программу с пользовательским интерфейсом, позволяющим выбирать определенную функцию и вводить требуемые данные.
"""

from main import create_product, select_products, delete_product_by_id

TEMPLATE = """
    Choose one of options:
    1. Create new product
    2. Output products information
    3. Update by ID
    4. Delete by ID
"""
