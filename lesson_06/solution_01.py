"""
Напишите программу, которая принимает текст и выводит два слова.
Первое - это наиболее часто встречающееся слово, второе - самое длинное.
В идеале не использовать библиотечные функции.
"""

MIN_WORD_LENGTH = 3


def most_common_word_in_text(text):
    pass


# using function "max"
def max_len_of_word_in_text(text):
    text = text.split()
    max_len = max(text, key=len)
    return max_len


my_text = "Hello, I'm Dima. I love computer games. Games take a lot of time. But it's a lot of fun. Games forever :)"

print(most_common_word_in_text(my_text))
print(max_len_of_word_in_text(my_text))    # computer
