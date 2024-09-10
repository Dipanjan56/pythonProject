""""""
from typing import List

"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2

Example 2:

Input: nums = [3,1,3,4,2]
Output: 3

 

Constraints:

    1 <= n <= 105
    nums.length == n + 1
    1 <= nums[i] <= n
    All the integers in nums appear only once except for precisely one integer which appears two or more times.

"""

"""time-complexity: O(n^2)
because although we are using one for loop, but here --- if nums[i] in nums[i + 1:]:]
also used second loop internally, which is why all test cases will not pass
"""


def find_duplicate_1(nums: List[int]) -> int:
    for i in range(len(nums)):
        if nums[i] in nums[i + 1:]:
            return nums[i]


"""Most optimized approach : Time complexity: O(n)
here using --- if element in visited: it will give the direct value using hashing in dictionary
but if instead if we did --- if element in visited.keys() it would fail as .keys will give an entire key list
and hence python will search in that list in brute force

"""


def find_duplicate_2(nums: List[int]) -> int:
    visited = {}
    for index, element in enumerate(nums):
        if element in visited:
            return element
        visited[element] = index


if __name__ == '__main__':
    nums = [1, 3, 4, 2, 2]
    print(find_duplicate_1(nums))
    print(find_duplicate_2(nums))
