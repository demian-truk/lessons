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


def customer_purchases(sales):
    sales_dict = {customer: [] for customer, product, amount, price in sales}
    for customer, product, amount, price in sales:
        sales_dict[customer].append([product, amount, price])
    for key, value in sales_dict.items():
        sum_of_amount_of_products = 0
        cost_of_products = 0
        res_dict = {}
        res_list = []
        for i in value:
            sum_of_amount_of_products += int(i[1])
            cost_of_products += int(i[1]) * int(i[2])
            res_list = [sum_of_amount_of_products, cost_of_products]
        res_dict[key] = res_list
        for k, v in res_dict.items():
            print(f"{k}: total amount of products - {v[0]}, total cost of products - {v[1]}")


def product_purchases(sales):
    pass


def main():
    sales = []
    with open("dictionary.csv", "r") as file:
        for row in csv.reader(file):
            sales.append(row)
    customer_purchases(sales)


if __name__ == "__main__":
    main()
