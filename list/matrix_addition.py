# Write a program to create matrix1 with 2x2 and matrix2 with 2x2
# and then perform the matrix additions.

m1 = [[10,20],[20,10],[30,20]]
m2 = [[40,50],[60,20],[10,80]]
res= [[0,0],[0,0],[0,0]]
for i in range(len(m1)):
    for j in range(len(m1[0])):
        res[i][j]=(m1[i][j]+m2[i][j])
print(res)