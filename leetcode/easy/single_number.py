""""""
from typing import List

"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]
Output: 1

Example 2:

Input: nums = [4,1,2,1,2]
Output: 4

Example 3:

Input: nums = [1]
Output: 1

 

Constraints:

    1 <= nums.length <= 3 * 104
    -3 * 104 <= nums[i] <= 3 * 104
    Each element in the array appears twice except for one element which appears only once.



"""

"""
Solution 1:

You can solve this problem using the XOR (^) bitwise operation. 
The XOR operation between two equal numbers results in 0, and XORing any number with 0 results in the number itself. 
Therefore, if you XOR all elements in the array, the duplicates will cancel each other out, 
and you'll be left with the element that appears only once.

Here's a Python function that implements this approach with linear runtime complexity and constant extra space:
"""


def single_number_1(nums: List[int]) -> int:
    result = 0
    for num in nums:
        result ^= num
    return result


"""
Solution2:

Algorithm =>

    Iterate over all the elements in nums\text{nums}nums
    If some number in nums\text{nums}nums is new to array, append it
    If some number is already in the array, remove it


"""


def single_number_2(nums: List[int]) -> int:
    no_duplicate_list = []

    for num in nums:
        if num in no_duplicate_list:
            no_duplicate_list.remove(num)
        else:
            no_duplicate_list.append(num)

    return no_duplicate_list[0]


if __name__ == '__main__':
    nums = [4, 1, 2, 1, 2]
    print(single_number_1(nums))
    print(single_number_2(nums))
