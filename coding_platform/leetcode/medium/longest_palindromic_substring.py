"""
Given a string s, return the longest
palindromic

substring
 in s.



Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb

Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.
"""
from functools import reduce
from typing import List

"""My approach with Time Complexity: O(n2)"""


def longest_palindrome_1(s: str) -> str:
    max_length = 0
    longest_palindromic_string = ''
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            s1 = s[i:j]
            if s1 == s1[::-1]:
                if len(s1) > max_length:
                    max_length = len(s1)
                    longest_palindromic_string = s1

    return longest_palindromic_string


def check_palindrome(s):
    if s == s[::-1]:
        return True
    return False


def longest_palindrome_2(s: str):
    palindrome_dict = {}
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            sub_string = s[i:j]
            if check_palindrome(sub_string):
                palindrome_dict[sub_string] = len(sub_string)
    print(palindrome_dict)
    max_length = max(palindrome_dict.values())
    longest_palindrome_list = []
    for key, value in palindrome_dict.items():
        if value == max_length:
            longest_palindrome_list.append(key)
    return longest_palindrome_list


def longest_palindrome_3(s: str) -> List[str]:
    palindrome_substring_list = [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1) if
                                 check_palindrome(s[i:j])]
    print(palindrome_substring_list)
    palindrome_dict = {}
    for sub_string in palindrome_substring_list:
        palindrome_dict[sub_string] = len(sub_string)
    print(palindrome_dict)
    max_length = max(palindrome_dict.values())
    longest_palindrome_list = []
    for key, value in palindrome_dict.items():
        if value == max_length:
            longest_palindrome_list.append(key)
    return longest_palindrome_list


"""optimised approach with Time Complexity: O(n2)"""


def longest_palindrome_4(s):
    if not s:
        return ""

    start = 0
    end = 0

    for i in range(len(s)):
        len1 = expand_around_center(s, i, i)  # Check for odd-length palindromes
        len2 = expand_around_center(s, i, i + 1)  # Check for even-length palindromes
        length = max(len1, len2)

        if length > end - start:
            start = i - (length - 1) // 2
            end = i + length // 2

    return s[start:end + 1]


def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1

    return right - left - 1


if __name__ == '__main__':
    s = 'babad'
    print('longest substring list: ', longest_palindrome_1(s))
    # print('longest substring list: ', longest_palindrome_2(s))
    # print('longest substring list: ', longest_palindrome_3(s))
    # print('longest substring list: ', longest_palindrome_4(s))

