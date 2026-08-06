# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

prices = [7,1,5,3,6,4]
prices = [2,4,1]


def max_profit(prices: list[int]) -> int:
    min_price = prices[0]
    profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > profit:
            profit = price - min_price

    return profit


print(max_profit(prices))