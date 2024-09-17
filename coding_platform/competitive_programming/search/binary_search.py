"""Binary Search"""

"""
1. binary search(logarithmic search) is a method for finding the position of an item in a SORTED list
2. the algorithm makes logN comparison in worst-case
3. hence running time complexity is O(logN)
4. it has practical and real world applications as O(logN) running time is quite favourable - 
   it is close to O(1) constant running time
"""

from typing import List


def binary_search_recursion(arr: List[int], left, right, target):
    mid = (left + right) // 2

    if target == arr[mid]:
        return mid
    elif target < arr[mid]:
        return binary_search_recursion(arr, left, mid - 1, target)
    elif target > arr[mid]:
        return binary_search_recursion(arr, mid + 1, right, target)
    else:
        return -1


def binary_search_iteration(arr: List[int], target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            right = mid - 1
        elif target > arr[mid]:
            left = mid + 1
    return -1


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6]
    x = 3
    print(f'binary_search_recursion: number {x} found at index: {binary_search_recursion(nums, 0, len(nums) - 1, x)}')
    print(f'binary_search_iteration: number {x} found at index: {binary_search_iteration(nums, x)}')


if __name__ == '__main__':
    num_list = [7, 2, 5, 8, 4, 1, 3, 6]
    print(binary_search(num_list, 8, 0, len(num_list) - 1))
