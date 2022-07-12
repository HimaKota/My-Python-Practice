# Write a Python program to get the difference between the two lists.

list1 = [1, 2, 3, 4]
list2 = [1, 2 ,5]
#with out using built in function
li_dif = [i for i in list1 + list2 if i not in list1 or i not in list2]
print("with out using built in function",li_dif)

list_diff=list(set(list1) - set(list2)) + list(set(list2) - set(list1))
print("With using built in functions ",list_diff)