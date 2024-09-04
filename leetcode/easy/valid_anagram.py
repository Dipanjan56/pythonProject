""""""
from typing import List

"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

"""


def is_anagram_1(s: str, t: str) -> bool:
    if len(s) == len(t):
        t_list = list(t)
        for char in s:
            if char in t_list:
                t_list.remove(char)
        if len(t_list) == 0:
            return True
    return False


def is_anagram_2(s: str, t: str) -> bool:
    sorted_s = sorted(s)
    sorted_t = sorted(t)
    return sorted_s == sorted_t


if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    print(is_anagram_1(s, t))
    print(is_anagram_2(s, t))
