"""

Input: num1 = 4, num2 = 8
Output: 4
Explanation: Since 4 is the greatest number which divides both num1 and num2.

Example 2:
Input: num1 = 3, num2 = 6
Output: 3
Explanation: Since 3 is the greatest number which divides both num1 and num2.

"""
"""
GCD stands for the Greatest Common Divisor. It is the largest positive integer that divides two or more numbers without leaving a remainder. The GCD is often used in various mathematical computations and algorithms.

Here are a few examples of finding the GCD of two numbers:

Example 1:
Numbers: 12 and 18

To find the GCD of 12 and 18, we can use the Euclidean algorithm:

Divide 18 by 12: 18 ÷ 12 = 1 remainder 6
Divide 12 by 6: 12 ÷ 6 = 2 remainder 0
Since the remainder is now 0, the GCD is the last non-zero remainder, which is 6.

Therefore, the GCD of 12 and 18 is 6.

Example 2:
Numbers: 24 and 36

Using the Euclidean algorithm:

Divide 36 by 24: 36 ÷ 24 = 1 remainder 12
Divide 24 by 12: 24 ÷ 12 = 2 remainder 0
Again, the remainder is 0, so the GCD is the last non-zero remainder, which is 12.

Hence, the GCD of 24 and 36 is 12.

In both examples, we can see that the GCD represents the largest number that divides both numbers without leaving a remainder.

"""

def gcd(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1

num1 = 24
num2 = 36

gcd_result = gcd(num1, num2)
print("GCD:", gcd_result)
