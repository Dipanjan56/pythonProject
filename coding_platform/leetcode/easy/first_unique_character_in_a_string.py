"""First Unique Character in a String"""

"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"
Output: 0

Example 2:

Input: s = "loveleetcode"
Output: 2

Example 3:

Input: s = "aabb"
Output: -1

 

Constraints:

    1 <= s.length <= 105
    s consists of only lowercase English letters.

"""


def first_unique_character(s: str) -> str:
    count_dict = {}
    for char in s:
        count_dict.setdefault(char, 0)
        count_dict[char] += 1

    """as order of dictionary is not maintained thats why we are iterating over the string again to get the key value in orederly format"""
    for char in s:
        if count_dict[char] == 1:
            return s.find(char)
    return -1


if __name__ == '__main__':
    s = 'hello, hyderabad'
    print('first unique character index: ', first_unique_character(s))
