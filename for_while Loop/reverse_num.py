# Develop python script to print the numbers in reverse order

num=int(input("Enter a number "))

while num!=0:
    rem = num % 10   
    num = num // 10
    print(rem,end="")