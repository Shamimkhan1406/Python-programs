def mergeAlternately(word1,word2):
    merge = []
    i = 0
    while i < len(word1) or i < len(word2):
        if i < len(word1):
            merge.append(word1[i])
        if i < len(word2):
            merge.append(word2[i])
        i += 1
    return ''.join(merge)
# Example usage:
if __name__ == "__main__":
    word1 = "abc"
    word2 = "pqr"
    result = mergeAlternately(word1, word2)
    print("Merged String:", result)  # Output: "apbqcr"
# Time Complexity: O(n), where n is the length of the longer string.
# Space Complexity: O(n), for storing the merged string.
# This code implements a function to merge two strings alternately.
# It iterates through both strings, appending characters from each string in alternating order.
# If one string is longer, the remaining characters from that string are appended at the end.
# The function returns the merged string, which combines characters from both input strings in the specified order.
# The function handles cases where the strings are of different lengths, ensuring that all characters are included in the final result.
# The merged string is constructed using a list to efficiently handle character appending, and then joined into a single string before returning.
# The function can be used for various applications, such as interleaving characters from two strings or creating a combined string from two sources.
       