"""
Kadanes Algorithm : Maximum Subarray Sum in an Array
Problem Statement: Given an integer array arr, find the contiguous subarray (containing at least one number) which
has the largest sum and returns its sum and prints the subarray.
"""

"""
Example 1:

Input: arr = [-2,1,-3,4,-1,2,1,-5,4] 

Output: 6 

Explanation: [4,-1,2,1] has the largest sum = 6. 

Examples 2: 

Input: arr = [1] 

Output: 1 

Explanation: Array has only one element and which is giving positive sum of 1.
"""

#brute force approach

"""
def maxSubarraySum(arr):
    n = len(arr)
    max_sum = float('-inf')

    for i in range(n):
        for j in range(i, n):
            sum = 0
            for k in range(i, j+1):
                sum += arr[k]
            max_sum = max(max_sum, sum)

    return max_sum

# Example usage:
arr = [1, -2, 3, 4, -1, 2, 1, -5, 4]
max_sum = maxSubarraySum(arr)
print(max_sum)  # Output: 10

"""

#better-method 

def maxSubarraySum(arr):
    max_sum = float('-inf')
    current_sum = 0

    for i in range(len(arr)):
        current_sum += arr[i]
        max_sum = max(max_sum, current_sum)
        
        # If the current sum becomes negative, reset it to 0
        if current_sum < 0:
            current_sum = 0

    return max_sum

# Example usage:
arr = [1, -2, 3, 4, -1, 2, 1, -5, 4]
max_sum = maxSubarraySum(arr)
print(max_sum)  # Output: 10

#optimal-approach 

"""
def maxSubarraySum(arr):
    max_sum = float('-inf')
    current_sum = 0

    for i in range(len(arr)):
        current_sum += arr[i]
        if current_sum < 0:
            current_sum = 0
        max_sum = max(max_sum, current_sum)

    return max_sum

# Example usage:
arr = [1, -2, 3, 4, -1, 2, 1, -5, 4]
max_sum = maxSubarraySum(arr)
print(max_sum)  # Output: 9

"""