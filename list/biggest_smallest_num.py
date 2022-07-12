# Create a python list object to store salary data of 5 employees, 
# then find the biggest salary and the smallest salary from the 
# list without using built in functions like max () and min ()

lst = [45,56,90,78,12,213,1,-43]
big=0
for i in lst:
    if i > big:
        big = i
print("Biggest Numeber: ",big)
small=lst[0]
for j in lst:
    if j < small:
        small = j
print("Smallest Number: ",small)
