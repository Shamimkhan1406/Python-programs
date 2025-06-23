
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
# This code calculates the h-index of a researcher based on their citation counts.
# The h-index is defined as the maximum value h such that the researcher has at least h papers with at least h citations each.
# The function sorts the citation counts in descending order and iterates through the sorted list to find the h-index.
# It returns the h-index value, which represents the researcher's productivity and impact based on their citations.
