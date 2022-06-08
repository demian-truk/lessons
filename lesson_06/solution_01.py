"""
Напишите программу, которая принимает текст и выводит два слова.
Первое - это наиболее часто встречающееся слово, второе - самое длинное.
В идеале не использовать библиотечные функции.
"""

MIN_WORD_LENGTH = 4


def get_text_stats(text: str) -> dict:
    text = text.lower()
    text = text.replace(".", " ").replace(",", " ").split()
    result = {}
    for word in text:
        word = word.strip()
        if len(word) < MIN_WORD_LENGTH:
            continue
        if word in result:
            result[word]["count"] += 1
        else:
            result[word] = {
                "length": len(word),
                "count": 1,
            }
    return result


def get_most_frequent_word(text_stats: dict) -> str:
    most_frequent = list(text_stats.keys())[0]
    for word, stats in text_stats.items():
        if text_stats[most_frequent]["count"] < stats["count"]:
            most_frequent = word
    return most_frequent


def get_the_longest_word(text_stats: dict) -> str:
    longest = list(text_stats.keys())[0]
    for word, stats in text_stats.items():
        if text_stats[longest]["length"] < stats["length"]:
            longest = word
    return longest


# get the longest word using function "max"
"""
def get_longest_word(text):
    text = text.split()
    max_len = max(text, key=len)
    return max_len
"""

my_text = "Hello, I'm Dima. I love computer games. Games take a lot of time. But it's a lot of fun. Games forever :)"
my_stats = get_text_stats(my_text)

print(f"Most frequent word in text: {get_most_frequent_word(my_stats)}")    # Most frequent word in text: games
print(f"The longest word in text: {get_the_longest_word(my_stats)}")    # The longest word in text: computer
