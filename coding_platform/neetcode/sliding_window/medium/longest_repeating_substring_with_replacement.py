"""Longest Repeating Substring With Replacement"""
from collections import defaultdict

"""
You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.

After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

Example 1:

Input: s = "XYYX", k = 2

Output: 4
Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.

Example 2:

Input: s = "AAABABB", k = 1

Output: 5

Example 2:

Input: s = "ABBB", k = 2

Output: 4

Constraints:

1 <= s.length <= 1000
0 <= k <= s.length
"""


def characterReplacement(s: str, k: int) -> int:
    left = 0
    max_char_count = 0  # Keeps track of the most frequent character in the window
    char_count = defaultdict(int) # Dictionary to store the frequency of characters in the window
    max_length = 0

    # Iterate over the string using the sliding window
    for right in range(len(s)):
        # Add the current character to the frequency count
        char_count[s[right]] += 1

        # Update the count of the most frequent character in the current window
        max_char_count = max(max_char_count, char_count[s[right]])

        # If the current window length minus the most frequent character count is greater than k,
        # we need to shrink the window (i.e., more than k characters need to be replaced)
        if (right - left + 1) - max_char_count > k:
            # Shrink the window by moving the left pointer forward
            char_count[s[left]] -= 1
            left += 1

        # Calculate the maximum length of the valid window
        max_length = max(max_length, right - left + 1)

    return max_length


if __name__ == '__main__':
    s = "AAABABB"
    k = 1
    print(characterReplacement(s, k))