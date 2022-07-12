#  Write a Python program to read last n lines of a file

def file_read_from_tail(fname,last_nLines):   
    with open(fname) as f:
        last_line = f.readlines()[-last_nLines:]
        print('\n'.join(last_line))
L_lines=int(input("How many lines you want "))
print('-----The Last {} lines-----'.format(L_lines))
file_read_from_tail('File Handling\sample.txt',L_lines)
