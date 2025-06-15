class solution:
    def lpsArray(s):
        n = len(s)
        j = 0
        lps = [0]*n
        i =1
        while i < n:
            if s[i] == s[j]:
                j += 1
                lps[i] = j
                i += 1
            else:
                if j != 0:
                    j = lps[j-1]
                else:
                    lps[i] = 0
                    i += 1
        return lps
    def minCharToAddForPalindrome(s):
        rev = s[::-1]
        concat = s + "$" + rev
        lps = solution.lpsArray(concat)
        return len(s) - lps[-1]
s = "abad"
print(solution.minCharToAddForPalindrome(s))
# Time Complexity: O(n)
# Space Complexity: O(n)
# This code finds the minimum number of characters that need to be added to the beginning of a string
# to make it a palindrome. It uses the concept of the longest prefix suffix (LPS) array from the KMP algorithm.
# The LPS array is constructed for the concatenated string of the original string, a separator, and its reverse.
# The last value of the LPS array gives the length of the longest palindromic suffix,
# and the difference between the length of the original string and this value gives the number of characters to add.
# The function returns this number, which is the minimum number of characters needed to be added to the beginning of the string.