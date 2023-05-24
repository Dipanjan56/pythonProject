""""""

"""
2. Given two strings. The task is to find the length of the longest common substring.

Example 1:

Input: S1 = "ABCDGH", S2 = "ACDGHR"
Output: 4
Explanation: The longest common substring
is "CDGH" which has length 4.

"""

import functools
from typing import List


def get_longest_common_substring(s1: str, s2: str):
    c1 = {s1[i:j] for i in range(len(s1)) for j in range(i + 1, len(s1) + 1)}
    c2 = {s2[i:j] for i in range(len(s2)) for j in range(i + 1, len(s2) + 1)}

    common_sub_string = c1.intersection(c2)

    longest_substring = functools.reduce(lambda a, b: a if len(a) > len(b) else b, common_sub_string)
    print(longest_substring)
    return len(longest_substring)

if __name__ == '__main__':
    s1 = "ABCDGH"
    s2 = "ACDGHR"
    print(get_longest_common_substring(s1, s2))
