"""
Пользователь делает вклад в размере 2130 рублей сроком на 5 лет под 10% годовых.
Рассчитать сумму на счету пользователя по окончании вклада и вывести её на печать.
При этом в конце каждого года пользователю начисляется бонус в размере 120 рублей.
"""

deposit_amount = 2130
deposit_term = 5
percentage_payment = 0.1
deposit_bonus = 120

# calculation of deposit profitability

for i in range(5):    # 5 == deposit_term
    deposit_amount += deposit_amount * percentage_payment + deposit_bonus
print("Deposit profitability:", deposit_amount)
