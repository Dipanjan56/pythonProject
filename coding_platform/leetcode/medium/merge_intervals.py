"""merge intervals"""

"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""


def merge_intervals(intervals):
    # If the list is empty, return an empty list
    if not intervals:
        return []

    # Sort the intervals based on the starting time
    intervals.sort(key=lambda x: x[0])

    # Initialize the merged list with the first interval
    merged = [intervals[0]]

    # Iterate over the intervals starting from the second one
    for i in range(1, len(intervals)):
        current_start, current_end = intervals[i]
        last_start, last_end = merged[-1]

        # If the current interval overlaps with the last one in the merged list, merge them
        if current_start <= last_end:
            merged[-1] = [last_start, max(last_end, current_end)]
        else:
            # If they don't overlap, add the current interval to the merged list
            merged.append([current_start, current_end])

    return merged


if __name__ == '__main__':
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(merge_intervals(intervals))