"""Contains Dupliacte II"""
from itertools import combinations
from typing import List

"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
"""


def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    num_dict = {}

    for i in range(len(nums)):
        num_dict.setdefault(nums[i], {})
        index_list = list(num_dict[nums[i]])
        index_list.append(i)
        num_dict[nums[i]] = index_list

    for value in num_dict.values():
        if len(value) > 1:
            for a, b in combinations(value, 2):
                diff = abs(a - b)
                if diff <= k:
                    return True

    return False


if __name__ == '__main__':
    nums = [1, 0, 1, 1]
    k = 1
    print(containsNearbyDuplicate(nums, k))