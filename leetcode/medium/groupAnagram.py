"""Group Anagram"""
from typing import List

"""
Given an array of strings strs, group the 
anagrams
 together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:

Input: strs = [""]
Output: [[""]]

Example 3:

Input: strs = ["a"]
Output: [["a"]]

 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    sorted_strs = []
    for word in strs:
        sorted_strs.append(''.join(sorted(word)))

    word_dict = {}

    for sorted_word, word in zip(sorted_strs, strs):
        word_dict.setdefault(sorted_word, {})
        word_list = list(word_dict[sorted_word])
        word_list.append(word)
        word_dict[sorted_word] = word_list

    return list(word_dict.values())

if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(groupAnagrams(strs))
