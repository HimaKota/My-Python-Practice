# Develop a python script to numbers from in following formats using nested for loop
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1
rows = 5
# reverse for loop from 5 to 0
for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print('\r')