"""Rotate array by K elements

Problem Statement: Given an array of integers, rotating array of elements by k elements either left or right.
"""

"""
Example 1:
Input: N = 7, array[] = {1,2,3,4,5,6,7} , k=2 , right
Output: 6 7 1 2 3 4 5
Explanation: array is rotated to right by 2 position .

Example 2:
Input: N = 6, array[] = {3,7,8,9,10,11} , k=3 , left 
Output: 9 10 11 3 7 8
Explanation: Array is rotated to right by 3 position.

"""


def rotate_array(arr, k, direction):
    n = len(arr)
    
    # Adjust the rotation count if it's larger than the array size
    k = k % n
    
    if direction == "left":
        # Rotate the array left by K elements
        reverse_elements(arr, 0, k - 1)
        reverse_elements(arr, k, n - 1)
        reverse_elements(arr, 0, n - 1)
    elif direction == "right":
        # Rotate the array right by K elements
        reverse_elements(arr, 0, n - 1)
        reverse_elements(arr, 0, k - 1)
        reverse_elements(arr, k, n - 1)
    else:
        raise ValueError("Invalid direction. Use 'left' or 'right'.")
    
    return arr

def reverse_elements(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

array = [1, 2, 3, 4, 5]
k = 2
direction = "left"
rotated_array = rotate_array(array, k, direction)
print(rotated_array)
