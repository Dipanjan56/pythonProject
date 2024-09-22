"""Products of Array Discluding Self"""

"""
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in O(n) time without using the division operation?

Example 1:

Input: nums = [1,2,4,6]

Output: [48,24,12,8]
Example 2:

Input: nums = [-1,0,1,2,3]

Output: [0,-6,0,0,0]
Constraints:

2 <= nums.length <= 1000
-20 <= nums[i] <= 20


"""

from typing import List

"""
Time Complexity : O(n^2)
"""
def productExceptSelf(nums: List[int]) -> List[int]:
    product_list = []
    for i in range(len(nums)):
        product = 1
        for j in range(len(nums)):
            if i != j:
                product *= nums[j]
        product_list.append(product)

    return product_list


"""
Approach:

	1.	Prefix Product: For each index i, calculate the product of all the elements before i (i.e., to the left of i).
	2.	Suffix Product: Similarly, for each index i, calculate the product of all the elements after i (i.e., to the right of i).
	3.	Result: Multiply the prefix product and the suffix product for each index i to get the desired output for output[i].

Solution Steps:

	1.	Initialize Two Arrays:
	•	One array for the prefix products.
	•	Another array for the suffix products.
	2.	Calculate Prefix Products:
	•	Traverse the array from left to right, and for each element, store the product of all previous elements.
	3.	Calculate Suffix Products:
	•	Traverse the array from right to left, and for each element, store the product of all the elements to its right.
	4.	Compute the Output:
	•	Multiply the corresponding prefix and suffix products for each index to get the result.
	
	Time Complexity : O(n)
"""
def productExceptSelf_optimized(nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        for i in range(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res


if __name__ == '__main__':
    nums = [1,2,4,6]
    print(productExceptSelf(nums))
    print(productExceptSelf_optimized(nums))