def isAnagram(s1,s2):
    carCount = {}
    for ch in s1:
        carCount[ch] = carCount.get(ch, 0)+1
    for ch in s2:
        carCount[ch] = carCount.get(ch, 0)-1
    for ch in carCount.values():
        if ch != 0:
            return False
    #for ch in carCount:
    #    if carCount[ch] != 0:
    #        return False
    return True

s1 = "listen"
s2 = "silent"
print(isAnagram(s1, s2))
# Time Complexity: O(n)
# Space Complexity: O(n) for the character count dictionary
# This code checks if two strings are anagrams of each other.
# It counts the occurrences of each character in both strings and compares them.
# If the counts match for all characters, the strings are anagrams.
# If any character count does not match, it returns False.