""""""
import math
from typing import List


def reverse_integer(num: int):
    rev_num = 0
    while num > 0:
        reminder = num % 10
        num = num // 10
        rev_num = (rev_num * 10) + reminder

    return rev_num


def check_prime(num: int):
    if num == 2:
        return True
    if num == 0 or num == 1 or num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)), 2):
        if num % i == 0:
            return False
    return True


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


def insertion_sort(arr: List[int]):
    for i in range(1, len(arr)):
        j = i
        while arr[j - 1] > arr[j] and j > 0:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1

    return arr


def bubble_sort(arr: List[int]):
    swapped = False
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            return arr


def merge_sort(arr: List[int]):
    if len(arr) > 1:
        arr_left = arr[: len(arr) // 2]
        arr_right = arr[len(arr) // 2:]

        merge_sort(arr_left)
        merge_sort(arr_right)

        i = j = k = 0
        while i < len(arr_left) and j < len(arr_right):
            if arr_left[i] < arr_right[j]:
                arr[k] = arr_left[i]
                i += 1
            else:
                arr[k] = arr_right[j]
                j += 1
            k += 1

        while i < len(arr_left):
            arr[k] = arr_left[i]
            i += 1
            k += 1

        while j < len(arr_right):
            arr[k] = arr_right[j]
            j += 1
            k += 1

    return arr


if __name__ == '__main__':
    arr = [4, 1, 5, 2, 3, 9, 7, 6]
    arr_sorted = [5, 7, 8, 9, 11, 20]
    print(reverse_integer(123))
    print(check_prime(2))
    print(binary_search_recursion(arr_sorted, 0, len(arr_sorted) - 1, 7))
    print(binary_search_iteration(arr_sorted, 7))
    print(insertion_sort(arr))
    print(bubble_sort(arr))
    print(merge_sort(arr))
