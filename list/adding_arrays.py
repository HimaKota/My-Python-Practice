# Write a code to add 2 arrays using for loop
from numpy import*

arr1 = array([5,10,15,20,30])
arr2 = array([55,16,1,280,60])
res=[]
for i in range(0,len(arr1)):
    add_arr =arr1[i]+arr2[i]
    res.append(add_arr)
print("Adding 2 arrays ",res)