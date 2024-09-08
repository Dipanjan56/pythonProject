"""Sqrt(x)"""
from head_first_python_tutorial.basics.DataStructure.list import squares

"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
 

Constraints:

0 <= x <= 231 - 1
"""

"""
Approach:

We can solve this problem using binary search. Since the square root of a number grows slower than the number itself, binary search is a very efficient way to find the square root.

Here’s a step-by-step breakdown of how binary search works for this problem:

	1.	Initial bounds: The square root of x is always between 0 and x (for x > 1). For example:
	•	If x = 4, the square root is between 0 and 4.
	•	If x = 8, the square root is between 0 and 8.
	2.	Binary search:
	•	We low with two pointers, low = 0 and high = x.
	•	We calculate the midpoint mid = (low + high) // 2.
	•	We check if mid * mid is equal to x (in which case mid is the exact square root), greater than x (in which case the square root must be smaller, so we move the high pointer), or less than x (in which case the square root must be larger, so we move the low pointer).
	3.	Stopping condition: The binary search continues until low exceeds high. When it stops, low points to the nearest integer square root of x.

Binary Search Algorithm:

	1.	Set low = 0 and high = x.
	2.	While low <= high:
	•	Set mid = (low + high) // 2.
	•	If mid * mid == x, return mid.
	•	If mid * mid < x, set low = mid + 1.
	•	Otherwise, set high = mid - 1.
	3.	If no exact square root is found, return high (which will be the integer square root rounded down).
	
	
	for x = 8,
	
	 | low | high | mid | condition |
	 |  0  |  8   |  4  |  4*4 > 8  |
	 |  0  |  3   |  1  |  1*1 < 8  |
	 |  2  |  3   |  2  |  2*2 < 8  |
	 |  3  |  3   |  3  |  3*3 > 9  |
	 |  3  |  2   |exit |   exit    |
	 
	 after loop exit, high = 2 which is the nearest square root of 8 
"""

def my_sqrt(x: int) -> int:
    if x == 0 or x == 1:
        return x

    low, high = 0, x

    while low <= high:
        mid = (low + high) // 2

        if mid * mid == x:
            return mid
        elif mid * mid < x:
            low = mid + 1
        elif mid * mid > x:
            high = mid - 1
    return high


if __name__ == '__main__':
    x = 8
    print(my_sqrt(x))
