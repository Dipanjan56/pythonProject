"""Valid Anagram"""
"""
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true
Example 2:

Input: s = "jar", t = "jam"

Output: false
Constraints:

s and t consist of lowercase English letters.

"""

from collections import Counter
from typing import List


def isAnagram_using_Counter(s: str, t: str) -> bool:
    s_counter = Counter(s)
    t_counter = Counter(t)

    if s_counter == t_counter:
        return True
    return False

def isAnagram_using_dictionary(s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = {}
        for letter in s:
            s_dict.setdefault(letter, 0)
            s_dict[letter] += 1

        t_dict = {}
        for letter in t:
            t_dict.setdefault(letter, 0)
            t_dict[letter] += 1

        if sorted(s_dict.items()) == sorted(t_dict.items()):
            return True
        return False


def isAnagram_simplest(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


if __name__ == '__main__':
    s = "racecar"
    t = "carrace"
    print(isAnagram_using_Counter(s, t))
    print(isAnagram_using_dictionary(s, t))
    print(isAnagram_simplest(s, t))
