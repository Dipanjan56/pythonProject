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

"most optimized approach"
def occurrence_one_pointer_1(nums: list):
    occurrence_dict = {}
    for n in nums:
        if n not in occurrence_dict.keys():
            occurrence_dict[n] = 0
        occurrence_dict[n] += 1
    print(occurrence_dict)

    


def occurrence_one_pointer_2(nums: list):
    num_dict = {}
    for num in nums:
        num_dict.setdefault(num, 0)
        num_dict[num] += 1

    print(num_dict)

    value_dict = {}

    value_list = sorted(num_dict.values())[::-1]
    print(value_list)

    for key, value in num_dict.items():
        if value not in value_dict:
            value_dict[value] = []
        value_dict[value].append(key)

    print(value_dict)

    value_set = set()
    for val in value_list:
        if val not in value_set:
            print(f'{val} : {value_dict[val]}')
            value_set.add(val)


if __name__ == '__main__':
    nums = [4, 1, 2, 2, 3, 4, 5, 8, 5, 6, 9, 1, 9, 3, 4, 4, 1]
    # occurence_two_pointer(nums)
    occurrence_one_pointer_1(nums)
