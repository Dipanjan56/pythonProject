"""question"""

"""
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays 
and you may return the result in any order.



Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.


Constraints:
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
"""
from typing import List


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    new_list = []

    if len(nums1) > len(nums2) or len(nums1) == len(nums2):
        for n1 in nums1:
            if n1 in nums2:
                new_list.append(n1)
                nums2.remove(n1)
    else:
        for n2 in nums2:
            if n2 in nums1:
                new_list.append(n2)
                nums1.remove(n2)

    return new_list




if __name__ == '__main__':
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print(intersect(nums1, nums2))
