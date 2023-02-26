"""Linear Search"""
from typing import List

"""
1. linear search(sequential search) is a method for finding an item in unsorted list
2. the algorithm makes N comparisons in worst-case
3. hence the running time complexity is O(N) linear
4. but not that practical as we can achieve O(logN) or O(1) time complexity with binary search or hash tables
"""

"""using iteration"""


def linear_search_iteration(num_list: List[int], item: int) -> int:
    for index in range(len(num_list)):
        if num_list[index] == item:
            return index
            break
    return -1


"""using recursion"""


def linear_search_recursion(num_list: List[int], item: int, index=0) -> int:
    # 1st base case: if we s=dont find the item
    if index >= len(num_list):
        return -1
    # 2nd base case
    if num_list[index] == item:
        return index
    return linear_search_recursion(num_list, item, index + 1)


if __name__ == '__main__':
    num_list = [7, 2, 5, 8, 4, 1, 3, 6]
    print(linear_search_iteration(num_list, 8))
    print(linear_search_recursion(num_list, 8))
