"""Two Sum"""
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

 

Constraints:

    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.
    
"""

from collections import Counter
from typing import List, Any

"""
Time complexity: O(n^2)
"""
def twoSum_using_list_slicing(nums: List[int], target: int) -> list[int] | None:
    for i in range(len(nums) - 1):
        diff = target - nums[i]
        if diff in nums[i + 1:]:
            return [i, nums[i + 1:].index(diff) + i + 1]
        return None
    return None


"""
Here we use dict , as data retrieval in dictionary is done by O(1) as dict is hashable
That's why Time complexity: O(n)
"""
def twoSum_usingDictionary(nums: List[int], target: int) -> list[int | Any] | None:
    seen_dict = {}

    for index, num in enumerate(nums):
        diff = target - num
        if diff in seen_dict:
            return [seen_dict[diff], index]
        seen_dict[num] = index
        return None
    return None


"""
Here we use set , as data retrieval in set is done by O(1) as set is hashable
That's why Time complexity: O(n)
"""
def twoSum_usingSet(nums: List[int], target: int) -> list[int] | None:
        seen_set = set()

        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen_set:
                return [nums.index(diff), i]
            else:
                seen_set.add(num)
                return None
        return None


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
