""""""
"""
insertion sort-> Compare key with each element on the left of it until an element smaller than it is found
 Time complexity -> O(n2)
"""


def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j-1] > arr[j] and j > 0:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

    return nums


if __name__ == '__main__':
    nums = [4, 1, 7, 6, 2, 3]
    print('using insertion_sort: ', insertion_sort(nums))
