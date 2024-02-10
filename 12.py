## Given a square matrix, turn it by 90 degrees in an anti-clockwise direction without using any extra space

def rotate_90_degrees(matrix):
    n = len(matrix)
    
    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse each row
    for i in range(n):
        matrix[i] = matrix[i][::-1]

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Original matrix:")
for row in matrix:
    print(row)

rotate_90_degrees(matrix)

print("\nMatrix rotated by 90 degrees anti-clockwise:")
for row in matrix:
    print(row)
