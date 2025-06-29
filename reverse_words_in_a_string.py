"""Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
"""

class Solution(object):
    def reverseWords(self, s):
        s = s.split()[::-1]
        s = ' '.join(s)
        return s
# Example usage
if __name__ == "__main__":
    s = "the sky is blue"
    sol = Solution()
    result = sol.reverseWords(s)
    
    print(f"The reversed string is: '{result}'")  # Output: "blue is sky the"
# Time Complexity: O(n) where n is the length of the string, as we traverse the string once to split it into words and then again to join them.
# Space Complexity: O(n) for storing the list of words created by splitting the string.
# This code implements a function to reverse the order of words in a given string.
# It first splits the string into words, reverses the list of words, and then joins them back into a single string with a single space separating each word.
# The function handles leading and trailing spaces by using the split method, which automatically removes them, and ensures that multiple spaces between words are reduced to a single space in the final output.
# The example usage demonstrates how to call the function and print the result.