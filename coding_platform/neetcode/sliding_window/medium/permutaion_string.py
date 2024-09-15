"""Permutation String"""

"""
You are given two strings s1 and s2.

Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.

Both strings only contain lowercase letters.

Example 1:

Input: s1 = "abc", s2 = "lecabee"

Output: true
Explanation: The substring "cab" is a permutation of "abc" and is present in "lecabee".

Example 2:

Input: s1 = "abc", s2 = "lecaabee"

Output: false
Constraints:

1 <= s1.length, s2.length <= 1000

"""
from typing import List
import math

"""
Time Complexity is O(n)
"""


def checkInclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False

    left = 0
    step = len(s1)

    for right in range(left + step, len(s2) + 1):
        sub_str = s2[left:right]
        # print(f'{sub_str} | {sorted(sub_str)} | {sorted(s1)}')
        if sorted(sub_str) == sorted(s1):
            return True
        left += 1

    return False


if __name__ == '__main__':
    s1 = "abc"
    s2 = "lecabee"
    print(checkInclusion(s1, s2))
