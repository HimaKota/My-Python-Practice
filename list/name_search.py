# Write a program to create a list of names and then search the 
# particular is present within the list or not

lst = ['hima','kishore','satya','aswi','harika','arya']
search_name = input("Enter name ")

if search_name in lst:
    print("Name Found")
else:
    print("Not Found")