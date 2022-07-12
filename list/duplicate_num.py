# Write a program to find the duplicate numbers within the list

num=['Ok', 'Ok', 'is', 'Ok', 'test', 'this', 'is', 'a', 'test']
num1=[10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
duplicate_list =[]
for i in num:   
    if num.count(i)>1:  
        if duplicate_list.count(i) == 0:  # condition to check in duplicate list values 
            duplicate_list.append(i) 
print("The duplicate list having",duplicate_list)
print("----------")

