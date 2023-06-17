"""

Input: N = 234
Output: 432
Explanation: The reverse of 234 is 432

"""

#approach1 
#using slice methods 
"""

 n =int(input())
 reversed = int(str(n[::-1]))
 print(reversed)
 """

 #appproach2

n=int(input())
reverse=0

while n > 0:
    digit = n%10 
    reverse = (reverse*10) + digit 
    n = n // 10
print("reverse number : ",reverse)
    