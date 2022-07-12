# Write a Python program to read a file line by line store it into a variable. 

def file_read(fname):
    with open (fname, "r") as myfile:   #we can use this one also txt = open(fname,"r")
        data=myfile.readlines()
        print(data)
file_read("File Handling\sample.txt")
