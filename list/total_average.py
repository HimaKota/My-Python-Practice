#Create a python list object to store salary of 5 employees, 
# then calculate and print the total and average of salary list.
lst = []
lst_len = int(input("Enter the length of the list "))
for i in range(1,lst_len+1):
    lst_val = int(input("enter a value "))
    lst.append(lst_val)
print("Final list is:",lst)

total_sal=0
count=0
for i in lst:
    total_sal = total_sal + i
    count = count + 1
    avg_sal = total_sal / count
print("The total of the employee salaries  ",total_sal)
print("The average of the employee salaries ",avg_sal)


