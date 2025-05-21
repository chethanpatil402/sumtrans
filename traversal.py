rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter the elements row by row:")
matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        val = int(input(f"Element [{i}][{j}]: "))
        row.append(val)
    matrix.append(row)

print("\nOriginal Matrix:")
for row in matrix:
    print(row)

if rows == cols:
    diagonal_sum = 0
    for i in range(rows):
        diagonal_sum += matrix[i][i]
    print("Sum of main diagonal elements:", diagonal_sum)
else:
    print("Not a square matrix, so diagonal sum is not defined.")
transpose = []
for j in range(cols):
    row = []
    for i in range(rows):
        row.append(matrix[i][j])
    transpose.append(row)

print("\n Transpose of the Matrix:")
for row in transpose:
    print(row)