""""""
from typing import List

"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

 

Constraints:

    0 <= nums.length <= 105
    -109 <= nums[i] <= 109


"""


def longest_consecutive(nums: List[int]) -> int:
    nums = sorted(list(set(nums)))
    max_seq = 0
    seq_length = 0

    if len(nums) == 1:
        return 1

    for i in range(0, len(nums) - 1):
        if nums[i + 1] - nums[i] == 1:
            seq_length += 1
        else:
            seq_length = 0
        max_seq = max(seq_length + 1, max_seq)
    return max_seq


if __name__ == '__main__':
    nums = [100,4,200,1,3,2]
    print(longest_consecutive(nums))
