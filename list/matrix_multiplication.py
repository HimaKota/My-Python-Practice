# Write a program to find multiplication of 2 matrices

m1 = [[10,20],[20,10],[30,20]]
m2 = [[40,50],[60,20],[10,80]]
res= [[0,0],[0,0],[0,0]]
for i in range(len(m1)):
    for j in range(len(m1[0])):
        res[i][j]=(m1[i][j]*m2[i][j])
print(res)