"""

Input: N = 8394
Output: 4
Explanation: N has 4 digits

"""

#approach1
#using built-in methods like len() 
#len() method counts digits 


#approach2

n=int(input())
digit_counts = 0

while n!= 0 :
    n = n // 10
    digit_counts +=1

print("Number of digits: ",digit_counts)