#Write a program to find the cube of a numbers using user input
 
# take input a number from user
num = int(input("Enter an any number: "))
 
# calculate cube using * operator
# cb = num*num*num
cb = num **3
# display result
print("Cube of \"{0}\" is {1} ".format(num, cb))