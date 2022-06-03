"""
Используя функцию из предыдущей задачи, написать программу игру Блэкджек.
Для этого необходимо реализовать цикл, в котором на каждом ходу у игрока спрашивается, достать ли следующую карту.
В случае положительного ответа - вытягивать случайную карту.
Игра заканчивается если игрок отказывается брать карту, либо сумма его карт больше 21-го.
"""

from classwork_03 import random_card

card_deck = {
    "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
    "J": 2, "D": 3, "K": 4, "A": 1,
}


def card_value(nominal):
    return card_deck[nominal]


card_nominal, _ = random_card()
value = card_value(card_nominal)
current_sum = value

while True:
    print(f"Your current amount: {current_sum}")
    choice = input("Get next card [Y/n]: ")
    if choice == "n":
        break
    card_nominal, _ = random_card()
    value = card_value(card_nominal)
    current_sum += value
    if current_sum > 21:
        print(f"Game over! Your current amount: {current_sum}")
        break
    if current_sum == 21:
        print("You win")
