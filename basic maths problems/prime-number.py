"""

Input: N = 3
Output: Prime
Explanation: 3 is a prime number

Example 2:
Input: N = 26
Output: Non-Prime
Explanation: 26 is not prime

"""
import math

def is_prime(number):
    if number < 2:
        return False

    # Check divisibility from 2 to the square root of the number
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True

number = 17

if is_prime(number):
    print("Prime Number")
else:
    print("Not a Prime Number")
