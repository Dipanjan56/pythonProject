""""""
"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

 

Constraints:

    1 <= s.length <= 2 * 105
    s consists only of printable ASCII characters.



"""

from collections import Counter
from typing import List
import re


def isPalindrome_two_pointers(s: str) -> bool:
    # Filter out non-alphanumeric characters and convert to lowercase
    filtered_chars = [char.lower() for char in s if char.isalnum()]
    print(filtered_chars)

    # Use two pointers to check for palindrome
    left, right = 0, len(filtered_chars) - 1
    while left < right:
        if filtered_chars[left] != filtered_chars[right]:
            return False
        left += 1
        right -= 1

    return True


if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    print(isPalindrome_two_pointers(s))
