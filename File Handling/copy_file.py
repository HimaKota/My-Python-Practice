# Write a Python program to copy the contents of a file to another file

# using the shutil.copytree() function, we can copy a folder.
import shutil
#insteasd of copyfile() we can use copy() to copying a file
shutil.copyfile("File Handling\sample.txt", "File Handling\copy_sample.txt") 
