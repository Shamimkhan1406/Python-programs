def myAtoi(s: str)-> int:
    sign = 1
    res = 0
    idx = 0
    while idx < len(s) and s[idx] == ' ':
        idx += 1
    if idx < len(s) and (s[idx]== '+' or s[idx] == '-'):
        if s[idx]== '-':
            sign = -1
        idx += 1
    while idx < len(s) and '0' <= s[idx] <= '9':
        res = res*10 + int(s[idx])
        #(ord(s[idx]) - ord('0')
        if res > (2**31-1):
            return sign * (2**31 - 1) if sign == 1 else -2**31
        idx += 1
    return res * sign

s = " -0012g4"
print(myAtoi(s))
# Time Complexity: O(n), where n is the length of the string s.
# Space Complexity: O(1), as we are using only a few extra variables.
# This code implements a function to convert a string to an integer, handling leading spaces, signs, and invalid characters.
# It also ensures that the result is within the 32-bit signed integer range.
# The function iterates through the string, skipping leading spaces, checking for a sign, and then converting the numeric characters to an integer.