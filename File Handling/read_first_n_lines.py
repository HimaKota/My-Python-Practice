# Write a Python program to read first n lines of a file.

from itertools import islice
F_lines=int(input("How many lines you want "))
def file_read_from_head(fname, nlines):   
    print('-----The First {} lines-----'.format(F_lines))
    with open(fname) as f:
        for line in islice(f, nlines):
            print(line)
file_read_from_head('File Handling\sample.txt',F_lines)

#we can use this code also
def read_first_nlines(fname,first_nLines):   
    with open(fname) as f:
        last_line = f.readlines()[:first_nLines]
        print('\n'.join(last_line))
print('-----The Last {} lines-----'.format(F_lines))
read_first_nlines('File Handling\sample.txt',F_lines)

