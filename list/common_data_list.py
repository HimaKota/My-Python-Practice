# Write a Python function that takes two lists and returns 
# True if they have at least one common member.

def common_data(lst1,lst2):
    result = False
    for x in lst1:
        for y in lst2:
            if x==y:
                result =True
                return result

print(common_data([1,2,3,4,5], [3,5,6,7,8,9]))