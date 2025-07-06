class Solution:
    def binarySearch(self,mat,k):
        lo = 0
        hi = len(mat)-1
        while lo <= hi:
            mid = lo+(hi-lo)//2
            if mat[mid]==k:
                return True
            elif mat[mid]>k:
                hi = mid-1
            elif mat[mid]<k:
                lo = mid+1
        return False
    
    def searchInMatrix(self,mat,k):
        n = len(mat)
        for i in range(n):
            if self.binarySearch(mat[i], k):
                return True
        return False
    
    # Problem Description:
    # Given a row-wise sorted matrix 'mat' and an integer 'k', determine if 'k' exists in the matrix.
    # Each row of the matrix is sorted in non-decreasing order.

    # Time Complexity: O(n * log m), where n is the number of rows and m is the number of columns.
    # Space Complexity: O(1), as no extra space is used apart from variables.

# Example usage
if __name__ == "__main__":
    mat = [
        [1, 4, 7, 11],
        [2, 5, 8, 12],
        [3, 6, 9, 16],
        [10, 13, 14, 17]
    ]
    k = 111
    sol = Solution()
    result = sol.searchInMatrix(mat, k)
    print("Element found." if result else "Element not found.")