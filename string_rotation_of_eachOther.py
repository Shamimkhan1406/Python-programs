#def stringRotationOrNot(s1,s2):
#    conct = s1 + s2
#    if s2 in conct:
#        return True
#    return False

class StringRotationChecker:
    def lpsArray(self, pat):
        n = len(pat)
        lps = [0] * n
        j = 0
        i = 1
        while i < n:
            if pat[i] == pat[j]:
                j+=1
                lps[i] = j
                i += 1
            else:
                if j!=0:
                    j =lps[j-1]
                else:
                    lps[i] = 0
                    i += 1
        return lps
    def isRotation(self, s1, s2):
        txt = s1 + s1
        pat = s2
        lps = self.lpsArray(pat)
        n = len(txt)
        m = len(pat)
        i = 0
        j = 0
        while i < n:
            if txt[i] == pat[j]:
                i += 1
                j += 1
                if j == m:
                    return True
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return False
s1 = "waterbottle"
s2 = "erbottlewat"
checker = StringRotationChecker()
print(checker.isRotation(s1, s2))  # Output: True
# Time Complexity: O(n + m) where n is the length of the concatenated string and m is the length of the pattern
# Space Complexity: O(m) for the lps array
# This code checks if one string is a rotation of another using the KMP algorithm.
# It constructs the longest prefix suffix (LPS) array for the pattern and uses it to efficiently search for the pattern in the concatenated string.
# If the pattern is found, it returns True; otherwise, it returns False.
# The LPS array helps in skipping unnecessary comparisons during the search.
# This approach is efficient and works in linear time, making it suitable for checking string rotations.