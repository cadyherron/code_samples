"""
List of integers where:
1. Integers are in the range 1..n
2. The list has a length of n + 1

example:
n is 6
n + 1 is 7
[1,6,5,2,3,4,4]

at least one integer appears at least twice
but there can be several duplicates, and each duplicate could appear more than twice

Write a function which finds an integer that appears more than once in our list.
Don't modify the input! (If there are multiple duplicates, you only need to find one of them.)
"""


def find_a_duplicate(ints):
    set_of_ints = set(ints)
    for i in ints:
        if i in set_of_ints:
            set_of_ints.remove(i)
        else:
            return i


def find_repeat(numbers):
    floor = 1
    ceiling = len(numbers) - 1
    while floor < ceiling:
        midpoint = floor + ((ceiling - floor) // 2)
        lower_range_floor = floor
        lower_range_ceiling = midpoint
        upper_range_floor = midpoint + 1
        upper_range_ceiling = ceiling

        items_in_lower_range = 0
        for item in numbers:
            if item >= lower_range_floor and item <= lower_range_ceiling:
                items_in_lower_range += 1

        distinct_in_lower_range = (lower_range_ceiling - lower_range_floor + 1)
        if items_in_lower_range > distinct_in_lower_range:
            floor = lower_range_floor
            ceiling = lower_range_ceiling
        else:
            floor = upper_range_floor
            ceiling = upper_range_ceiling

    return floor
