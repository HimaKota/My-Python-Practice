# Write a Python program to count the number of strings where the string length is 
# 2 or more and the first and last character are same from a given list of strings.
# Sample List : ['abc', 'xyz', 'aba', '1221']

lst = ['abc', 'xyz', 'abda', '1221']
lst1=[]
count = 0
for i in lst:
    if(len(i)>=2 and i[0]==i[-1]):
       count =count+1
       lst1.append(i)
print("Matched Words list",lst1)
print("Matched Words Count",count)
