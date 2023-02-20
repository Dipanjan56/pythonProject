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


def longestPalindrome(s: str) -> list:
    palindrome_dict = {}
    for i in range(0, len(s)):
        for j in range(i + 1, len(s) + 1):
            sub_string = s[i:j]
            if check_palindrome(sub_string):
                if len(sub_string) in palindrome_dict.keys():
                    l = list(palindrome_dict[len(sub_string)])
                    l.append(sub_string)
                    palindrome_dict[len(sub_string)] = l
                else:
                    palindrome_dict[len(sub_string)] = {sub_string}

    print(palindrome_dict)
    max_length = max(list(palindrome_dict.keys()))
    longest_palindrome = palindrome_dict[max_length]
    return longest_palindrome


def check_palindrome(s):
    if s == s[::-1]:
        return True
    return False


if __name__ == '__main__':
    s = 'babad'
    print('longest substring list: ', longestPalindrome(s))
