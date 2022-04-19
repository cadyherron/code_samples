"""
Given all three lists, write a function to check that my service is first-come, first-served.
All food should come out in the same order customers requested it.

BAD
Take Out Orders: [1, 3, 5]
 Dine In Orders: [2, 4, 6]
  Served Orders: [1, 2, 4, 6, 5, 3]


GOOD
Take Out Orders: [17, 8, 24]
 Dine In Orders: [12, 19, 2]
  Served Orders: [17, 8, 12, 19, 24, 2]
"""


def first_come_first_served(take_out_orders, dine_in_orders, served_orders):
    take_out_index = 0
    dine_in_index = 0
    for order in served_orders:
        take_out_exhausted = take_out_index >= len(take_out_orders) - 1
        dine_in_exhausted = dine_in_index >= len(dine_in_orders) - 1

        if order == take_out_orders[take_out_index]:
            if not take_out_exhausted:
                take_out_index += 1
        elif order == dine_in_orders[dine_in_index]:
            if not dine_in_exhausted:
                dine_in_index += 1
        else:
            return False

    return True
