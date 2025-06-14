class solution:
    def constLps(pat,lps):
        j = 0
        lps[0] = 0
        m = len(pat)
        i = 1
        while i < m:
            if pat[i] == pat[j]:
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
    def KMPSearch(pat,txt):
        n = len(txt)
        m = len(pat)
        lps = [0]*m
        lps = solution.constLps(pat, lps)
        i = 0
        j = 0
        res = []
        while i < n:
            if pat[j] == txt[i]:
                i += 1
                j += 1
                if j == m:
                    res.append(i-j)
                    j = lps[j-1]
            else:
                if j != 0:
                    j = lps[j-1]
                else:
                    i += 1
        return res
    
txt = "aabaacaadaabaaba"
pat = "aaba"
res = solution.KMPSearch(pat, txt)
for i in range(len(res)):
    print(res[i], end=" ")
# Output: 0 9 12
# Time Complexity: O(n + m) where n is the length of the text and m is the length of the pattern
# Space Complexity: O(m) for the lps array
# This code implements the Knuth-Morris-Pratt (KMP) algorithm for substring search.
# It preprocesses the pattern to create an lps (longest prefix suffix) array,
# which is used to skip unnecessary comparisons during the search.
# The KMP algorithm efficiently finds all occurrences of a pattern in a text.
# It returns the starting indices of all occurrences of the pattern in the text.
# The lps array helps in avoiding redundant comparisons by indicating how many characters can be skipped.





