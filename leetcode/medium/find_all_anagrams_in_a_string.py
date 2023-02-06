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

"""This is my solution, not the optimized one"""


def findAnagrams(s: str, p: str):
    if len(s) < len(p):
        return []
    anagram_length = len(p)
    possible_anagram_list = []
    for i in range(0, len(s)):
        j = i + anagram_length
        if len(s[i:j]) == anagram_length:
            possible_anagram_list.append(s[i:j])
    print(possible_anagram_list)

    index_list = []
    for index in range(0, len(possible_anagram_list)):
        substring = sorted(possible_anagram_list[index])
        sorted_anagram = sorted(p)
        if substring == sorted_anagram:
            index_list.append(index)

    print(index_list)


if __name__ == '__main__':
    s = "baa"
    p = "aa"
    findAnagrams(s, p)
