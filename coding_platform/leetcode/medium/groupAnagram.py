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

"""
Optimized Solution:

	1.	Sort each word: For each word in the list, sort its characters. Anagrams will result in the same sorted string.
	2.	Use a dictionary: Use a dictionary where the key is the sorted word and the value is a list of all words that, when sorted, result in the same key.
	3.	Group anagrams: Append each word to its respective list in the dictionary.
	4.	Return the values of the dictionary: The result will be the grouped anagrams.
"""
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    word_dict = {}

    for word in strs:
        sorted_word = ''.join(sorted(word))
        word_dict.setdefault(sorted_word, [])
        word_dict[sorted_word].append(word)

    return word_dict.values()


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(groupAnagrams(strs))
