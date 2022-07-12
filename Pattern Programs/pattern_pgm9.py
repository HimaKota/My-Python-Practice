# Develop a python script to numbers from in following formats using nested for loop
# * * * * *  
#  * * * *
#   * * *
#    * *
#     *

n = int(input("Enter the number of rows: "))  
m = (2 * n) - 2  
for i in range(n, -1,-1):  
    for j in range(m,0,-1):  
        print(end=" ")  
    m = m + 1  # decrementing m after each loop  
    for j in range(1, i + 1):  
        # printing full Triangle pyramid using stars  
        print("*", end=' ')  
    print(" ")  