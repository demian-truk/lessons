"""
Дана база данных (в виде текстового файла) о продажах некоторого интернет-магазина.
Каждая строка входного файла представляет собой запись вида: Покупатель, Товар, Количество, Стоимость.
Где: покупатель - имя покупателя, товар - название товара, количество - количество приобретенных единиц товара.
Имя покупателя и название товара - строки без пробелов.
    a) Создайте список и выведите на экран всех покупателей.
    Для каждого покупателя подсчитайте общее количество приобретенных им товаров и их стоимость.
    b) Создайте список и выведите на экран все товары.
    Для каждого товара подсчитайте общее количество приобретенных и их стоимость.
"""

import csv


def load_sales_from_file():
    sales = []
    with open("dictionary.csv", "r") as file:
        for row in csv.reader(file):
            row[2], row[3] = int(row[2]), int(row[3])
            sales.append(row)
    return sales


def get_stats(sales, index):
    result = {}
    for row in sales:
        if row[index] in result:
            result[row[index]]["products_bought"] += row[2]
            result[row[index]]["total cost"] += row[2] * row[3]
        else:
            result[row[index]] = {
                "products_bought": row[2],
                "total cost": row[2] * row[3],
            }
    return result


def main():
    sales = load_sales_from_file()
    user_stats = get_stats(sales, index=0)
    print(f"Customer purchases: {user_stats}")
    product_stats = get_stats(sales, index=1)
    print(f"Product purchases: {product_stats}")


if __name__ == "__main__":
    main()
