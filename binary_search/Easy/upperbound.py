"""
Implement Upper Bound
Problem Statement: Given a sorted array of N integers and an integer x, write a program to find the upper bound of x.
"""

"""
Example 1:
Input Format: N = 4, arr[] = {1,2,2,3}, x = 2
Result: 3
Explanation: Index 3 is the smallest index such that arr[3] > x.

Example 2:
Input Format: N = 6, arr[] = {3,5,8,9,15,19}, x = 9
Result: 4
Explanation: Index 4 is the smallest index such that arr[4] > x.

"""


def upper_bound(arr, x):
    left = 0
    right = len(arr) - 1
    result = len(arr)

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] > x:
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result


# Test case 1
arr1 = [1, 2, 2, 3]
x1 = 2
print("Result for Test case 1:", upper_bound(arr1, x1))

# Test case 2
arr2 = [3, 5, 8, 9, 15, 19]
x2 = 9
print("Result for Test case 2:", upper_bound(arr2, x2))
