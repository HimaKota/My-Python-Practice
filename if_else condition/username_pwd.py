# Write a python script to take username and password as inputs and then 
# check if the username=='trishana' and password=='12345' if both are correct 
# print result as "Logged in" otherwise print result as "Invalid user / password "

username= input("Enter Username: ")
password= input("Enter Password: ")

if(username=='trishana' and password=='12345'):
    print("Logged in")
else:
    print("Invalid User / password")