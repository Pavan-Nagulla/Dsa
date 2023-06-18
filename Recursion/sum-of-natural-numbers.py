"""

Input: N=6
Output: 21
Explanation: 1+2+3+4+5+6=15

"""

def recursive(n):
    if n == 1:
        return 1 
    else:
        return n + recursive(n-1)

n=int(input())

sum = recursive(n)
print(sum)