# Write a python program to print the value of a given key
# Values	=	Router1		1.1.1.1	 	zframez		zframez
# Keys	=	(name)			(IP)		(username)		(pwd)

dict = {
        "name":"Router1",
        "IP":"1.1.1.1" ,
        "username":"Zframez",
        "pwd":"zframez"
        }
user_input = input("enter a key ")
if(user_input in dict):
    print(user_input,"contains the value:",dict[user_input])
else:
    print("Key Not found")
