#Remove Duplicates in-place from Sorted Array
"""

Problem Statement: Given an integer array sorted in non-decreasing order, remove the duplicates in place such that each unique element appears only once. The relative order of the elements should be kept the same.

If there are k elements after removing the duplicates, then the first k elements of the array should hold the final result. It does not matter what you leave beyond the first k elements.
"""


"""
Example 1: 

Input: arr[1,1,2,2,2,3,3]

Output: arr[1,2,3,_,_,_,_]

Explanation: Total number of unique elements are 3, i.e[1,2,3] and Therefore return 3 after assigning [1,2,3] in the beginning of the array.

Example 2: 

Input: arr[1,1,1,2,2,3,3,3,3,4,4]

Output: arr[1,2,3,4,_,_,_,_,_,_,_]

Explanation: Total number of unique elements are 4, i.e[1,2,3,4] and Therefore return 4 after assigning [1,2,3,4] in the beginning of the array.

"""

def remove_duplicates(nums):
    if len(nums) == 0:
        return 0

    # Initialize the pointer to track the position to update
    pos = 1

    # Iterate over the array starting from the second element
    for i in range(1, len(nums)):
        # If the current element is different from the previous element
        if nums[i] != nums[i - 1]:
            # Update the value at the position pointer and move it forward
            nums[pos] = nums[i]
            pos += 1

    # Return the length of the new array without duplicates
    return pos

# Example usage:
nums = [1, 1, 2, 2, 3, 4, 5, 5, 5, 6]
length = remove_duplicates(nums)

# Print the modified array without duplicates
for i in range(length):
    print(nums[i])
