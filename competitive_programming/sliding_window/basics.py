"""Sliding Window"""


"""
The sliding window approach is a commonly used algorithmic technique for solving problems that involve arrays or lists. 
The idea behind this approach is to maintain a window (a contiguous subarray) that moves or “slides” across the array 
to solve the problem efficiently.

It is particularly useful for problems that involve finding the maximum, minimum, or other properties (like sums or averages)
of subarrays of a fixed size, or for dynamically adjusting the window size based on some condition.

Key Concept:

	•	The window is defined by two pointers (usually called left and right), which represent the boundaries of the 
	current subarray.
	•	The sliding happens by moving either the right pointer to expand the window or the left pointer to shrink it,
	 depending on the problem.

Why Use Sliding Window?

The sliding window technique is used to reduce the time complexity from O(n²) to O(n) in problems that would otherwise 
require nested loops. This is because the window adjusts dynamically, meaning you don’t have to reprocess the entire 
subarray when expanding or shrinking the window.

Types of Sliding Windows:

	1.	Fixed-Sized Sliding Window: The window has a fixed size, and both pointers move simultaneously to maintain that size.
	•	Example: Finding the maximum sum of a subarray of size k.
	2.	Dynamic Sliding Window: The window size can grow or shrink based on certain conditions, and only one pointer 
	(either left or right) moves at a time.
	•	Example: Finding the smallest subarray with a sum greater than a given target.
	
Sliding Window Summary:

	1.	Fixed-Sized Window:
	•	Used when the problem involves processing every subarray of a specific size.
	•	Example: Finding the maximum sum of subarrays of size k.
	2.	Dynamic-Sized Window:
	•	Used when the problem requires adjusting the size of the window based on some condition (like the sum of the elements).
	•	Example: Finding the smallest subarray whose sum is greater than a target.

Sliding Window Advantages:

	•	Efficiency: Reduces the need for nested loops, allowing you to solve problems in O(n) time.
	•	Simplicity: By maintaining only a few variables (like the sum of the window or the current window size), 
	the sliding window approach is easy to implement.

Example Problems for Sliding Window:

	1.	Maximum/Minimum sum of a subarray.
	2.	Longest substring without repeating characters.
	3.	Smallest subarray with a sum greater than a target.
	4.	Longest contiguous subarray with a given sum.

Conclusion:

The sliding window approach is a powerful technique for solving problems where the solution involves finding subarrays 
or substrings. By maintaining a window that dynamically expands or contracts, this method allows you to solve problems 
efficiently in O(n) time.	

======================================================================================================================================================

Example 1: Fixed-Sized Sliding Window

Problem: Find the maximum sum of any subarray of size k.

Approach:

	1.	Maintain a window of size k.
	2.	Slide the window across the array, adding the new element entering the window and removing the element 
	that is leaving.
	3.	Track the maximum sum encountered.
"""

"""
Explanation:

	•	The window starts at the first k elements.
	•	For each step, you add the element entering the window (arr[i]) and subtract the element 
	leaving the window (arr[i - k]).
	•	The time complexity is O(n) because each element is processed once.
"""
def maxSumSubarray(arr, k):
    n = len(arr)
    max_sum = 0
    window_sum = 0

    # Calculate the sum of the first window of size k
    for i in range(k):
        window_sum += arr[i]

    max_sum = window_sum

    # Slide the window across the array
    for i in range(k, n):
        window_sum += arr[i] - arr[i - k]  # Add the new element and remove the old one
        max_sum = max(max_sum, window_sum)

    return max_sum

"""
Example 2: Dynamic Sliding Window

Problem: Given an array of positive integers, find the smallest subarray with a sum greater than or equal to a given target.

Approach:

	1.	Use two pointers (left and right) to define the window.
	2.	Expand the window by moving right to include more elements.
	3.	Shrink the window by moving left when the sum exceeds the target.
	4.	Track the smallest window that satisfies the condition.
"""

"""
Explanation:

	•	We start by expanding the window (right pointer) until the sum exceeds or equals the target.
	•	Once the sum is greater than or equal to the target, we start shrinking the window (left pointer) 
	while maintaining the sum condition.
	•	The time complexity is O(n) because each element is added and removed from the window once.
"""
def minSubArrayLen(target, nums):
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