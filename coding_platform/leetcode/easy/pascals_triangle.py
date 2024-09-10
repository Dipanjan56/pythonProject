""""""
from typing import List

"""

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:

Input: numRows = 1
Output: [[1]]

 

Constraints:

    1 <= numRows <= 30

"""

"""Using Bottoms Up approach - Dynamic Programing -> time-complexity -> O(numRows^2)"""


def pascals_triangle(numRows: int) -> List[List[int]]:
    result_arr = []

    for i in range(numRows):
        dp = [None] * (i + 1)
        dp[0] = 1
        dp[-1] = 1
        if i > 1:
            previous_arr = result_arr[i - 1]
            for j in range(1, len(dp) - 1):
                dp[j] = previous_arr[j - 1] + previous_arr[j]
        result_arr.append(dp)

    return result_arr


if __name__ == '__main__':
    numRows = 5
    print(pascals_triangle(5))
