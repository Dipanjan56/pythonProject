"""Rotate Array"""
from typing import List

"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]


Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
 

Follow up:

Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""


def rotate(nums: List[int], k: int) -> None:
    """
        Do not return anything, modify nums in-place instead.
        steps:
        1. reverse the array first
        2. then again reverse the two halves of the array based on k
        3. add them toa new array
        4. shallow copy the new array to the input array using [:]

        example: [1,2,3,4,5,6,7]
        1. [7,5,6,4,3,2,1]
        2. [5,6,7] and [1,2,3,4]
        3. a = 5,6,7] + [1,2,3,4]
        4. input_arr[:] = a
        """

    k %= len(nums) # this is because if k is greater than length of the array then actual k should be: k = k - len(arr)
    print(k)
    a = nums[::-1][0:k][::-1] + nums[::-1][k:][::-1]
    nums[:] = a # this is shallow copy
    print(nums)




if __name__ == '__main__':
    nums = [1, 2, 3]
    rotate(nums, 4)
