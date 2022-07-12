# Write python to print the Transpose  of the matrix 
# i.e rows into colums and columns into rows

m1 = [[12,7],
    [4 ,5],
    [3 ,8]]

result = [[0,0,0],
         [0,0,0]]

for i in range(len(m1)):
    for j in range(len(m1[0])):
        result[j][i] = m1[i][j]
print("Transpose of matrix",result)