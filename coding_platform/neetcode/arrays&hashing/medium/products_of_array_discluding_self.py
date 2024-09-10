"""Products of Array Discluding Selfe"""

"""
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in 
O
(
n
)
O(n) time without using the division operation?

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


def productExceptSelf(nums: List[int]) -> List[int]:
    if len(nums) == 2:
        return nums[::-1]

    product_list = []
    for i in range(len(nums)):
        product = 1
        for j in range(len(nums)):
            if i != j:
                product *= nums[j]
        product_list.append(product)

    return product_list


if __name__ == '__main__':
    nums = [1,2,4,6]
    print(productExceptSelf(nums))