n = int(input("Enter matrix size: "))

matrix = []

print("Enter matrix elements:")
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Step 1: Transpose the matrix
for i in range(n):
    for j in range(i + 1, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

# Step 2: Reverse each row
for i in range(n):
    matrix[i].reverse()

# Print rotated matrix
print("Rotated matrix:")
for row in matrix:
    print(*row)