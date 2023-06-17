"""
Input: N = 123
Output: Not Palindrome Number
Explanation: 123 read backwards is 321.Since these are two different numbers 123 is not a palindrome.

Example 2:
Input: N =  121 
Output: Palindrome Number
Explanation: 121 read backwards as 121.Since these are two same numbers 121 is a palindrome.

"""

number = 12321

# Convert the number to a string for easier comparison
number_str = str(number)

# Reverse the number
reversed_number = int(number_str[::-1])

# Check if the original number is equal to the reversed number
if number == reversed_number:
    print("Palindrome")
else:
    print("Not a Palindrome")
