"""
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

 

Example 1:


Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]
Example 2:


Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]
"""

def equalPairs(grid):
    sum = 0
    dict = {}
    for row in grid:
        dict[tuple(row)] = dict.get(tuple(row), 0) + 1
    for col in zip(*grid):
        col = tuple(col)
        if col in dict:
            sum += dict[col]
    return sum
grid = [[3,2,1],[1,7,6],[2,7,7]]
print(equalPairs(grid))
grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
print(equalPairs(grid))

# time complexity: O(n^2)
# space complexity: O(n^2)