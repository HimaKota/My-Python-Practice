# Find the factorial of a number

#using for loop
num=int(input("Enter a number "))
fact=1
for i in range(1,num+1):
    fact=fact*i
print("Using for loop: ",fact)

#using while loop
res=1
while num>=1:
    res=res*num
    num=num-1
print("Using While loop: ",res)

#Factorial Using Recursion
def fact(n):
    if(n==0):
        return 1
    return n * fact(n-1)
x=int(input("Enter numberUsing Recursion "))
result=fact(x)
print("Using Recursion",result)

