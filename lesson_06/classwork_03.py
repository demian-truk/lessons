"""
Написать функцию, которая возвращает случайным образом одну карту из стандартной колоды в 36 карт.
При этом, на первом месте номинал карты (6 - 10, J, D, K, A).
На втором - название масти (Hearts, Diamonds, Clubs, Spades).
"""

import random

card_nominal = ("6", "7", "8", "9", "10", "J", "D", "K", "A")
card_suit = ("Hearts", "Diamonds", "Clubs", "Spades")


def random_card():
    random_nominal = random.choice(card_nominal)
    random_suit = random.choice(card_suit)
    return random_nominal, random_suit


def main():
    card = random_card()
    print(card)


if __name__ == "__main__":
    main()
