"""
Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products.

For example, given:

  [1, 7, 3, 4]

your function would return:

  [84, 12, 28, 21]

by calculating:

  [7 * 3 * 4,  1 * 3 * 4,  1 * 7 * 4,  1 * 7 * 3]

Here's the catch: You can't use division in your solution!
"""
# ideally move through the array one time
# if i could use division: multiply all numbers together, then divide by the current index's number (two passes)
# can i use another data structure? set doesn't really help... dictionary?
# how else are the resulting numbers related?
# does sorting help?
# what's the greedy solution?


def get_products_of_all_ints_with_division(ints):
    product = 1
    for i in ints:
        product = product * i

    return [product / i for i in ints]


def get_products_of_all_ints_except_at_index(ints):
    if len(ints) < 2:
        raise IndexError("Please provide at least 2 numbers")

    left_product = 1
    result = []
    for index, num in enumerate(ints):
        right_product = 1
        for r in ints[index + 1:]:
            right_product = right_product * r
        result.append(left_product * right_product)
        left_product = left_product * ints[index]

    return result


def binary_search(target, nums):
    floor_index = -1
    ceiling_index = len(nums)
    while floor_index + 1 < ceiling_index:
        distance = ceiling_index - floor_index
        half_distance = distance // 2
        guess_index = floor_index + half_distance
        guess_value = nums[guess_index]

        if guess_value == target:
            return True
        if guess_value > target:
            ceiling_index = guess_index
        else:
            floor_index = guess_index

    return False
