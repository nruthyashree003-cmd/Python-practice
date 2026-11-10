m, n = map(int, input("Enter rows and columns: ").split())

matrix = []

print("Enter matrix elements:")

for i in range(m):
    row = list(map(int, input().split()))
    matrix.append(row)

zero_rows = set()
zero_cols = set()

# Find positions containing zero
for i in range(m):
    for j in range(n):
        if matrix[i][j] == 0:
            zero_rows.add(i)
            zero_cols.add(j)

# Set complete rows and columns to zero
for i in range(m):
    for j in range(n):
        if i in zero_rows or j in zero_cols:
            matrix[i][j] = 0

print("Updated Matrix:")

for row in matrix:
    print(*row)