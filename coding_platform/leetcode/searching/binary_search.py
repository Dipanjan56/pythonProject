from typing import List

"""for binary search, array/list needs to be sorted"""


def binary_search_recursion(arr: List[int], start, end, target):
    mid = (start + end) // 2

    if target == arr[mid]:
        return mid
    elif target < arr[mid]:
        return binary_search_recursion(arr, start, mid - 1, target)
    elif target > arr[mid]:
        return binary_search_recursion(arr, mid + 1, end, target)
    else:
        return -1


def binary_search_iteration(arr: List[int], target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            end = mid - 1
        elif target > arr[mid]:
            start = mid + 1
    return -1


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6]
    x = 3
    print(f'binary_search_recursion: number {x} found at index: {binary_search_recursion(nums, 0, len(nums) - 1, x)}')
    print(f'binary_search_iteration: number {x} found at index: {binary_search_iteration(nums, x)}')
