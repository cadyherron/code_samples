"""
Write an efficient function that takes stock_prices and returns the best profit I could have made from one purchase
    and one sale of one share of Apple stock yesterday.

For example:

  stock_prices = [10, 7, 5, 8, 11, 9]

    get_max_profit(stock_prices)
    # Returns 6 (buying for $5 and selling for $11)

No "shorting" — you need to buy before you can sell.
Also, you can't buy and sell in the same time step—at least 1 minute has to pass.
"""
from typing import List


def get_max_profit(stock_prices):
    min_price = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]
    for current_time in range(1, len(stock_prices)):
        current_price = stock_prices[current_time]
        potential_profit = current_price - min_price
        max_profit = max(max_profit, potential_profit)
        min_price = min(min_price, current_price)

    return max_profit


def max_profit(prices: List[int]) -> int:
    if len(prices) <= 1:
        return 0

    deltas = [p2 - p1 for p1, p2 in zip(prices[:-1], prices[1:])]
    (owning, cooling_down, not_owning) = (0, 0, 0)
    for d in deltas:
        (owning, cooling_down, not_owning) = (
            d + max(owning, not_owning),
            owning,
            max(not_owning, cooling_down)
        )

    return max((owning, cooling_down, not_owning))

    # how do we do this by hand?
    # find the first, largest delta between buy and sell
    # continue through the array until we reach the end
    # options at each number:
    #    buy (if we just sold)
    #    sell (if we've already bought)
    #    cooldown (after we sold)
    #    do nothing

    # [1,2,3,0,2] -> 3, buy, sell, cooldown, buy, sell
    # [3,2,4,0,1] -> 2, x, buy, sell, x, x

    # (1,2) (0,2) -> give me the (min,max) in order, with at least 1 index between each one
    # total_profit = 0
    # can_buy = True
    # can_sell = True
    # cooldown = False
    # for index, day in enumerate(prices):
    #     for next_index, next_day in prices[index + 1:]:
    #         if can_buy is True:
    #             profit = next_day - day
    #
    # tuples = []
    # for index, day in enumerate(prices):
    #     for next_index, next_day in enumerate(prices[index + 1:]):
    #         tuples.append((day, next_day))

    # buy on day 0: what's the best day to sell?
    # profits_matrix = []
    # single_day = []
    # buy_day = 0
    # for index, day in enumerate(prices):
    #     for next_index, next_day in enumerate(prices):
    #         if index >= next_index:
    #             single_day.append(None)
    #         else:
    #             single_day.append(next_day - day)
    #     profits_matrix.append(single_day)
    #     single_day = []

    # [None, 1,    2,    -1,   1]
    # [None, None, 1,    -2,   0]
    # [None, None, None, -3,  -1]
    # [None, None, None, None, 2]
    # [None, None, None, None, None]
