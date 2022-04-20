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


def get_max_profit(stock_prices):
    min_price = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]
    for current_time in range(1, len(stock_prices)):
        current_price = stock_prices[current_time]
        potential_profit = current_price - min_price
        max_profit = max(max_profit, potential_profit)
        min_price = min(min_price, current_price)

    return max_profit
