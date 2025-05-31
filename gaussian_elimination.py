def gaussian_elimination(A, b):
    """
    Solves the system of equations Ax = b using Gaussian Elimination.
    """
    # Your code here
    answer = []
    matrix = []

    # probably an elegant python way to do this but for now ill just use 2 loops
    for row in range(len(A)):
        new_row = []
        for item in A[row]:
            new_row.append(item)
        new_row.append(b[row])
        matrix.append(new_row)    
    # checking to see if the matrix was combined properly
    print(matrix)
    # the goal is to reduce a row so that a coeffient is equal to 1 and the rest are zero
    # also being mindful of where the coefficent is, [[0,1],[1,0]] -> [[1,0],[0,1]]
    # if a coefficent is equal to 1 check its location in the row


    return answer

# Example Usage:
A = [[2, 1], [5, 7]]
b = [11, 13]
print(gaussian_elimination(A, b))
