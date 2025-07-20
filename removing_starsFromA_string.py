"""
You are given a string s, which contains stars *.

In one operation, you can:

Choose a star in s.
Remove the closest non-star character to its left, as well as remove the star itself.
Return the string after all stars have been removed.

Note:

The input will be generated such that the operation is always possible.
It can be shown that the resulting string will always be unique.
 

Example 1:

Input: s = "leet**cod*e"
Output: "lecoe"
Explanation: Performing the removals from left to right:
- The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
- The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
- The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
There are no more stars, so we return "lecoe".
Example 2:

Input: s = "erase*****"
Output: ""
Explanation: The entire string is removed, so we return an empty string.
"""

def removeStars(s):
    stack = []
    for char in s:
        if char == '*':
            if stack:
                stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)
# Example usage
if __name__ == "__main__":
    s = "leet**cod*e"
    result = removeStars(s)
    print(f"The string after removing stars is: {result}")  # Output: "lecoe"

# Time Complexity: O(n) where n is the length of the string, as we traverse the string once.
# Space Complexity: O(n) for the stack, which in the worst case can store all characters if there are no stars.
# This code implements a function to remove stars from a string by using a stack.
# It iterates through each character in the string, pushing non-star characters onto the stack.
# When a star is encountered, it pops the last character from the stack (if the stack is not empty).
# Finally, it joins the characters in the stack to form the resulting string without stars.
# The function returns the modified string after all stars have been removed.