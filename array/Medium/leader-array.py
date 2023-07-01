"""
Leaders in an Array
Problem Statement: Given an array, print all the elements which are leaders. A Leader is an element that is greater than all of the elements on its right side in the array.
"""

"""

Example 1:
Input:
 arr = [4, 7, 1, 0]
Output:
 7 1 0
Explanation:
 Rightmost element is always a leader. 7 and 1 are greater than the elements in their right side.

Example 2:
Input:
 arr = [10, 22, 12, 3, 0, 6]
Output:
 22 12 6
Explanation:
 6 is a leader. In addition to that, 12 is greater than all the elements in its right side (3, 0, 6), also 22 is greater than 12, 3, 0, 6.
"""


#brute-force




def printLeadersBruteForce(arr, n):
    ans = []
  
    for i in range(n):
        leader = True

        # Checking whether arr[i] is greater than all 
        # the elements in its right side
        for j in range(i+1, n):
            if arr[j] > arr[i]:
                # If any element found is greater than current leader,
                # curr element is not the leader.
                leader = False
                break

        # Push all the leaders in ans array.
        if leader:
            ans.append(arr[i])

    return ans

# Main function
if __name__ == '__main__':
    # Array Initialization
    n = 6
    arr = [10, 22, 12, 3, 0, 6]

    ans = printLeadersBruteForce(arr, n)

    for i in range(len(ans)):
        print(ans[i], end=" ")

    print()

