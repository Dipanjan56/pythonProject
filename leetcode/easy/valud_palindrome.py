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


def is_palindrome(s: str) -> bool:
    char_list = []
    for char in s.lower().strip():
        ascii_value = ord(char)
        if (97 <= ascii_value <= 122) or (48 <= ascii_value <= 57):
            char_list.append(char)

    s = ''.join(char_list)

    print(s)

    if s == s[::-1]:
        return True

    return False

""" The re.sub() function identifies all these non-alphanumeric characters with the pattern r'[^a-zA-Z0-9]' 
and replaces them with an empty string '' """
def is_palindrome_most_optimized(s: str) -> bool:
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    if s == s[::-1]:
        return True
    return False


if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    print(is_palindrome(s))
    print(is_palindrome_most_optimized(s))
