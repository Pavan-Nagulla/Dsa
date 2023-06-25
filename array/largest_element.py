"""
Example 1:
Input: arr[] = {2,5,1,3,0};
Output: 5
Explanation: 5 is the largest element in the array. 

Example2: 
Input: arr[] = {8,10,5,7,9};
Output: 10
Explanation: 10 is the largest element in the array. 
"""

def largest_arr(arr):
    arr.sort()
    return arr[-1]

array1 = [1, 5, 9, 4, 2]
print(largest_arr(array1))
