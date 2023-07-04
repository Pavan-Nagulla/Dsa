"""
Search Insert Position
Problem Statement: You are given a sorted array arr of distinct values and a target value x. You need to search for the index of the target value in the array.

If the value is present in the array, then return its index. Otherwise, determine the index where it would be inserted in the array while maintaining the sorted order.


"""

"""

Example 1:
Input Format: arr[] = {1,2,4,7}, x = 6
Result: 3
Explanation: 6 is not present in the array. So, if we will insert 6 in the 3rd index(0-based indexing), the array will still be sorted. {1,2,4,6,7}.

Example 2:
Input Format: arr[] = {1,2,4,7}, x = 2
Result: 1
Explanation: 2 is present in the array and so we will return its index i.e. 1.
"""

def search_insert(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left


# Test case 1
arr1 = [1, 3, 5, 6]
target1 = 5
print("Result for Test case 1:", search_insert(arr1, target1))

# Test case 2
arr2 = [1, 3, 5, 6]
target2 = 2
print("Result for Test case 2:", search_insert(arr2, target2))

# Test case 3
arr3 = [1, 3, 5, 6]
target3 = 7
print("Result for Test case 3:", search_insert(arr3, target3))

# Test case 4
arr4 = [1, 3, 5, 6]
target4 = 0
print("Result for Test case 4:", search_insert(arr4, target4))
