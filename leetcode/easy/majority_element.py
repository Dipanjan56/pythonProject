"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.



Example 1:

Input: nums = [3,2,3]
Output: 3

Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2



Constraints:

    n == nums.length
    1 <= n <= 5 * 104
    -109 <= nums[i] <= 109


"""

from collections import Counter
from typing import List


def majority_element_1(nums: List[int]) -> int:
    occurrence_dict = {}

    for n in nums:
        if n not in occurrence_dict.keys():
            occurrence_dict[n] = 0
        occurrence_dict[n] += 1

    print(f'occurence_dict: {occurrence_dict}')

    sorted_dict = sorted(occurrence_dict.items(), key=lambda x: x[1], reverse=True)

    print(f'sorted_dict: {sorted_dict}')

    majority_element = sorted_dict[0][0]
    return majority_element


def majority_element_2(nums: List[int]) -> int:
    majority_element = 0
    occurrence_dict = {}

    for n in nums:
        if n not in occurrence_dict.keys():
            occurrence_dict[n] = 0
        occurrence_dict[n] += 1

    max_occurrence = 0
    for key, value in occurrence_dict.items():
        if value > max_occurrence:
            max_occurrence = value
            majority_element = key

    return majority_element

"""Space-complexity: O(1)"""
def majority_element_3(nums: List[int]) -> int:
    sorted_nums = sorted(nums)
    k = sorted_nums[0]
    count = 1
    for i in range(1, len(sorted_nums)):
        if k == sorted_nums[i]:
            count += 1
        else:
            print(f'num: {k} | count: {count}')
            if count > len(nums) / 2:
                return k
            k = sorted_nums[i]
            count = 1
    return k


if __name__ == '__main__':
    num_list = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(majority_element_1(num_list))
    print(majority_element_2(num_list))
    print(majority_element_3(num_list))
