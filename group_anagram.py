"""
Given an array of strings, return all groups of strings that are anagrams. The strings in each group must be arranged in the order of their appearance in the original array. Refer to the sample case for clarification.

Examples:

Input: arr[] = ["act", "god", "cat", "dog", "tac"]
Output: [["act", "cat", "tac"], ["god", "dog"]]
Explanation: There are 2 groups of anagrams "god", "dog" make group 1. "act", "cat", "tac" make group 2.
Input: arr[] = ["no", "on", "is"]
Output: [["is"], ["no", "on"]]
Explanation: There are 2 groups of anagrams "is" makes group 1. "no", "on" make group 2.
Input: arr[] = ["listen", "silent", "enlist", "abc", "cab", "bac", "rat", "tar", "art"]
Output: [["abc", "cab", "bac"], ["listen", "silent", "enlist"], ["rat", "tar", "art"]]
Explanation: 
Group 1: "abc", "bac", and "cab" are anagrams.
Group 2: "listen", "silent", and "enlist" are anagrams.
Group 3: "rat", "tar", and "art" are anagrams.
"""

def groupAnagrams(arr):
    ans = {}
    for word in arr:
        count = [0] * 26
        for char in word:
            count[ord(char) - ord('a')] += 1
        ans[tuple(count)] = ans.get(tuple(count), []) + [word]
    return list(ans.values())

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

# time complexity: O(n*m) where n is the number of strings and m is the maximum length of a string
# space complexity: O(n*m) where n is the number of strings and m is the maximum length of a string
# because we are storing the count of each character in each string in a list of size 26 (26 letters in the English alphabet) 
