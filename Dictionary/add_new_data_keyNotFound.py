# check whether the given key is present, if present 
# print the value , else add a new key and value
# Values	=	Router1		1.1.1.1	 	zframez		zframez
# Keys	=	(name)			(IP)		(username)		(pwd)

eth={
        'Name':'Router1',
        'IP':'1.1.1.1',
        'Username':'zframez',
        'Password':'pwd'
    }
user_input = input("Please Enter the key to get value ")
if(user_input in eth):
    print("The",user_input,"contains the value", eth[user_input])
else:
    print("Key Not found")
    new_val=input("Please Enter the new value for your entered key ")
    eth[user_input]=new_val
    print("After added new key and value:",eth)