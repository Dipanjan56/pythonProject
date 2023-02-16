from typing import List

"""in selection_sort we first search for the index where where lowest number resides, and then swap it
 and as a result the lowest number will be placed at the left most side"""


def selection_sort(nums: List[int]) -> List[int]:
    for i in range(len(nums)):
        min_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums


if __name__ == '__main__':
    nums = [4, 1, 7, 6, 2, 3]
    print('using selection_sort: ', selection_sort(nums))
