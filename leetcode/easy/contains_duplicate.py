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
    """using counter data tructure"""

    def containsDuplicate_using_counter(nums: List[int]) -> bool:
        num_counter = Counter(nums)
        print(num_counter)

        for key, value in num_counter.items():
            if value > 1:
                print(f'duplicate value: {key}')
                return True
        return False

    def containsDuplicate_using_for_loop(nums: List[int]) -> bool:
        for i in range(0, len(nums) - 1):
            count = 0
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    count += 1
                    print(f'duplicate value: {nums[i]}')
                    return True
        return False


if __name__ == '__main__':
    num_list = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(Solution.containsDuplicate_using_counter(num_list))
    print(Solution.containsDuplicate_using_for_loop(num_list))
