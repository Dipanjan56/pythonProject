"""Search 2D Matrix"""

"""

You are given an m x n 2-D integer array matrix and an integer target.

Each row in matrix is sorted in non-decreasing order.
The first integer of every row is greater than the last integer of the previous row.
Return true if target exists within matrix or false otherwise.

Can you write a solution that runs in O(log(m * n)) time?

Example 1:



Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10

Output: true
Example 2:



Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15

Output: false
Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10000 <= matrix[i][j], target <= 10000



"""

from collections import Counter
from typing import List
"""
Time-complexity: O(m * log(n))
"""
def searchMatrix_1(matrix: List[List[int]], target: int) -> bool:
    for nums_list in matrix:
        if search(nums_list, target):
            return True
    return False


def search(nums: List[int], target: int) -> bool:
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = (start + end) // 2

        if target == nums[mid]:
            return True
        elif target < nums[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return False

"""
Time-complexity: O(log(m*n))
"""
def searchMatrix_optuimezed(matrix: List[List[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False

    # Dimensions of the matrix
    m = len(matrix)  # Number of rows
    n = len(matrix[0])  # Number of columns

    # Binary search on the conceptual 1D array
    start, end = 0, m * n - 1

    while start <= end:
        mid = (start + end) // 2
        # Convert 1D index back to 2D matrix indices
        mid_value = matrix[mid // n][mid % n]

        if mid_value == target:
            return True
        elif target < mid_value:
            end = mid - 1
        else:
            start = mid + 1

    return False


if __name__ == '__main__':
    matrix = [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]]
    target = 10

    print(searchMatrix_1(matrix, target))
    print(searchMatrix_optuimezed(matrix, target))
