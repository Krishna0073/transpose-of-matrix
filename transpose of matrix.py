r = int(input("Rows: "))
c = int(input("Columns: "))

matrix = []

print("Enter row-wise elements:")
for i in range(r):
    row = list(map(int, input().split()))
    matrix.append(row)

print("\nOriginal Matrix:")
for row in matrix:
    print(row)

transposed_matrix = [[0 for j in range(r)] for i in range(c)]

for i in range(r):
    for j in range(c):
        transposed_matrix[j][i] = matrix[i][j]

print("\nTransposed Matrix:")
for row in transposed_matrix:
    print(row)

if r == c:
    diag_sum = 0
    for i in range(r):
        diag_sum += matrix[i][i]
    print("Main Diagonal Sum:", diag_sum)

if r == c:
    symmetric = True
    for i in range(r):
        for j in range(c):
            if matrix[i][j] != matrix[j][i]:
                symmetric = False
                break
        if not symmetric:
            break

    if symmetric:
        print("Matrix is Symmetric")
    else:
        print("Matrix is Not Symmetric")

even = 0
odd = 0

for i in range(r):
    for j in range(c):
        if matrix[i][j] % 2 == 0:
            even += 1
        else:
            odd += 1

print("Even Elements:", even)
print("Odd Elements:", odd)

for i in range(r):
    mx = matrix[i][0]
    for j in range(c):
        if matrix[i][j] > mx:
            mx = matrix[i][j]
    print(f"Maximum in Row {i+1}:", mx)

for j in range(c):
    mn = matrix[0][j]
    for i in range(r):
        if matrix[i][j] < mn:
            mn = matrix[i][j]
    print(f"Minimum in Column {j+1}:", mn)

key = int(input("\nEnter element to search: "))
found = False

for i in range(r):
    for j in range(c):
        if matrix[i][j] == key:
            print(f"Element found at Row {i+1}, Column {j+1}")
            found = True

if not found:
    print("Element not found")

k = int(input("\nEnter scalar value: "))

print("Matrix after Scalar Multiplication:")
for i in range(r):
    for j in range(c):
        print(matrix[i][j] * k, end=" ")
    print()

if r == c:
    identity = True

    for i in range(r):
        for j in range(c):
            if i == j and matrix[i][j] != 1:
                identity = False
            elif i != j and matrix[i][j] != 0:
                identity = False

    if identity:
        print("Identity Matrix")
    else:
        print("Not an Identity Matrix")
