"""question"""
"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).

"""
import math
from typing import List

"""this is my solution using two for loops, not an optimized one"""


def minSubArrayLen(nums: List[int], target: int, ) -> int:
    min_len = math.inf
    for i in range(len(nums) - 1):
        current_sum = nums[i]
        for j in range(i + 1, len(nums)):
            if nums[i] >= target or nums[j] >= target:
                return 1
            current_sum += nums[j]
            if current_sum >= target:
                index_len = j - i + 1
                min_len = min(min_len, index_len)
                break
    if min_len == math.inf:
        return 0
    return min_len


"""use sliding window"""


def minSubArrayLen_optyimized(nums: List[int], target: int) -> int:
    left = 0
    current_sum = 0
    min_length = float('inf')

    for right in range(len(nums)):
        current_sum += nums[right]  # Expand the window by including nums[right]

        # Shrink the window from the left as long as the condition is satisfied
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return min_length if min_length != float('inf') else 0


if __name__ == '__main__':
    nums = [2, 3, 1, 2, 4, 3]
    target = 7
    print(minSubArrayLen(nums, target))
    print(minSubArrayLen_optyimized(nums, target))
