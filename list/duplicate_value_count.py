# script to find duplicates numbers within the list and 
# print number of times number is appearing

num=[10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
duplicate_list =[]
for i in num:   
    if num.count(i)>1:  
        if duplicate_list.count(i) == 0:  # condition to check in duplicate list values 
            duplicate_list.append(i) 
print("The duplicate list having",duplicate_list)
print("----------")
#Finding the no.of times number is repeating
for no_count in duplicate_list:
    duplicate_count=num.count(no_count)
    print("The",no_count,"is appreared in",duplicate_count)