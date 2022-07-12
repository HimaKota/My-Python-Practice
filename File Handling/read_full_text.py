# Write a Python program to read an entire text file.
def file_read(fname):
        txt = open(fname,"r")
        print(txt.read())

file_read('File Handling\sample.txt')
