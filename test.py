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


def binary_search_recursion(nums: List[int], left, right, target):
    mid = (left + right) // 2

    if target == nums[mid]:
        return mid
    elif target < nums[mid]:
        return binary_search_recursion(nums, 0, mid - 1, target)
    elif target > nums[mid]:
        return binary_search_recursion(nums, mid + 1, right, target)
    else:
        return -1


def binary_search_iteration(nums: List[int], target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            right = mid - 1
        elif target > nums[mid]:
            left = mid + 1
        else:
            return -1


def insertion_sort(nums: List[int]):
    for i in range(1, len(nums)):
        j = i
        while nums[j - 1] > nums[j] and j > 0:
            nums[j - 1], nums[j] = nums[j], nums[j - 1]
            j -= 1
    return nums


def bubble_sort(nums: List[int]) -> List[int]:
    length = len(nums)
    for i in range(length - 1):
        swapped = False
        # this is because after every iteration [i] the largest element will be placed at the last of the array
        # that is why we are keeping range as length - i -1
        for j in range(length - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if not swapped:
            return nums
    return nums


def merge_sort(nums: List[int]):
    if len(nums) > 1:
        left_nums = nums[:len(nums) // 2]
        right_nums = nums[len(nums) // 2:]

        merge_sort(left_nums)
        merge_sort(right_nums)

        i = 0
        j = 0
        k = 0

        while i < len(left_nums) and j < len(right_nums):
            if left_nums[i] < right_nums[j]:
                nums[k] = left_nums[i]
                i += 1
            else:
                nums[k] = right_nums[j]
                j += 1
            k += 1

        while i < len(left_nums):
            nums[k] = left_nums[i]
            i += 1
            k += 1

        while j < len(right_nums):
            nums[k] = right_nums[j]
            j += 1
            k += 1
    return nums


if __name__ == '__main__':
    nums = [4, 1, 5, 2, 3, 9, 7, 6]
    nums_sorted = [5, 7, 8, 9, 11, 20]
    print_fibonacci(5)
    print(reverse_integer(123))
    print(check_prime(149))
    print(binary_search_recursion(nums_sorted, 0, len(nums_sorted) - 1, 7))
    print(binary_search_iteration(nums_sorted, 7))
    print(insertion_sort(nums))
    print(bubble_sort(nums))
    print(merge_sort(nums))
    nums = [0, 1, 2, 4, 5, 7]
