from typing import List

"""for binary search, array/list needs to be sorted"""


def binary_search_recursion(nums: List[int], start, end, x):
    nums = sorted(nums)
    mid = (start + end) // 2
    # it will give me nearest integer at the lower end i.e 7//2 = 3
    if x == nums[mid]:
        return mid
    elif x < nums[mid]:
        binary_search_recursion(nums, start, mid - 1, x)
    elif x > nums[mid]:
        binary_search_recursion(nums, mid + 1, end, x)
    else:
        return -1


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    x = 3
    print(f'number {x} found at index: {binary_search_recursion(nums, 0, len(nums) - 1, x)}')
