"""
Input: n = 36
Output: 1 2 3 4 6 9 12 18 36
Explanation: All the divisors of 36 are printed.

Example 2:
Input: n = 97
Output: 1 97
Explanation: Since 97 is a prime number, only 1 and 97 are printed.

"""

n=int(input())

for i in range(1,n+1):
    if n % i ==0:
        print(i,end=" ")
print()