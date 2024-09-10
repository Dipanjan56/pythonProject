"""Two Sum"""
"""
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true
Example 2:

Input: s = "jar", t = "jam"

Output: false
Constraints:

s and t consist of lowercase English letters.

"""

from collections import Counter
from typing import List


def twoSum_using_list_slicing(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums) - 1):
        diff = target - nums[i]
        if diff in nums[i + 1:]:
            return [i, nums[i + 1:].index(diff) + i + 1]


def twoSum_using_dictionary(nums: List[int], target: int) -> List[int]:
    seen = {}

    for index, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], index]
        seen[num] = index


if __name__ == '__main__':
    nums = [3, 4, 5, 6]
    target = 7
    print(twoSum_using_list_slicing(nums, target))
    print(twoSum_using_dictionary(nums, target))
