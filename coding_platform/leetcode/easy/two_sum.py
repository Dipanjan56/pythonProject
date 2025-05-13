""""""
from typing import List, Any

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


def two_sum_1(nums: List[int], target: int) -> list[int] | None:
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
            return None
        return None
    return None


def two_sum_2(nums: List[int], target: int) -> list[int] | None:
    for i in range(len(nums) - 1):
        diff = target - nums[i]
        if diff in nums[i + 1:]:
            diff_index = nums[i + 1:].index(diff) + i + 1
            return [i, diff_index]
        return None
    return None


"""
two_sum_3() is the most optimized approach. 
Time complexity: O(n)
explanatory video: https://www.youtube.com/watch?v=luicuNOBTAI
"""


def two_sum_3(nums: List[int], target: int) -> list[int | Any] | None:
    seen = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in seen.keys():
            return [seen[diff], i]
        seen[nums[i]] = i
        return None
    return None


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum_1(nums, target))
    print(two_sum_3(nums, target))
