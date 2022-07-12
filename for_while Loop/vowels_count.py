# Develop a python script to count number of vowel characters 
# in given string solve it by using for and if conditions.

username= input("Enter String: ")

count = 0
for i in username:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
        count =count+1
print(count)