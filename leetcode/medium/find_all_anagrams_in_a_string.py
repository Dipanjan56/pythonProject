from collections import Counter
import itertools

"""Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

Example 3:

Input: s = "baa", p = "aa"
Output: [1]


Constraints:

1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters."""

"""This is the optimized one"""
"""Solution: use sliding window approach and make use of Counter ds from collections library
What is Counter?
Counter is an unordered collection where elements are stored as Dict keys and their count as dict value. 
Counter elements count can be positive, zero or negative integers. However there is no restriction on it’s keys 
and values. Although values are intended to be numbers but we can store other objects too.
"""


def findAnagrams(s: str, p: str):
    if len(s) < len(p):
        return []
    anagram_length = len(p)
    anagram_counter = Counter(p)
    print(anagram_counter)
    index_list = []
    for i in range(0, len(s)):
        j = i + anagram_length
        if len(s[i:j]) == anagram_length:
            s_counter = Counter(s[i:j])
            if anagram_counter == s_counter:
                index_list.append(i)

    print(index_list)


def find_all_possible_anagram(s: str):
    perms = [''.join(perm) for perm in itertools.permutations(s)]
    print(perms)


if __name__ == '__main__':
    s = "cbaebabacd"
    p = "abc"
    findAnagrams(s, p)
    find_all_possible_anagram('1234')
