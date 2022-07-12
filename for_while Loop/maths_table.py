# Develop a python script to accept a number as input then print the following maths table
# 5x1=5
# 5x2=10
# 5x3=15
# .....
# .....
# 5x10=50

num=int(input("Enter a number "))
print(num,"table is")
for i in range(1,11):
    print(num,"x",i," = ",num*i)