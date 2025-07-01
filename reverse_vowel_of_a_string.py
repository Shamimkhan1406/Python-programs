"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"


"""
def reverseVowel(self,s):
    left = 0
    right = len(s) - 1
    s = list(s)
    vowels = set('aeiouAEIOU')
    while left<right:
        if s[left] not in vowels:
            left += 1
        elif s[right] not in vowels:
            right -= 1
        else:
            s[left],s[right] = s[right],s[left]
            left += 1
            right -= 1
    return ''.join(s)
# Example usage
if __name__ == "__main__":
    s = "hello"
    result = reverseVowel(None, s)
    
    print(f"The string after reversing vowels is: {result}")  # Output: "holle"
# Time Complexity: O(n) where n is the length of the string, as we traverse the string once.
# Space Complexity: O(n) for converting the string to a list, but the final result is returned as a string.
# This code implements a function to reverse the vowels in a given string.
# It uses two pointers, one starting from the beginning and the other from the end of the string.
# The function checks if the characters at these pointers are vowels and swaps them if both are vowels.
# The process continues until the two pointers meet, ensuring that all vowels in the string are reversed.
# The function returns the modified string with vowels reversed.