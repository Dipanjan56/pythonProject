""""""
"""
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true


Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109

"""

from collections import Counter
from typing import List


def contains_duplicate_using_set(nums: List[int]) -> bool:
    num_set = set()
    for n in nums:
        if n in num_set:
            print(f'duplicate value: {n}')
            return True
        else:
            num_set.add(n)
    return False


def contains_duplicate_using_dictionary(nums: List[int]) -> bool:
    occurrence_dict = {}
    for i in range(len(nums)):
        occurrence_dict.setdefault(nums[i], 0)
        occurrence_dict[nums[i]] += 1

    for key, value in occurrence_dict.items():
        if value > 1:
            print(f'duplicate value: {key}')
            return True
    return False


def contains_duplicate_using_counter(nums: List[int]) -> bool:
    num_counter = Counter(nums)
    print(num_counter)

    for key, value in num_counter.items():
        if value > 1:
            print(f'duplicate value: {key}')
            return True
    return False


def contains_duplicate_using_two_for_loop(nums: List[int]) -> bool:
    for i in range(0, len(nums) - 1):
        count = 0
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                count += 1
                print(f'duplicate value: {nums[i]}')
                return True
    return False


def contains_duplicate_using_one_for_loop(nums: List[int]) -> bool:
    for i in range(len(nums)):
        if nums[i] in nums[i + 1:]:
            print(f'duplicate value: {nums[i]}')
            return True
    return False


"First three solution using set, dict and counter are the optimized one, among them using set is the most optimized"

if __name__ == '__main__':
    num_list = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(contains_duplicate_using_set(num_list))
    print(contains_duplicate_using_dictionary(num_list))
    print(contains_duplicate_using_counter(num_list))
    print(contains_duplicate_using_two_for_loop(num_list))
    print(contains_duplicate_using_one_for_loop(num_list))
