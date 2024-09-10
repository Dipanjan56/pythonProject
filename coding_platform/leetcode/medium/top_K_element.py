"""Top K Element"""
from typing import List

"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

"""
Approach:

	1.	Manually Count Frequencies:
	•	Create a dictionary to count the frequency of each element in the array.
	2.	Sort the Elements by Frequency:
	•	After counting the frequencies, convert the dictionary into a list of tuples (element, frequency) and sort it based on frequency in descending order.
	3.	Return the Top k Elements:
	•	After sorting, select the top k elements from the sorted list and return them.

"""

def topKFrequent(nums: List[int], k: int) -> List[int]:
    frequency_dict = {}

    for num in nums:
        frequency_dict.setdefault(num, 0)
        frequency_dict[num] += 1

    print(frequency_dict)

    sorted_frequency_list = sorted(frequency_dict.items(), key=lambda x: x[1], reverse=True)
    print(sorted_frequency_list)

    top_k_list = [element for element, index in sorted_frequency_list[:k]]

    return top_k_list


if __name__ == '__main__':
    nums = [1,1,1,2,2,3]
    k = 2
    print(topKFrequent(nums, k))