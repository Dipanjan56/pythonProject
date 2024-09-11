from typing import List

"""in bubble_sort after first iteration, the highest number will be placed at the right most side
Time complexity is c * (n-1) * (n-1) ~= O(n2)
"""


def bubble_sort(nums: List[int]) -> List[int]:
    for i in range( len(nums) - 1):
        swapped = False
        # this is because after every iteration [i] the largest element will be placed at the last of the array
        # that is why we are keeping range as length - i -1
        for j in range( len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if not swapped:
            return nums
    return nums


if __name__ == '__main__':
    nums = [4, 1, 7, 6, 2, 3]
    print('using bubble_sort: ', bubble_sort(nums))
