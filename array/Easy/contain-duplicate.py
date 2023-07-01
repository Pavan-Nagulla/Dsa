"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 
"""

def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

nums = [1, 2, 3, 4, 5]
result = containsDuplicate(nums)
print(result)  # False

nums = [1, 2, 3, 2, 5]
result = containsDuplicate(nums)
print(result)  # True
