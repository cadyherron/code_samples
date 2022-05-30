"""
Write a recursive function for generating all permutations of an input string. Return them as a set.

input = "abc"
output = {abc, acb, bca, bac, cab, cba}

"""
import sys
from typing import List


def get_permutations(string: str) -> {}:
    if len(string) <= 1:
        return {string}

    all_chars_except_last = string[:-1]
    last_char = string[-1]

    permutations_except_last = get_permutations(all_chars_except_last)

    permutations = set()
    for perm in permutations_except_last:
        for position in range(len(all_chars_except_last) + 1):
            permutation = perm[:position] + last_char + perm[position:]
            permutations.add(permutation)

    return permutations


"""
Write a function fib() that takes an integer n and returns the nth Fibonacci number
fib(0)  # => 0
fib(1)  # => 1
fib(2)  # => 1
fib(3)  # => 2
fib(4)  # => 3
"""


def fib(i: int) -> int:
    if i == 0 or i == 1:
        return i

    return fib(i - 1) + fib(i - 2)


seen = {}


def fib_memo(n: int) -> int:
    if n < 0:
        return False
    elif n in [0, 1]:
        return n

    if n in seen:
        return seen[n]

    result = fib(n - 1) + fib(n - 2)
    seen[n] = result
    return result


def coins(amount: int, denominations: List) -> int:
    ways_of_doing_n_cents = [0] * (amount + 1)
    ways_of_doing_n_cents[0] = 1
    for coin in denominations:
        print(f"calculating this coin: {coin}")
        for higher_amount in range(coin, amount + 1):
            print(f"this is higher amount: {higher_amount}")
            higher_amount_remainder = higher_amount - coin
            print(f"higher amount remainder: {higher_amount_remainder}")
            ways_of_doing_n_cents[higher_amount] += ways_of_doing_n_cents[higher_amount_remainder]
            print(f"new dict: {ways_of_doing_n_cents}")

    return ways_of_doing_n_cents[amount]


"""
Write a function max_duffel_bag_value() that takes a list of cake type tuples and a weight capacity, 
    and returns the maximum monetary value the duffel bag can hold.

For example:
    cake_tuples = [(7, 160), (3, 90), (2, 15)]  # weighs 7, value of 160
    capacity    = 20

Answer: 
    555 (6 of the middle type of cake and 1 of the last type of cake)
"""


def max_duffel_bag_value(cake_tuples: List, capacity: int) -> int:
    cake_values = [0] * (capacity + 1)
    for current_capacity in range(capacity + 1):
        current_max_value = 0
        for cake_weight, cake_value in cake_tuples:
            if cake_weight == 0 and cake_value != 0:
                return sys.maxsize
            if cake_weight <= current_capacity:
                # the value of this cake PLUS the value of the other cakes we're taking
                max_value_using_cake = cake_value + cake_values[current_capacity - cake_weight]
                current_max_value = max(max_value_using_cake, current_max_value)

        cake_values[current_capacity] = current_max_value

    return cake_values[capacity]


