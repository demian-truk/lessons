"""
Напишите программу, которая принимает текст и выводит два слова.
Первое - это наиболее часто встречающееся слово, второе - самое длинное.
В идеале не использовать библиотечные функции.
"""

my_text = "Hello, I'm Dima. I love computer games. Games take a lot of time. But it's a lot of fun. Games forever :)"
my_text = my_text.split()


def max_len_of_word_in_text(text):
    max_len = max(my_text, key=len)
    return max_len


def most_common_word_in_text(text):
    pass


print(max_len_of_word_in_text(my_text))
