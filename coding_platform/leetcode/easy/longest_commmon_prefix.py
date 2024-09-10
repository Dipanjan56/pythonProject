""""""
from typing import List

"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""


def longestCommonPrefix(strs: List[str]) -> str:
    if len(strs) == 0:
        return ""
    elif len(strs) == 1:
        return strs[0]
    longestCommonPrefix_list = []
    sorted_list = sorted(strs, key=len)
    min_word = sorted_list[0]
    for i in range(len(min_word)):
        presence = False
        for j in range(1, len(sorted_list)):
            if sorted_list[j][i] == min_word[i]:
                presence = True
            else:
                presence = False
                break
        if presence:
            longestCommonPrefix_list.append(min_word[i])
        else:
            break

    return ''.join(longestCommonPrefix_list)

def longest_common_prefix_optimized(strs: list) -> str:
    if not strs:
        return ""

    # Start with the first word as the prefix
    prefix = strs[0]

    for s in strs[1:]:
        # Keep trimming the prefix until it's a prefix of s
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            # If the prefix becomes empty, return empty string
            if not prefix:
                return ""

    return prefix




if __name__ == '__main__':
    strs = ["abab","aba","abc"]
    print(longestCommonPrefix(strs))
    print(longest_common_prefix_optimized(strs))
