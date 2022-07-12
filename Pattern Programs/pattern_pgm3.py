# Develop a python script to numbers from in following formats using nested for loop
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
num=int(input("Enter a number "))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()