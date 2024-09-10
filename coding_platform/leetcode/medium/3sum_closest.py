""""""
import math
from typing import List

"""
3Sum Closest

company: Amazon, Adobe, Facebook

Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:
Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 

Constraints:

3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-104 <= target <= 104
"""

"""this is 3 pointer approach -> time complexity -> n^3 -> not an optimised solution"""


def threeSumClosest_3_pointer(nums: List[int], target: int) -> int:
    min_diff = math.inf
    num_dict = {}
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                three_sum = nums[i] + nums[j] + nums[k]
                diff = abs(three_sum - target)
                num_dict[diff] = three_sum
                min_diff = min(diff, min_diff)

    return num_dict[min_diff]

"""This is the optimized approach
explanation:
We'll use Three-pointer approach in this question.
Sort the given list in ascending order.
A pointer lets say 'i' will be used to iterate through the given list nums.
Within that loop, two more pointers lets say 'start' and 'end' would be initialised as follows:
start=i+1
end=len(nums)-1
Now within this loop we will run another loop until the value of start in less than end.
Take a variable lets say 'sum' to store value of nums[i]+nums[start]+nums[end].
In this loop we would be checking for 3 conditions.
Condition 1:
if sum==target, the sum contains the required answer as the minimum possible difference between any two numbers is 0 and sum-target will also give 0 in this case.
Condition 2:
if difference in target and sum is less than value contained by our 'diff' variable(initialized with maximum possible value) the the diff would become equal to the absolute difference in target and sum and answer variable 'ans' would be assigned the value of 'sum', as this sum gives the minimum difference till now.
Condition 3:"
We'll check if the value of sum is greater than target then the end will be decremented by one or else the start in incremented by one in case the sum is less than target.
"""

def threeSumClosest_2_pointer(nums: List[int], target: int) -> int:
    diff = math.inf
    nums = sorted(nums)
    ans = 0
    for i in range(len(nums) - 1):
        start = i + 1
        end = len(nums) - 1
        while (start < end):
            sum = nums[i] + nums[start] + nums[end]
            if sum == target:
                return sum
            if abs(target - sum) < diff:
                diff = abs(target - sum)
                ans = sum
            if sum > target:
                end -= 1
            else:
                start += 1
    return ans


if __name__ == '__main__':
    nums = [-1, 2, 1, -4]
    target = 1
    print(threeSumClosest_3_pointer(nums, target))
    print(threeSumClosest_2_pointer(nums, target))
