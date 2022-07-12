# Develop a python script to numbers from in following formats using nested for loop
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
num=int(input("Enter a number "))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
