"""
Linear Search
Problem Statement: Given an array, and an element num the task is to find if num is present in the given array or not. If present print the index of the element or print -1.
"""

def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i 
    return -1 

array1= [1,4,5,6,2]
target = 6 
index_array = linear_search(array1,target)
print(index_array)