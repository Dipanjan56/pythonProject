""""""
from typing import List

"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""

"""optimized solution with n^2 time-complexity"""


def three_sum_1(nums: List[int]) -> List[List[int]]:
    triplet_list = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) - 1):
            two_sum = nums[i] + nums[j]
            third_num = - two_sum
            if third_num in nums[j + 1:]:
                triplet = sorted([nums[i], nums[j], third_num])
                if triplet not in triplet_list:
                    triplet_list.append(triplet)
    return triplet_list


"""Most optimized Solution: Time Complexity: O(n^2)"""


def three_sum_2(nums: List[int]) -> List[List[int]]:
    result_set = set()
    seen = {}
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            diff = 0 - (nums[i] + nums[j])
            if diff in seen and seen[diff] == i:
                triplet = tuple(sorted([nums[i], nums[j], diff]))
                result_set.add(triplet)
            else:
                seen[nums[j]] = i
    return result_set


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    print(three_sum_1(nums))
    print(three_sum_2(nums))
