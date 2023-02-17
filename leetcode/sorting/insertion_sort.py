"""
insertion sort-> Compare key with each element on the left of it until an element smaller than it is found
For descending order, change key<array[j] to key>array[j]
Place key at after the element just smaller than it
 Time complexity -> O(n2)
"""


def insertion_sort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]
            j = j - 1
        nums[j + 1] = key

    return nums


if __name__ == '__main__':
    nums = [4, 1, 7, 6, 2, 3]
    print('using insertion_sort: ', insertion_sort(nums))
