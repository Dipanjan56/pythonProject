"""Binary Search"""

"""
1. binary search(logarithmic search) is a method for finding the position of an item in a SORTED list
2. the algorithm makes logN comparison in worst-case
3. hence running time complexity is O(logN)
4. it has practical and real world applications as O(logN) running time is quite favourable - 
   it is close to O(1) constant running time
"""
from typing import List


def binary_search(num_list: List[int], item, start, end) -> int:
    # 1st base case: if item is not present in the container
    if end < start:
        return -1

    mid = (start + end) // 2

    # 2nd base case: if we find the item in the middle
    if num_list[mid] == item:
        return mid

    # if item is less than middle_num, then we can get the item in the left side of the sub_array
    # as this is a sorted list and hence we can discard the right side of the array
    if item < num_list[mid]:
        return binary_search(num_list, item, start, mid - 1)
    # if item is greater than middle_num, then we can get the item in the right side of the sub_array
    # as this is a sorted list and hence we can discard the left side of the array
    elif item > num_list[mid]:
        return binary_search(num_list, item, mid + 1, end)


if __name__ == '__main__':
    num_list = [7, 2, 5, 8, 4, 1, 3, 6]
    print(binary_search(num_list, 8, 0, len(num_list) - 1))
