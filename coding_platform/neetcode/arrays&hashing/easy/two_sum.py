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

"""
Time complexity: O(n^2)
"""
def twoSum_using_list_slicing(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums) - 1):
        diff = target - nums[i]
        if diff in nums[i + 1:]:
            return [i, nums[i + 1:].index(diff) + i + 1]

"""
Here we use dict , as data retrieval in dictionary is done by O(1) as dict is hashable
That's why Time complexity: O(n)
"""
def twoSum_usingDictionary(nums: List[int], target: int) -> List[int]:
    seen_dict = {}

    for index, num in enumerate(nums):
        diff = target - num
        if diff in seen_dict:
            return [seen_dict[diff], index]
        seen_dict[num] = index


"""
Here we use set , as data retrieval in set is done by O(1) as set is hashable
That's why Time complexity: O(n)
"""
def twoSum_usingSet(nums: List[int], target: int) -> List[int]:
        seen_set = set()

        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen_set:
                return [nums.index(diff), i]
            else:
                seen_set.add(num)

"""
Note:

Drawback of Using a Set:

	The nums.index(complement) function call to retrieve the index of the complement has a time complexity of O(n), 
	which makes this solution slightly less efficient than using a dictionary for this problem. However, if you don’t 
	need to worry about index retrieval or if you’re focused on the simplicity of using a set, this approach works fine.

    If you’re looking for a more optimal solution, using a dictionary (hash map) would be the preferred approach as 
    discussed previously, as it allows direct retrieval of indices in constant time.
"""


if __name__ == '__main__':
    nums = [3, 4, 5, 6]
    target = 7
    print(twoSum_using_list_slicing(nums, target))
    print(twoSum_usingDictionary(nums, target))
    print(twoSum_usingSet(nums, target))
