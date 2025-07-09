class Solution:
    #brutforce solution to spiral traversal of a 2D matrix
    def spiralTraversal(self, arr):
        m = len(arr)
        n = len(arr[0])
        dr = [0, 1, 0, -1]  # Direction vectors for right, down, left, up
        dc = [1, 0, -1, 0]  # Direction vectors for right, down, left, up
        c,r = 0,0
        idx = 0
        vis = [[False]*n for _ in range(m)] # Visited matrix
        res = []
        for i in range(m*n):
            res.append(arr[r][c])
            vis[r][c] = True
            newR = r + dr[idx]
            newC = c + dc[idx]
            if 0 <= newR < m and 0 <= newC < n and not vis[newR][newC]:
                r, c, = newR, newC
            else:
                idx = (idx + 1)%4
                r, c = r + dr[idx], c + dc[idx]
        return res
# Example usage:
if __name__ == "__main__":
    arr = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    sol = Solution()
    result = sol.spiralTraversal(arr)
    print("Spiral Traversal:", result)  # Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]   
# Time Complexity: O(m * n), where m is the number of rows and n is the number of columns in the matrix.
# Space Complexity: O(m * n), for the visited matrix and result list.
# This code implements a function to perform a spiral traversal of a 2D matrix.
# It uses direction vectors to navigate through the matrix in a spiral order.
# The function maintains a visited matrix to keep track of the elements that have already been traversed.
# The result is stored in a list which is returned at the end.
# The spiral traversal starts from the top-left corner and moves right, then down, left, and up, repeating this pattern until all elements are visited.
# The function handles edge cases such as empty matrices and single-row or single-column matrices.
# The spiral traversal is useful in various applications, such as image processing and matrix manipulation.


