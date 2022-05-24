# add deposit conditions

deposit_amount = 2130
deposit_term = 5
percentage_payment = 0.1
deposit_bonus = 120

# calculation of deposit profitability

for i in range(5):
    # 5 == deposit_term
    deposit_amount += deposit_amount * percentage_payment + deposit_bonus

print("Deposit profitability:", deposit_amount)

Deposit profitability: 4162.9983


