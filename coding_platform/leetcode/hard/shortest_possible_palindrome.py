""""""

"""
Given a string, find the shortest possible string which can be achieved by adding characters to the end of initial string to make it a palindrome.

Example:
For st = "abcdc", the output should be
solution(st) = "abcdcba".

Input/Output

[execution time limit] 4 seconds (py3)

[input] string st

A string consisting of lowercase English letters.

Guaranteed constraints:
3 ≤ st.length ≤ 10.

[output] string
"""


def shortest_possible_palindrome(st: str) -> str:
    reversed_st = st[::-1]

    # Find the longest common substring of the original string and its reversed version.
    longest_common_substring = ''
    for i in range(len(st)):
        for j in range(len(reversed_st)):
            if st[i] == reversed_st[j]:
                longest_common_substring = st[i:j + 1]
                break

    # Add the characters after the longest common substring to the end of the original string to make it a palindrome.
    palindrome = st + longest_common_substring[::-1]

    return palindrome


if __name__ == '__main__':
    s = 'abcdc'
    print(shortest_possible_palindrome(s))
