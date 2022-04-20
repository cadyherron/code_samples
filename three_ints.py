"""
Given a list of integers, find the highest product you can get from three of the integers.

The input list_of_ints will always have at least three integers.
"""
# can we just find the largest product of 2 integers, and then find the largest int?
# what if they're negative? 2 negatives * 1 positive
# let's sort the list first


def highest_product(list_of_ints):
    highest = max(list_of_ints[0], list_of_ints[1])
    lowest = min(list_of_ints[0], list_of_ints[1])
    highest_product_of_2 = list_of_ints[0] * list_of_ints[1]
    lowest_product_of_2 = list_of_ints[0] * list_of_ints[1]
    highest_product_of_3 = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]

    for i in range(2, len(list_of_ints)):
        current = list_of_ints[i]
        highest_product_of_3 = max(highest_product_of_3,
                                   current * highest_product_of_2,
                                   current * lowest_product_of_2)
        highest_product_of_2 = max(highest_product_of_2,
                                   current * highest,
                                   current * lowest)
        lowest_product_of_2 = min(lowest_product_of_2,
                                  current * highest,
                                  current * lowest)
        highest = max(highest, current)
        lowest = min(lowest, current)

    return highest_product_of_3
