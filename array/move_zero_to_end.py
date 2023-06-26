"""

Problem Statement: You are given an array of integers, your task is to move all the zeros in the array to the end of the array and move non-negative integers to the front by maintaining their order.
"""

"""

Example 1:
Input: 1 ,0 ,2 ,3 ,0 ,4 ,0 ,1
Output: 1 ,2 ,3 ,4 ,1 ,0 ,0 ,0
Explanation: All the zeros are moved to the end and non-negative integers are moved to front by maintaining order

Example 2:
Input: 1,2,0,1,0,4,0
Output: 1,2,1,4,0,0,0
Explanation: All the zeros are moved to the end and non-negative integers are moved to front by maintaining order
"""


def move_zeros_to_end(arr):
    left = 0
    right = 0
    
    # Move non-zeros to the front
    while right < len(arr):
        if arr[right] != 0:
            arr[left] = arr[right]
            left += 1
        right += 1
    
    # Fill the remaining elements with zeros
    while left < len(arr):
        arr[left] = 0
        left += 1
    
    return arr
