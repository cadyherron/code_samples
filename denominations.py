"""
Write a function that, given:

1. an amount of money
2. a list of coin denominations

computes the number of ways to make the amount of money with coins of the available denominations.

Example: for amount=4 (4¢) and denominations=[1,2,3] (1¢, 2¢ and 3¢),
    your program would output 4—the number of ways to make 4¢ with those denominations:

1¢, 1¢, 1¢, 1¢
1¢, 1¢, 2¢
1¢, 3¢
2¢, 2¢

"""
# what are the possible permutations where sum = amount?
# we can use a coin unlimited times
# how do we do this by hand?
# start with smallest, see if amount % smallest is 0, then do amount / smallest
# move to the next one and repeat; then we check if the remainder is one of the other coins
# the remainder might be TWO coins: amount = 8, denominations = [6,1]
from typing import List


def number_of_ways(amount: int, denominations: List[int]) -> int:
    return 0
