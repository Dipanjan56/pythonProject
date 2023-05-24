"""merge sort: for this sort, we use recursive algorithm with divide and conquer strategy
 Time complexity -> O(nlogn)
 But it requires extra memory, hence Space complexity -> O(n)
"""
from typing import List


def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) > 1:
        # divide the array in two halves
        left_arr = arr[len(arr) // 2:]
        right_arr = arr[:len(arr) // 2]

        # use recursion
        merge_sort(left_arr)
        merge_sort(right_arr)

        # merge the arrays after sorting
        i = 0  # left array index
        j = 0  # right array index
        k = 0  # merged array index

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        # merge the remaining numbers

        # When we run out of elements in either left_arr or right_arr,
        # pick up the remaining elements and put in arr
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

    return arr


if __name__ == '__main__':
    nums = [4, 1, 7, 6, 2, 3]
    print('using mergeSort: ', merge_sort(nums))
