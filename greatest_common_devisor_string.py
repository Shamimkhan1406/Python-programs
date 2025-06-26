class Solution:
    def gcd(self, a, b):
        while b:
            a, b = b, a%b
        return a
    def gcdOfStrings(self,str1,str2):
        if str1 + str2 != str2 + str1:
            return ""
        return str1[:self.gcd(len(str1),len(str2))]

# Example usage:
str1 = "ABCABC"
str2 = "ABC"
sol = Solution()
result = sol.gcdOfStrings(str1, str2)
print("GCD of Strings:", result)  # Output: "ABC"
# Time Complexity: O(n + m), where n and m are the lengths of str1 and str2, respectively.
# Space Complexity: O(1), as we are using a constant amount of space.
# This code implements a function to find the greatest common divisor (GCD) of two strings.
# It checks if the concatenation of the two strings in both orders is equal.
# If they are equal, it calculates the GCD of their lengths and returns the substring of str1 up to that length.
# If the concatenated strings are not equal, it returns an empty string.
# The function uses the Euclidean algorithm to compute the GCD of the lengths of the two strings.
# The GCD of strings is defined as the longest string that can divide both input strings without leaving a remainder.