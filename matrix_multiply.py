def matrix_multiply(A, B):
    """
    Multiplies two matrices A and B and returns the resulting matrix.
    Assumes dimensions are valid (A columns == B rows).
    """
    AB = []
    # first row of the new matrix
    for i in range(len(A)):
        new_row = []
        
        # Loop through columns of B
        for j in range(len(B[0])):
            total = 0
            
            # Dot product of row of A and column of B
            for k in range(len(A[0])):
                total += A[i][k] * B[k][j]
                
            new_row.append(total)
        
        AB.append(new_row)




    return AB

# Example Usage:
A = [[1, 2], [3, 4]]
B = [[2, 0], [1, 2]]

print(matrix_multiply(A, B))
