"""Containers with most water"""
from typing import List

"""
link: https://leetcode.com/problems/container-with-most-water/description/?envType=study-plan-v2&envId=top-interview-150

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""

"""Time complexity: O(N) | using two pointers approach"""


def maxArea_optimized(height: List[int]) -> int:
    left = 0  # Pointer at the beginning
    right = len(height) - 1  # Pointer at the end
    max_area = 0  # Variable to track the maximum area

    # Iterate while left pointer is less than right pointer
    while left < right:
        # Calculate the current area
        width = right - left
        current_area = width * min(height[left], height[right])

        # Update the maximum area if the current area is greater
        max_area = max(max_area, current_area)

        # Move the pointer that has the shorter line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area


if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(maxArea_optimized(height))
