"""Top K Element"""
import heapq
from collections import Counter
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
    sorted_frequency_list = sorted(frequency_dict.items(), key=lambda x: x[1], reverse=True)

    # we are using element. index as inside list there is tuple: eg: [(1, 3), (2, 2), (3, 1)]
    top_k_list = [element for element, index in sorted_frequency_list[:k]]

    return top_k_list

"""
Time Complexity: 

1. num_counter = Counter(nums):

	•	This step creates a frequency dictionary (Counter) where the keys are the unique elements from nums and the values are their counts.
	•	Time complexity: O(n), where n is the number of elements in the nums list. This is because each element in nums is processed once to build the frequency counter.

2. sorted(num_counter.items(), key=lambda x:x[1], reverse=True)[:k]:
	•	num_counter.items() returns a list of tuples containing each unique number and its frequency. There are at most m items, where m is the number of unique elements in nums.
	•	Sorting this list by frequency (x[1]) takes O(m log m), where m is the number of unique elements in nums.
	•	After sorting, we slice the first k elements, which is an O(k) operation.

3. result = [num[0] for num in freq_list]:

	•	This list comprehension extracts the k most frequent elements from the sorted list.
	•	Time complexity: O(k), where k is the number of elements you want to return.

Total Time Complexity:

	•	Building the frequency counter: O(n)
	•	Sorting the frequency list: O(m log m), where m is the number of unique elements in nums.
	•	Slicing the sorted list and list comprehension: O(k).

Thus, the overall time complexity is O(n + m log m), where:

	•	n is the total number of elements in the list nums.
	•	m is the number of unique elements in nums.

In the worst case, m is proportional to n (i.e., when all elements in nums are unique), so the time complexity can be approximated as O(n log n) in such scenarios.
"""

def topKFrequent_usingCounter(nums: List[int], k: int) -> List[int]:
    num_counter = Counter(nums)
    k_most_freq_list = sorted(num_counter.items(), key=lambda x: x[1], reverse=True)[:k]
    top_k_list =  [num[0] for num in k_most_freq_list]
    return top_k_list

"""
# Step 1: Count the frequency of each element
# Step 2: Use a heap to get the k most frequent elements
# The heapq.nlargest function finds the k largest elements based on the frequency.

Time Complexity:

	1.	Counting Frequencies: Counting the frequency of each element takes O(n), where n is the number of elements in nums.
	2.	Finding the Top k Elements: The heap operation to extract the top k elements takes O(m log k), where m is the 
	number of unique elements in nums. In the worst case, m can be up to n.

Thus, the overall time complexity is O(n + m log k), which simplifies to O(n log k) in most cases 
since m is typically smaller than n.
"""
def topKFrequent_using_heapq(nums, k):
    num_counter = Counter(nums)
    return [item for item, count in heapq.nlargest(k, num_counter.items(), key=lambda x: x[1])]


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(topKFrequent(nums, k))
    print(topKFrequent_usingCounter(nums, k))
    print(topKFrequent_using_heapq(nums, k))