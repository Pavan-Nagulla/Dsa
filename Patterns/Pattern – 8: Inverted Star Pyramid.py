"""

Input Format: N = 6
Result:     
***********
 *********
  *******
   ***** 
    ***    
     *
"""

n = 5

for i in range(n, 0, -1):
    print(" " * (n - i), end="")
    print("* " * i)
