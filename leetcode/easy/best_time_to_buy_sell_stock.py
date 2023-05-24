


"""Best Time To Buy Sell Problem"""

"""You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Example 3:
Input: prices = [2,4,1]
Output: 2


Constraints:
1 <= prices.length <= 105
0 <= prices[i] <= 104
"""
from typing import List
import math

"""using two pointers approach
Time Complexity is O(n^2)
"""


def maxProfit(prices: List[int]) -> int:
    max_profit = 0
    for i in range(len(prices) - 1):
        current_profit = 0
        for j in range(i + 1, len(prices)):
            current_profit = prices[j] - prices[i]
            if current_profit < 0:
                break
            if current_profit > max_profit:
                max_profit = current_profit

    return max_profit


"""using single pointer
Time complexity is O(n)
"""


def max_profit_optimized(prices: List[int]) -> int:
    min_price = math.inf
    max_profit = 0
    for i in range(len(prices)):
        current_profit = 0
        if prices[i] < min_price:
            min_price = prices[i]
        else:
            current_profit = prices[i] - min_price
        if current_profit > max_profit:
            max_profit = current_profit

    return max_profit


if __name__ == '__main__':
    prices_1 = [7, 1, 5, 3, 6, 4]
    prices_2 = [2, 4, 1]
    prices_3 = [7, 2, 5, 8, 4, 1, 3, 6]
    print(maxProfit(prices_3))
    print(max_profit_optimized(prices_3))
