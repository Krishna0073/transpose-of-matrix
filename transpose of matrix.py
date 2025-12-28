r = int(input("rows: "))
c = int(input("columns: "))
matrix = []
print("row wise elements:")
for i in range(r):
	li = list(map(int, input().split()))
	matrix.append(li)
print("original matrix:",matrix)
#write you code to find the transpose
transposed_matrix =[[i for i in range(r)]for j in range(c)]
for i in range(r):
	for j in range(c) :
		transposed_matrix[j][i] = matrix[i][j]
	
	
#print the transposed matrix
print("Transposed matrix:",transposed_matrix)
