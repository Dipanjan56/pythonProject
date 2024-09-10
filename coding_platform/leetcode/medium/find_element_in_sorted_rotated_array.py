""""""

"""
Given a sorted rotated array. Find an element in the array. Print -1 if element does not exist else print the position.
 Eg 4,6,8,99,1,2 : Find 99. Solution: 3
"""


def find_element_in_sorted_rotated_array(nums: list, target: int):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1

if __name__ == '__main__':

    arr3 = [4, 5, 6, 8, 99, 1, 2 ]
    arr4 = [7, 9, 12, 17, 1, 2, 3, 4, 5, 6]
    target = 4
    print(f'input arr: {arr4}')
    print(f'Find: {target}')
    print(f'Solution: {find_element_in_sorted_rotated_array(arr4, target)}')