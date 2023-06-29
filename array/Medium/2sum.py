"""
Two Sum : Check if a pair with given sum exists in Array
Problem Statement: Given an array of integers arr[] and an integer target.

1st variant: Return YES if there exist two numbers such that their sum is equal to the target. Otherwise, return NO.

2nd variant: Return indices of the two numbers such that their sum is equal to the target. Otherwise, we will return {-1, -1}.

Note: You are not allowed to use the same element twice. Example: If the target is equal to 6 and num[1] = 3, then nums[1] + nums[1] = target is not a solution.
"""

#bruteforce

def twoSumExists(arr, target):
    num_set = set()
    for num in arr:
        complement = target - num
        if complement in num_set:
            return "YES"
        num_set.add(num)
    return "NO"

# Example usage:
nums = [2, 4, 7, 11, 15]
target = 9
print(twoSumExists(nums, target))  # Output: YES
