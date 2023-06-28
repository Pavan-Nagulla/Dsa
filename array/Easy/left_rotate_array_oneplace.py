"""
Example 1:
Input: N = 5, array[] = {1,2,3,4,5}
Output: 2,3,4,5,1
Explanation: 
Since all the elements in array will be shifted 
toward left by one so ‘2’ will now become the 
first index and and ‘1’ which was present at 
first index will be shifted at last.


Example 2:
Input: N = 1, array[] = {3}
Output: 3
Explanation: Here only element is present and so 
the element at first index will be shifted to 
last index which is also by the way the first index.
"""

def left_rotate_array(arr):
    # Store the first element in a variable
    first_element = arr[0]
    
    # Shift each element one position to the left
    for i in range(len(arr) - 1):
        arr[i] = arr[i + 1]
    
    # Assign the first element to the last position
    arr[-1] = first_element
    
    return arr

array = [1, 2, 3, 4, 5]
rotated_array = left_rotate_array(array)
print(rotated_array)
