# 1st word of each line in a txt file?
f=open("File Handling\sample.txt","r")
for line in f:
    words=line.split()
    print(words[0])