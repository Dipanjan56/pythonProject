""""""
import math
from typing import List


def print_fibonacci(count: int):
    n1 = 0
    n2 = 1
    print(n1)
    print(n2)
    for _ in range(count):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        print(n3)


def reverse_integer(num: int):
    rev_num = 0
    while num > 0:
        reminder = num % 10
        num = num // 10
        rev_num = (rev_num * 10) + reminder
    return rev_num


def check_prime(num: int) -> bool:
    if num == 2:
        return True
    elif num == 0 or num == 1 or num % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(num)), 2):
            if num % i == 0:
                return False
    return True


def binary_search_recursion(arr: List[int], start, end, target):
    mid = (start + end) // 2

    if target == arr[mid]:
        return mid
    elif target < arr[mid]:
        return binary_search_recursion(arr, 0, mid - 1, target)
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
        else:
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
        for j in range(i + 1, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            return arr


def merge_sort(arr: List[int]):
    if len(arr) > 1:
        left_arr = arr[:len(arr) // 2]
        right_arr = arr[len(arr) // 2:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        i = j = k = 0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

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
    arr = [4, 1, 5, 2, 3, 9, 7, 6]
    arr_sorted = [5, 7, 8, 9, 11, 20]
    print_fibonacci(5)
    print(reverse_integer(123))
    print(check_prime(149))
    print(binary_search_recursion(arr_sorted, 0, len(arr_sorted) - 1, 7))
    print(binary_search_iteration(arr_sorted, 7))
    print(insertion_sort(arr))
    print(bubble_sort(arr))
    print(merge_sort(arr))
    nums = [0, 1, 2, 4, 5, 7]
