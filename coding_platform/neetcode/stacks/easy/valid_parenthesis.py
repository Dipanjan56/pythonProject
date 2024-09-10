"""valid Parenthesis"""
from typing import List

"""
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.

Example 1:

Input: s = "[]"

Output: true
Example 2:

Input: s = "([{}])"

Output: true
Example 3:

Input: s = "[(])"

Output: false
Explanation: The brackets are not closed in the correct order.

Constraints:

1 <= s.length <= 1000
67141512131681720543212122910111819
                    top_element = stack.pop()
                if bracket_map[char] != top_element:
                    return False
            else:
                stack.append(char) 

        if len(stack) == 0:
            return True
        return False               

"""


def isValid(s: str) -> bool:
    bracket_map = {']': '[', '}': '{', ')': '('}
    stack = []

    for char in s:
        if char in bracket_map:
            if not stack:
                top_element = '#'
            else:
                top_element = stack.pop()
            if bracket_map[char] != top_element:
                return False
        else:
            stack.append(char)

    if len(stack) == 0:
        return True
    return False

def maxProfit(prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]

        left = 0
        for right in range(left + 1, len(prices) - 1):
            if prices[left] > prices[right]:
                left += 1
            else:
                min_price = min(prices[left], min_price)
                profit = prices[right] - min_price
                max_profit = max(profit, max_profit)
        return max_profit

if __name__ == '__main__':
    # s = "([{}])"
    # print(isValid(s))
    prices = [5, 1, 5, 6, 7, 1, 10]
    print(maxProfit(prices))