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


class Solution:
    def containsDuplicate(nums: List[int]) -> bool:
        n_counter = Counter(nums)
        print(n_counter)

        for count in n_counter.values():
            if count > 1:
                return True

        return False


if __name__ == '__main__':
    num_list = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(Solution.containsDuplicate(num_list))
