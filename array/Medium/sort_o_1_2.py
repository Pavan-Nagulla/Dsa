"""

Sort an array of 0s, 1s and 2s
Problem Statement: Given an array consisting of only 0s, 1s, and 2s. Write a program to in-place sort the array without using inbuilt sort functions. ( Expected: Single pass-O(N) and constant space)

"""

#bruteforce
#sorting-built-in
"""
def sortColors(nums):
    nums.sort()

# Example usage:
nums = [2, 0, 2, 1, 1, 0]
sortColors(nums)
print(nums)  # Output: [0, 0, 1, 1, 2, 2]

"""

#better-approach 
"""intial 3 variables for count 0's and 1's , 2's """


def sortColors(nums):
    count_0, count_1, count_2 = 0, 0, 0

    # First traversal to count the occurrences
    for num in nums:
        if num == 0:
            count_0 += 1
        elif num == 1:
            count_1 += 1
        elif num == 2:
            count_2 += 1

    # Second traversal to overwrite the array
    index = 0
    for i in range(count_0):
        nums[index] = 0
        index += 1
    for i in range(count_1):
        nums[index] = 1
        index += 1
    for i in range(count_2):
        nums[index] = 2
        index += 1

# Example usage:
nums = [2, 0, 2, 1, 1, 0]
sortColors(nums)
print(nums)  # Output: [0, 0, 1, 1, 2, 2]


#optimal-solution 
#using dutch national flag algorithm

"""

def sortColors(nums):
    low = 0
    mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

# Example usage:
nums = [2, 0, 2, 1, 1, 0]
sortColors(nums)
print(nums)  # Output: [0, 0, 1, 1, 2, 2]

"""