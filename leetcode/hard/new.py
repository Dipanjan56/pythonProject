"""Minimum Window Substring"""

"""
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
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
    if s == t:
        return s
    if len(s) < len(t):
        return ""
    s_dict = {}
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
                    s_dict[s[i:j]] = len(s[i:j])

    for key, value in s_dict.items():
        if value == min(s_dict.values()):
            return key
    return ""


if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"
    print(minWindow(s, t))