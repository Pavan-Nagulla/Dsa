"""

Example 1:
Input: Str =  “ABCDCBA”
Output: Palindrome
Explanation: String when reversed is the same as string.

Example 2:
Input: Str = “TAKE U FORWARD”
Output: Not Palindrome
Explanation: String when reversed is not the same as string.


"""

def is_palindrome(string):
    if len(string) <= 1:
        return True
    elif string[0] != string[-1]:
        return False
    else:
        return is_palindrome(string[1:-1])


# Test the function
string1 = "radar"
print(f"Is '{string1}' a palindrome? {is_palindrome(string1)}")

string2 = "hello"
print(f"Is '{string2}' a palindrome? {is_palindrome(string2)}")
