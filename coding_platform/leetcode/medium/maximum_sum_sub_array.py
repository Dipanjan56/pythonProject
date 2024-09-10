"""question"""
"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.



Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104

"""
import math
from typing import List

"""this is my solution using two pointers approach, not an optimized one"""


def maxSubArray(nums: List[int]) -> int:
    sum_list = []

    sub_array = [nums[i:j] for i in range(len(nums)) for j in range(i + 1, len(nums) + 1)]

    for num_array in sub_array:
        sum = 0
        for num in num_array:
            sum += num
        sum_list.append(sum)

    return sorted(sum_list)[-1]


"""optimized solution: using optimized bruteforce and two pointers approach starting from 0 index
Time complexity -> O(n^2)
still all the test cases will not be  passed in leetcode due to time
"""


def maxSubArray_2(nums: List[int]) -> int:
    max_sum = -math.inf
    for i in range(len(nums)):
        current_sum = 0
        for j in range(i, len(nums)):
            current_sum += nums[j]
            max_sum = max(current_sum, max_sum)

    return max_sum


"""Most optimized solution - Kanade's algo : Time Complexity: O(n)

see approach 2 -> https://leetcode.com/problems/maximum-subarray/editorial/?envType=featured-list&envId=top-interview-questions?envType=featured-list&envId=top-interview-questions
"""


def maxSubArray_3(nums: List[int]) -> int:
    # Initialize our variables using the first element.
    current_sum = max_sum = nums[0]

    # Start with the 2nd element since we already used the first one.
    for num in nums[1:]:
        # If current_subarray is negative, throw it away. Otherwise, keep adding to it.
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(maxSubArray(nums))
    print(maxSubArray_2(nums))
    print(maxSubArray_3(nums))
