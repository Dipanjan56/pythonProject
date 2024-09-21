"""Contains Duplicate"""
"""
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true


Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109

"""

from collections import Counter
from typing import List

"""
Time Complexity:

	•	The outer loop runs for each element in the list, i.e., O(n), where n is the length of the list nums.
	•	For each iteration of the loop, the in operator is used to search for nums[i] in the sublist nums[i + 1:].
	•	The sublist slicing nums[i + 1:] takes O(n - i) time and the in operation, which checks for membership, also takes linear time, i.e., O(n - i).

In the worst case, this results in:

	•	First iteration: O(n)
	•	Second iteration: O(n - 1)
	•	Third iteration: O(n - 2)
	•	…and so on.

So the overall time complexity is the sum:
\[ O(n + (n - 1) + (n - 2) + \dots + 1) = O(n^2) \]

Conclusion: The time complexity of this method is O(n²).
"""
def hasDuplicate(nums: List[int]) -> bool:
    for i in range(len(nums) - 1):
        if nums[i] in nums[i + 1:]:
            return True
    return False

"""
Time Complexity:

	•	The Counter(nums) function creates a dictionary where the keys are the elements of nums and the values are their counts. This step takes O(n), where n is the length of nums.
	•	The loop that checks if any value in the counter is greater than 1 iterates over the values of the dictionary, which has at most n unique elements. So this part takes O(n) in the worst case.

Conclusion: The time complexity of this method is O(n).
"""
def hasDuplicate_usingCounter(nums: List[int]) -> bool:
    num_counter = Counter(nums)

    for val in num_counter.values():
        if val is not 1:
            return True
    return False

"""
Here we sue set , as data retrieval in set is done by O(1) as set is hashable

Thats why Time complexity: O(n)
"""
def hasDuplicate_usingSet(nums: List[int]) -> bool:
    seen = set()

    for num in nums:
        if num in seen:
            return True
        else:
            seen.add(num)
    return False


if __name__ == '__main__':
    num_list = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(hasDuplicate(num_list))
    print(hasDuplicate_usingCounter(num_list))
    print(hasDuplicate_usingSet(num_list))
