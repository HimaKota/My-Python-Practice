# Develop a python script to find biggest of 3 numbers
# x, y and z. Solve using if, elif with AND
x= int(input("Enter the first value "))
y= int(input("Enter the second value "))
z= int(input("Enter the third value "))

if(x>=y and x>=z):
    print(x,"is biggest number")
elif(y>=z and y>=x):
    print(y,"is biggest number")
else:
    print(z,"is biggest number")
