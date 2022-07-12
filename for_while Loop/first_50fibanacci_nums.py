# Print first 50 Fibonacci numbers

x = int(input("enter value "))
a = 0
b = 1
if x==1:
    print(a) 
elif x<0:
    print("Invalid Number")
else:
    print(a,end=" ")
    print(b,end=" ")
    for i in range(2,x):
        c=a+b
        a=b
        b=c            
        print(c,end=" ") #prints the values for count of user enter input

