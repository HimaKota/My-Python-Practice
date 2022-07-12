# Write a Python program to remove duplicates from a list.

lst = [10,20,30,20,10,50,60,40,80,50,40]
for i in lst:   
    if lst.count(i) > 1:  
        lst.remove(i)
        # if unique_list.count(i) == 0:  # condition to check in unique list values 
        #     unique_list.append(i)
print("After removing duplicates final list is having",lst)
