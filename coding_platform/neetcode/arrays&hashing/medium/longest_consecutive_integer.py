"""longest consecutive integer"""

"""
Given an array of integers nums, return the length of the longest consecutive sequence of elements.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [2,20,4,10,3,4,5]

Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Example 2:

Input: nums = [0,3,2,5,4,6,1,1]

Output: 7
Constraints:

0 <= nums.length <= 1000
-10^9 <= nums[i] <= 10^9


"""

from typing import List


def longestConsecutive_1(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return 1

    nums = sorted(nums)
    max_count = 0
    count = 1

    for i in range(len(nums) - 1):
        if abs(nums[i + 1] - nums[i]) == 1:
            count += 1
        elif abs(nums[i + 1] - nums[i]) == 0:
            continue
        else:
            max_count = max(count, max_count)
            count = 1
        max_count = max(count, max_count)
    return max_count

"""
Total Time Complexity:

	•	O(n) for converting the input list to a set to remove duplicates.
	•	O(m log m) for sorting the list of m unique elements.
	•	O(m) for the final loop that checks consecutive elements.

Thus, the overall time complexity is O(n + m log m + m). Since m is at most n (the number of unique elements cannot exceed the number of total elements), the time complexity simplifies to O(n log n).

Conclusion:

The time complexity of the given function is O(n log n), where n is the length of the input list nums.
"""
def longestConsecutive_2(nums: List[int]) -> int:
    nums = sorted(list(set(nums)))
    print(nums)

    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return 1

    count = 1
    max_count = 0

    for i in range(len(nums) - 1):
        if abs(nums[i + 1] - nums[i]) == 1:
            count += 1
        else:
            max_count = max(count, max_count)
            count = 1
        max_count = max(count, max_count)
    return max_count

"""

Approach:

	1.	Use a Set for Efficient Lookups: Store all the elements in a set. This allows for O(1) average time complexity for checking if an element exists in the set.
	2.	Only Start from the Beginning of a Sequence: For each element, check if it’s the start of a sequence (i.e., the previous element is not in the set). If it’s the start, calculate the length of the sequence by checking how many consecutive numbers exist after it.
	3.	Track the Maximum Length: For each sequence, keep track of its length and update the maximum length found.


Explanation:

	1.	Hash Set Creation:
	•	We first convert the array into a set (num_set) to allow constant-time lookups.
	2.	Check for the Start of a Sequence:
	•	For each element num, we check if num - 1 is not in the set. If it’s not, that means num is the start of a consecutive sequence.
	3.	Count Consecutive Numbers:
	•	From num, we keep checking for consecutive numbers (num + 1, num + 2, …) and count how long the sequence is.
	4.	Track Maximum Length:
	•	We track the length of each sequence and update the maximum length found so far (longest_streak).
	
	
Time Complexity:

	•	O(n): We visit each number at most twice—once when we check if it’s the start of a sequence and then for counting the length of the sequence.
	•	Space Complexity: O(n) because we store all elements in a set.
"""

def longestConsecutive_optimized(nums):
    # Step 1: Convert the list into a set to allow O(1) lookups
    num_set = set(nums)
    longest_streak = 0

    # Step 2: Iterate through the set
    for num in num_set:
        # Check if this number is the start of a sequence
        if num - 1 not in num_set:  # Only start counting if `num` is the start of the sequence
            current_num = num
            current_streak = 1

            # Count how long the streak is
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            # Update the longest streak
            longest_streak = max(longest_streak, current_streak)

    return longest_streak


if __name__ == '__main__':
    #nums = [2, 20, 4, 10, 3, 4, 5]
    nums = [4, 0, -4, -2, 2, 5, 2, 0, -8, -8, -8, -8, -1, 7, 4, 5, 5, -4, 6, 6, -3]
    print(longestConsecutive_1(nums))
    print(longestConsecutive_2(nums))
    print(longestConsecutive_optimized(nums))
