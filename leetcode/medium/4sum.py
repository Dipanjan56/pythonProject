""""""
from typing import List

"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:=
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
"""

"""time """
def solution_3_pointer(nums: List[int], target: int) -> List[List[int]]:
    sum_list = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                three_sum = nums[i] + nums[j] + nums[k]
                diff = target - three_sum
                if diff in nums[k + 1:]:
                    nums_list = sorted([nums[i], nums[j], nums[k], diff])
                    if nums_list not in sum_list:
                        sum_list.append(nums_list)
    return sum_list


if __name__ == '__main__':
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    print(solution_3_pointer(nums, target))
