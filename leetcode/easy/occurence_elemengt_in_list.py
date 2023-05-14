""""""
from typing import List

"""find occurance of elements in a list
Example: nums = [4,1,2,2,3,4,5,8,5,6,9,1,9,3,4,4,1]
"""

"""time complexity: m * n"""


def occurence_two_pointer(nums: list):
    num_dict = {}
    num_set = set(nums)
    for num in num_set:
        num_dict[num] = 0
        for i in range(len(nums)):
            if num == nums[i]:
                num_dict[num] += 1

    print(num_dict)


"""time complexity: n"""


def occurence_one_pointer(nums: list):
    num_dict = {}
    for num in nums:
        num_dict.setdefault(num, 0)
        num_dict[num] += 1

    print(num_dict)


if __name__ == '__main__':
    nums = [4, 1, 2, 2, 3, 4, 5, 8, 5, 6, 9, 1, 9, 3, 4, 4, 1]
    occurence_two_pointer(nums)
    occurence_one_pointer(nums)
