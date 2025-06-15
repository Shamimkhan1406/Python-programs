def hIndex(citations):
    citations.sort(reverse=True)
    idx = 0
    while idx < len(citations) and citations[idx] > idx:
        idx += 1
    return idx
citations = [3, 0, 6, 1, 5]
print(hIndex(citations))  # Output: 3
# Explanation:
# The sorted citations are [6, 5, 3, 1, 0].
# The h-index is 3 because there are 3 papers with at least 3 citations.
# The first paper has 6 citations, the second has 5, and the third has 3.
# Time Complexity: O(n log n) due to sorting
# Space Complexity: O(1) since we are sorting in place
