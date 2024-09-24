"""Move All Duplicates to the Right of an Array"""
from typing import List

"""
You are give na array, move all the duplicates element of the array to the right so that all the unique elements
are in the left

input: nums = [10,15,10,25,10,7,9,9,25]

output = [10,15,25,7,9,.......]

"""

def move_duplicate_to_right(nums: List[int]) -> List[int]:
    seen_set = set()
    idx = 0

    for i in range(len(nums)):
        if nums[i] not in seen_set:
            nums[idx] = nums[i]
            idx += 1
        seen_set.add(nums[i])

    while idx < len(nums) :
        nums[idx] = None
        idx+=1

    return nums

if __name__=='__main__':
    nums = [10, 15, 10, 25, 10, 7, 9, 9, 25]
    print(move_duplicate_to_right(nums))

