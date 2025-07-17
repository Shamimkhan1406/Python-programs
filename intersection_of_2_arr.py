"""
Given two integer arrays a[] and b[], you have to find the intersection of the two arrays. Intersection of two arrays is said to be elements that are common in both arrays. The intersection should not have duplicate elements and the result should contain items in any order.

Note: The driver code will sort the resulting array in increasing order before printing.

Examples:

Input: a[] = [1, 2, 1, 3, 1], b[] = [3, 1, 3, 4, 1]
Output: [1, 3]
Explanation: 1 and 3 are the only common elements and we need to print only one occurrence of common elements.
Input: a[] = [1, 1, 1], b[] = [1, 1, 1, 1, 1]
Output: [1]
Explanation: 1 is the only common element present in both the arrays.
Input: a[] = [1, 2, 3], b[] = [4, 5, 6]
Output: []
Explanation: No common element in both the arrays.
"""

def intersection(a,b):
    # Convert the list a to sets to remove duplicates and improve lookup efficiency
    set_a = set(a)
    res = []
    # Iterate over the list b
    for i in b:
        # Check if the element is present in set_a
        if i in set_a:
            # If the element is present, add it to the result list
            res.append(i)
            # Remove the element from set_a to avoid duplicates
            set_a.remove(i)
    return res
# Test the function
print(intersection([1, 2, 1, 3, 1], [3, 1, 3, 4, 1]))  # Output: [1, 3]
print(intersection([1, 1, 1], [1, 1, 1, 1, 1]))  # Output: [1]

# time complexity: O(n + m) where n and m are the sizes of the input lists 
# space complexity: O(n) for the set and the result list 