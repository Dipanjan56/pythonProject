"""Palindrome Number"""
from test import isPalindrome

"""
Given an integer x, return true if x is a 
palindrome
, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
"""


def is_palindrome(x: int) -> bool:
    if x < 0:
        return False
    if x < 10:
        return True

    num = x
    rev_x = 0
    while (num > 0):
        dividend = num % 10
        num = num // 10
        rev_x = rev_x * 10 + dividend

    if rev_x == x:
        return True
    return False

if __name__ == '__main__':
    n = 121
    print(isPalindrome(n))