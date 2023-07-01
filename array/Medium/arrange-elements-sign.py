"""

Rearrange Array Elements by Sign
Variety-1

Problem Statement:

Theres an array A of size N with an equal number of positive and negative elements. Without altering the relative order of positive and negative elements, you must return an array of alternately positive and negative values.

Note: Start the array with positive elements.


"""

"""
Input:
arr[] = {1,2,-4,-5}, N = 4
Output:
1 -4 2 -5

Explanation: 

Positive elements = 1,2
Negative elements = -4,-5
To maintain relative ordering, 1 must occur before 2, and -4 must occur before -5.

Example 2:
Input:
arr[] = {1,2,-3,-1,-2,-3}, N = 6
Output:
1 -3 2 -1 3 -2
Explanation: 

Positive elements = 1,2,3
Negative elements = -3,-1,-2
To maintain relative ordering, 1 must occur before 2, and 2 must occur before 3.
Also, -3 should come before -1, and -1 should come before -2.

"""

#bruteforce

def rearrange_by_sign(A):
    # Define 2 lists, one for storing positive and other for negative elements of the array.
    pos = []
    neg = []
  
    # Segregate the array into positives and negatives.
    for i in range(len(A)):
        if A[i] > 0:
            pos.append(A[i])
        else:
            neg.append(A[i])
  
    # Positives on even indices, negatives on odd.
    for i in range(len(pos)):
        A[2 * i] = pos[i]
    for i in range(len(neg)):
        A[2 * i + 1] = neg[i]
  
    return A

# Array Initialisation.
A = [1, 2, -4, -5]
ans = rearrange_by_sign(A)

for i in range(len(ans)):
    print(ans[i], end=" ")



#optimal-solution 
"""
from typing import List

def RearrangebySign(A: List[int]) -> List[int]:
    n = len(A)
    
    # Define array for storing the ans separately.
    ans = [0] * n
    
    # positive elements start from 0 and negative from 1.
    posIndex, negIndex = 0, 1
    for i in range(n):
        
        # Fill negative elements in odd indices and inc by 2.
        if A[i] < 0:
            ans[negIndex] = A[i]
            negIndex += 2
        
        # Fill positive elements in even indices and inc by 2.
        else:
            ans[posIndex] = A[i]
            posIndex += 2
    
    return ans
    
# Test the function
A = [1,2,-4,-5]
ans = RearrangebySign(A)
print(ans)

"""