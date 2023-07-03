"""
Problem statement: You are given a sorted array of integers and a target, your task is to search for the target in the given array. Assume the given array does not contain any duplicate numbers.

Lets say the given array is = {3, 4, 6, 7, 9, 12, 16, 17} and target = 6.


"""

def search(nums, target):
        low = 0 
        high = len(nums) - 1 
        while low <= high :
            mid = (low + high) // 2 
            if nums[mid] == target :
                return mid 
            elif target > nums[mid]:
                low = mid + 1
            else :
                high = mid - 1
        return -1 

arr = [1,2,3,4,5,6]
target = 5 
index = search(arr,target)
if index == -1 :
     print("element not found")
else:
     print("Element index at :",index)