""""""

"""
Merge two sorted array

Example 1:
arr1 = [1, 3, 5, 8, 9, 12, 12, 17]
arr2 = [2, 4, 6, 8, 12]
Output: [1, 2, 3, 4, 5, 6, 8, 8, 9, 12, 12, 12, 17]

"""

"""use merge sort technique"""

def merge_array(arr1: list, arr2: list) -> list:
    merged = []
    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    while i < len(arr1):
        merged.append(arr1[i])
        i += 1

    while j < len(arr2):
        merged.append(arr2[j])
        j += 1

    print(merged)
    return merged

if __name__ == '__main__':
    arr1 = [1, 3, 5, 8, 9, 12, 12, 17]
    arr2 = [2, 4, 6, 8, 12]
    merge_array(arr1, arr2)