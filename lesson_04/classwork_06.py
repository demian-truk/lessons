"""
Вывести в порядке возрастания все простые числа, расположенные между n и m (включая сами числа n и m).
Также вывести количество x этих чисел.
"""

n = int(input("Enter first number: "))
m = int(input("Enter second number: "))
new_list = []

# find primes
for number in range(n, m+1):
    if number > 1:
        for divider in range(2, number):
            if number % divider == 0:
                break
        else:
            new_list.append(number)
print("List of all primes in the current range:", new_list)

# output amount of primes
amount_of_primes = len(new_list)
print("Amount of primes:", amount_of_primes)
