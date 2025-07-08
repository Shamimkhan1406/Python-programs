class solution:
    #brute force approach
    def rotateMatrixBy90(self, matrix):
        n = len(matrix)
        # Create a new matrix to store the rotated result
        rotated_mat = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                # Place the element in the new position
                rotated_mat[n-1-j][i] = matrix[i][j]
        for i in range(n):
            for j in range(n):
                # Update the original matrix with the rotated values
                matrix[i][j] = rotated_mat[i][j]
        return matrix
    

    #optimal approach
    def rotateMatrixBy90Optimal(self, matrix):
        n = len(matrix)
        #reverse each row
        for row in matrix:
            row.reverse()
        #  transpose the matrix
        for i in range(n):
            for j in range(i + 1,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix
# Example usage
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    sol = solution()
    rotated_matrix = sol.rotateMatrixBy90(matrix)
    
    print("Rotated Matrix by 90 degrees:")
    for row in rotated_matrix:
        print(row)
    # Using the optimal approach
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    rotated_matrix_optimal = sol.rotateMatrixBy90Optimal(matrix)
    print("Rotated Matrix by 90 degrees (Optimal):")
    for row in rotated_matrix_optimal:
        print(row)



# Time Complexity: O(n^2) for both approaches as we are iterating through the matrix elements.
# Space Complexity: O(n^2) for the brute force approach due to the creation of a new matrix, while the optimal approach uses O(1) additional space as it modifies the matrix in place.
# This code implements a function to rotate a square matrix by 90 degrees clockwise.
# The brute force approach creates a new matrix to store the rotated result, while the optimal approach modifies the matrix in place by first reversing each row and then transposing the matrix.
# The example usage demonstrates how to call the function and print the rotated matrix.
# The implementation ensures that the rotation is efficient and suitable for square matrices, making it a common approach in problems involving matrix manipulation.