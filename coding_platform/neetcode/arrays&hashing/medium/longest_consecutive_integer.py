"""longest consecutive integer"""

"""
Given an array of integers nums, return the length of the longest consecutive sequence of elements.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [2,20,4,10,3,4,5]

Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Example 2:

Input: nums = [0,3,2,5,4,6,1,1]

Output: 7
Constraints:

0 <= nums.length <= 1000
-10^9 <= nums[i] <= 10^9


"""

from typing import List


def longestConsecutive(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return 1

    nums = sorted(nums)
    max_count = 0
    count = 1

    for i in range(len(nums) - 1):
        if abs(nums[i + 1] - nums[i]) == 1:
            count += 1
        elif abs(nums[i + 1] - nums[i]) == 0:
            continue
        else:
            max_count = max(count, max_count)
            count = 1
    max_count = max(count, max_count)
    return max_count


if __name__ == '__main__':
    nums = [2, 20, 4, 10, 3, 4, 5]
    print(longestConsecutive(nums))
