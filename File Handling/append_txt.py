# Write a Python program to append text to a file and display the text.

def file_read(fname):
        with open(fname, "a") as myfile:                
            myfile.write("Python Exercises\n")
            txt = open(fname)
        print(txt.read())
file_read("File Handling\samplefile.txt")
