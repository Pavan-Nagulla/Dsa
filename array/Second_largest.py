"""
Example 1:
Input: [1,2,4,7,7,5]
Output: Second Smallest : 2
	Second Largest : 5
Explanation: The elements are as follows 1,2,3,5,7,7 and hence second largest of these is 5 and second smallest is 2

Example 2:
Input: [1]
Output: Second Smallest : -1
	Second Largest : -1
Explanation: Since there is only one element in the array, it is the largest and smallest element present in the array. There is no second largest or second smallest element present.
"""

def find_second_smallest_largest(arr):
    if len(arr) < 2:
        return None

    # Initialize the smallest and second smallest variables
    smallest = second_smallest = float('inf')

    # Initialize the largest and second largest variables
    largest = second_largest = float('-inf')

    for num in arr:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num

        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    return second_smallest, second_largest


# Example usage:
array = [9, 2, 12, 5, 7, 3]
result = find_second_smallest_largest(array)
print("Second Smallest:", result[0])
print("Second Largest:", result[1])
