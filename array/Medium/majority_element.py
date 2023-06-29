"""
Find the Majority Element that occurs more than N/2 times
Problem Statement: Given an array of N integers, write a program to return an element that occurs more than N/2 times in the given array. You may consider that such an element always exists in the array.
"""

"""

Example 1:
Input Format: N = 3, nums[] = {3,2,3}
Result: 3
Explanation: When we just count the occurrences of each number and compare with half of the size of the array, you will get 3 for the above solution. 

Example 2:
Input Format:  N = 7, nums[] = {2,2,1,1,1,2,2}

Result: 2

Explanation: After counting the number of times each element appears and comparing it with half of array size, we get 2 as result.

Example 3:
Input Format:  N = 10, nums[] = {4,4,2,4,3,4,4,3,2,4}

Result: 4

"""

#bruteforce 

def findMajority(nums):
    majority = None
    n = len(nums)

    for num in nums:
        count = 0
        for i in range(n):
            if nums[i] == num:
                count += 1
        if count > n // 2:
            majority = num
            break

    return majority

# Example usage:
nums = [1, 2, 2, 2, 3, 2, 4, 2, 2]
majority_element = findMajority(nums)
print(majority_element)  # Output: 2


#better-approach 
#Using hashing-method 
"""

def findMajority(nums):
    freq = {}

    for num in nums:
        if num not in freq:
            freq[num] = 1
        else:
            freq[num] += 1

        if freq[num] > len(nums) // 2:
            return num

    return None

# Example usage:
nums = [1, 2, 2, 2, 3, 2, 4, 2, 2]
majority_element = findMajority(nums)
print(majority_element)  # Output: 2

"""

#optimal-method 
#moore voting algorithm
"""

"""