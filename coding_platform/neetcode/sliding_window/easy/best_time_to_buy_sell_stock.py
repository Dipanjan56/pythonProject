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

"""
Time Complexity is O(n)
"""
def maxProfit(prices: List[int]) -> int:
    max_profit = 0
    min_price = prices[0]

    for price in prices:
        min_price = min(price, min_price)
        current_profit = price - min_price
        max_profit = max(current_profit, max_profit)
    return max_profit


if __name__ == '__main__':
    prices_1 = [7, 1, 5, 3, 6, 4]
    prices_2 = [2, 4, 1]
    prices_3 = [7, 2, 5, 8, 4, 1, 3, 6]
    print(maxProfit(prices_3))
