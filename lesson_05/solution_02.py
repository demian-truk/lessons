"""
Реализуйте алгоритм игры “Тайный Санта (Secret Santa)” - в шляпу кладутся небольшие записки с именами участников.
Затем каждый играющий по очереди вытягивает бумажку с именем того, кому предстоит вручить презент.
Ваша программа должна, используя список имен участников, выдать на выходе пары, кто и кому будет дарить.
При этом, сам себе человек не может подарить, дубликаты тоже не допустимы.
"""

party = ["Alex", "Leo", "Sasha", "Jimmy", "Ben", "Steven"]

for index in range(len(party)):
    # special case when we match last person in list to first
    if index == len(party) - 1:
        print(f"{party[index]} gives gift to {party[0]}")
    else:
        print(f"{party[index]} gives gift to {party[index + 1]}")
