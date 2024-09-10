""""""
import functools

"""
Given an array and a value, find if there is a triplet in array whose sum is equal to the given value. If there is such a triplet present in array, then print the triplet and return true. Else return false.
Examples: 
Input: array = {12, 3, 4, 1, 6, 9}, sum = 24; 
Output: 12, 3, 9 
Explanation: There is a triplet (12, 3 and 9) present 
in the array whose sum is 24. 
Input: array = {1, 2, 3, 4, 5}, sum = 9 
Output: 5, 3, 1 
Explanation: There is a triplet (5, 3 and 1) present 
in the array whose sum is 9.
"""
from typing import List

"""This is the optimized approach
Time-complexity: O(n^2)
"""


def get_nums(arr: List[int], sum: int) -> bool:
    for i in range(len(arr)):
        for j in range(i + 1, len(arr) - 1):
            two_sum = arr[i] + arr[j]
            remaining_num = sum - two_sum
            if remaining_num in arr[j + 1:]:
                print(f'{arr[i]} | {arr[j]} | {remaining_num}')
                return True




if __name__ == '__main__':
    array = [12, 3, 4, 1, 6, 9]
    sum = 13
    print(get_nums(array, sum))
