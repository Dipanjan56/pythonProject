""""""
"""Given a string s, find the length of the longest substring without repeating characters.


Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.

Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces."""
from collections import Counter
from pprint import pprint

"""
as set() is hashable so data retrival will take O(1), j=hence time complexity is : O(n) [due to the outer for loop]

"""
def lengthOfLongestSubstring(s: str) -> int:
    left = 0
    max_len = 0
    char_set = set()

    for right in range(len(s)):
        # If there's a duplicate character, shrink the window from the left
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        # Add the current character to the set
        char_set.add(s[right])
        # Update the maximum length of the substring
        max_len = max(max_len, right - left + 1)

    return max_len


if __name__ == '__main__':
    s1 = 'abcabcbb'
    print(lengthOfLongestSubstring(s1))
