"""

Example 1:
Input: array[] = {10,5,10,15,10,5};
Output: 10 15
Explanation: The frequency of 10 is 3, i.e. the highest and the frequency of 15 is 1 i.e. the lowest.

Example 2:

Input: array[] = {2,2,3,4,4,2};
Output: 2 3
Explanation: The frequency of 2 is 3, i.e. the highest and the frequency of 3 is 1 i.e. the lowest.

"""

def find_highest_lowest_frequency(arr):
    frequency = {}

    for element in arr:
        if element in frequency:
            frequency[element] += 1
        else:
            frequency[element] = 1

    highest_frequency = max(frequency.values())
    lowest_frequency = min(frequency.values())

    highest_frequency_elements = [key for key, value in frequency.items() if value == highest_frequency]
    lowest_frequency_elements = [key for key, value in frequency.items() if value == lowest_frequency]

    return highest_frequency_elements, lowest_frequency_elements

# Example usage
my_array = [1, 2, 3, 4, 2, 3, 1, 2, 1]
highest_frequency_elements, lowest_frequency_elements = find_highest_lowest_frequency(my_array)

print("Highest frequency elements:", highest_frequency_elements)
print("Lowest frequency elements:", lowest_frequency_elements)
