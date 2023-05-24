"""Minimum Window Substring"""
import functools

"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring
of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

Example 4:
Input: s = "bbaa", t = "aba"
Output: "baa"
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
"""

"""not the optimized one"""


def minWindow(s: str, t: str) -> str:
    if len(s) == 1 and len(t) == 1:
        if s == t:
            return s
        else:
            return ""
    if len(s) < len(t):
        return ""
    s_list = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring_l = list(s[i:j])
            flag = True
            if len(t) <= len(substring_l):
                for char in t:
                    if char not in substring_l:
                        flag = False
                        break
                    else:
                        substring_l.remove(char)
                if flag:
                    s_list.append(s[i:j])
    if len(s_list) > 0:
        return functools.reduce(lambda a, b: a if len(a) < len(b) else b, s_list)

    return ""


if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"
    print(minWindow(s, t))
