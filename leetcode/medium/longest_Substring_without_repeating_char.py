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

"""This is my solution, not the optimized one"""


def lengthOfLongestSubstring(s: str) -> int:
    if len(s) == 0:
        return 0
    elif len(s) == 1:
        return 1
    """first extract all the substring using set comprehension removing duplicates"""
    substring_set = sorted({s[i:j] for i in range(0, len(s)) for j in range(i + 1, len(s) + 1)})

    """extract the set of unique individual characters"""
    individual_char_set = {char for char in s}

    """create an empty dict"""
    substring_without_repeat_dict = {}

    """ and first taking one substring at a time from substring_set and adding that in the dict in this way:
    key = substring and value = length of the substring
    """
    for substring in substring_set:
        break_flag = False
        substring_without_repeat_dict[substring] = len(substring)
        """taking one unique char from individual_char_set and see if that char present or not in the substring
        if present, then we are taking presence count of that character in that substring, and if the count is 
        greater than 1 then that that means there are repeating char in that substring, 
        hence we are then popping the substring from the dict
        """
        for c1 in individual_char_set:
            if c1 in substring:
                count = 0
                for c2 in substring:
                    if c1 == c2:
                        count += 1
                if count > 1:
                    substring_without_repeat_dict.pop(substring)
                    break_flag = True
                    break
            if break_flag:
                break

    """now we get the dictionary of substrings without repeating characters
    To get the longest substring length, we need to sort the values of dictionary 
    and then retrieve the last value as it will be the longest value 
    """
    longest_value = sorted(list(substring_without_repeat_dict.values()))[-1]
    return longest_value


def lengthOfLongestSubstring_2(s: str) -> int:
    if len(s) == 0:
        return 0
    elif len(s) == 1:
        return 1
    substring_counter_list = [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]

    result = []
    for substring in substring_counter_list:
        flag = False
        substring_counter = Counter(substring)
        for value in substring_counter.values():
            if value > 1:
                flag = True
                break
        if not flag:
            result.append(len(substring))
    return max(result)


def lengthOfLongestSubstring_3(s: str) -> int:
    if len(s) == 0:
        return 0
    elif len(s) == 1:
        return 1
    result = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring_counter = Counter(s[i:j])
            flag = False
            for value in substring_counter.values():
                if value > 1:
                    flag = True
                    break
            if not flag:
                result.append(len(s[i:j]))

    return max(result)


"""most optimized approach with Time Complexity of O(n)"""


def lengthOfLongestSubstring_4(s: str):
    char_set = set()  # To store unique characters in the current substring
    max_length = 0  # Length of the longest substring
    i, j = 0, 0  # Pointers for the sliding window

    while i < len(s) and j < len(s):
        if s[j] not in char_set:
            char_set.add(s[j])
            j += 1
            max_length = max(max_length, j - i)  # Update the maximum length
        else:
            char_set.remove(s[i])
            i += 1

    return max_length


def lengthOfLongestSubstring_5(s: str) -> int:
    if len(s) == 1:
        return 1
    max_length = 0
    for i in range(len(s) - 1):
        subStr = s[i]
        max_length = max(len(subStr), max_length)
        for j in range(i + 1, len(s)):
            if s[j] not in subStr:
                subStr += s[j]
                print(subStr)
                max_length = max(len(subStr), max_length)
            else:
                break
    return max_length


if __name__ == '__main__':
    s1 = 'abcabcbb'
    print(lengthOfLongestSubstring(s1))
    print(lengthOfLongestSubstring_2(s1))
    print(lengthOfLongestSubstring_3(s1))
    print(lengthOfLongestSubstring_4(s1))
    print(lengthOfLongestSubstring_5(s1))
