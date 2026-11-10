m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

matrix = []

for i in range(m):
    row = list(map(int, input().split()))
    matrix.append(row)

result = []

top = 0
bottom = m - 1
left = 0
right = n - 1

while top <= bottom and left <= right:

    # Left to right
    for i in range(left, right + 1):
        result.append(matrix[top][i])
    top += 1

    # Top to bottom
    for i in range(top, bottom + 1):
        result.append(matrix[i][right])
    right -= 1

    # Right to left
    if top <= bottom:
        for i in range(right, left - 1, -1):
            result.append(matrix[bottom][i])
        bottom -= 1

    # Bottom to top
    if left <= right:
        for i in range(bottom, top - 1, -1):
            result.append(matrix[i][left])
        left += 1

print("Spiral order:", result)