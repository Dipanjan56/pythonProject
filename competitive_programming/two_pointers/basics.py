"""Two Pointers"""

"""
The two-pointer algorithm is a technique commonly used in array or list problems where two pointers (or indices) are 
used to traverse the array or compare elements from two ends or positions in the array simultaneously. 
This method helps solve various problems efficiently by reducing the need for nested loops, which would otherwise 
increase time complexity.

Key Characteristics:

	1.	Two Pointers: The algorithm involves two pointers, which are typically initialized at different positions in the
	 array (often one at the beginning and the other at the end).
	2.	Movement of Pointers: Depending on the problem, the pointers either move toward each other or in the same 
	direction, making decisions on how to adjust the pointers based on the logic of the problem.
	3.	Optimization: It is used when a brute-force approach would require more than O(n) time complexity. 
	With two pointers, the traversal is often linear, i.e., O(n).

Types of Two-Pointer Techniques:

	1.	Opposite Direction (Converging):
	•	Pointers are typically placed at the two ends of the array, and they move toward each other.
	•	Example problems: Finding the two numbers that add up to a specific target in a sorted array, or finding the 
	maximum area in the “Container With Most Water” problem.
	2.	Same Direction (Sliding Window):
	•	Both pointers start at the same position and one of them moves ahead of the other, either trying to expand or 
	contract the range.
	•	Example problems: Finding subarrays with a given sum, or finding the longest substring without repeating characters.

Advantages of Two-Pointer Algorithm:

	1.	Efficient: It often reduces the time complexity from O(n^2) to O(n) by eliminating the need for nested loops.
	2.	Simple: Easy to implement for problems related to arrays or lists.
	3.	Versatile: Can be applied to a wide variety of problems, including finding pairs, detecting patterns, 
	and searching ranges.

Common Use Cases:

	•	Finding pairs in a sorted array.
	•	Finding the maximum or minimum values based on a condition.
	•	Checking for palindromes.
	•	Solving problems involving subarrays or sublists.

Conclusion:

The two-pointer algorithm is a powerful and efficient technique for solving problems that involve traversing arrays 
or lists, especially when the problem involves pairs, ranges, or sequences. By intelligently moving the two pointers, 
you can solve problems with reduced time complexity, making it a go-to approach for many array-related problems.	
	

======================================================================================================================================================

Example Problem 1: Two-Sum (Sorted Array)

Problem: Given a sorted array of integers, find two numbers that add up to a specific target.

Two-pointer approach:

	1.	Initialize pointers: One pointer starts at the beginning (left = 0) and another at the end (right = n - 1) 
	of the array.
	2.	Check sum:
	•	If the sum of the numbers at the two pointers is equal to the target, return those numbers.
	•	If the sum is less than the target, move the left pointer to the right (i.e., increase the sum).
	•	If the sum is greater than the target, move the right pointer to the left (i.e., decrease the sum).
	3.	Repeat until the two pointers meet or the target is found.
"""


def two_sum(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []  # No solution found


if __name__ == '__main__':
    nums = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    target = 10
    print(two_sum(nums, target))
