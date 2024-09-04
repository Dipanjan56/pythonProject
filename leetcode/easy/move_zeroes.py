""""""
from typing import List

"""

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104


"""

"use buubble sort technique -> time-complexity O(n^2)"


def move_zeroes_1(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    swapped = False
    length = len(nums)
    for i in range(length - 1):
        for j in range(0, length - i - 1):
            if nums[j] == 0:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if not swapped:
            break


"below is the most optimized technique - time-complexity - O(n)"


def move_zeroes_2(nums: List[int]) -> None:
    for n in nums:
        if n == 0:
            nums.remove(n)
            nums.append(0)


if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    print(move_zeroes_1(nums))
    print(move_zeroes_2(nums))
