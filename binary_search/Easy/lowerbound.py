"""
Implement Lower Bound
Problem Statement: Given a sorted array of N integers and an integer x, write a program to find the lower bound of x.


"""

"""
Example 1:
Input Format: N = 4, arr[] = {1,2,2,3}, x = 2
Result: 1
Explanation: Index 1 is the smallest index such that arr[1] >= x.

Example 2:
Input Format: N = 5, arr[] = {3,5,8,15,19}, x = 9
Result: 3
Explanation: Index 3 is the smallest index such that arr[3] >= x.
"""

def lower_bound(arr, x):
    left, right = 0, len(arr) - 1
    lower_bound_index = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] >= x:
            lower_bound_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return lower_bound_index

# Example usage:
arr = [1, 2, 2, 3]
x = 2
result = lower_bound(arr, x)
print(result)  # Output: 1

arr = [3, 5, 8, 15, 19]
x = 9
result = lower_bound(arr, x)
print(result)  # Output: 3
