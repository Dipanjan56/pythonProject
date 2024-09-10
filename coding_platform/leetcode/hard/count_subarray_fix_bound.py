"""COUNT SUBARRAY WITH FIXED BOUND"""
from typing import List

"""
You are given an integer array nums and two integers minK and maxK.

A fixed-bound subarray of nums is a subarray that satisfies the following conditions:

The minimum value in the subarray is equal to minK.
The maximum value in the subarray is equal to maxK.
Return the number of fixed-bound subarrays.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
Output: 2
Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].
Example 2:

Input: nums = [1,1,1,1], minK = 1, maxK = 1
Output: 10
Explanation: Every subarray of nums is a fixed-bound subarray. There are 10 possible subarrays.
 

Constraints:

2 <= nums.length <= 105
1 <= nums[i], minK, maxK <= 106
"""


def countSubarrays(nums: List[int], minK: int, maxK: int) -> int:
    fix_bound_subarray_list = [nums[i:j] for i in range(len(nums)) for j in range(i + 1, len(nums) + 1) if
                               min(nums[i:j]) == minK and max(nums[i:j]) == maxK]
    print(fix_bound_subarray_list)
    return len(fix_bound_subarray_list)


if __name__ == '__main__':
    nums = [1, 3, 5, 2, 7, 5]
    minK = 1
    maxK = 5
    print(countSubarrays(nums, minK, maxK))
