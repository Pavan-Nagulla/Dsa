"""

Example 1:
Input: arr[] = {10,5,10,15,10,5};
Output: 10  3
	 5  2
        15  1
Explanation: 10 occurs 3 times in the array
	      5 occurs 2 times in the array
              15 occurs 1 time in the array

Example2: 
Input: arr[] = {2,2,3,4,4,2};
Output: 2  3
	3  1
        4  2
Explanation: 2 occurs 3 times in the array
	     3 occurs 1 time in the array
             4 occurs 2 time in the array

             """

def count_frequency(arr):
    frequency = {}
    
    for element in arr:
        if element in frequency:
            frequency[element] += 1
        else:
            frequency[element] = 1
    
    return frequency

# Example usage
my_array = [1, 2, 3, 4, 2, 3, 1, 2, 1]
frequency_dict = count_frequency(my_array)
print(frequency_dict)
