# Write a Python program to read a random line from a file.

import random
def random_line(fname):
    lines = open(fname).read().splitlines()
    print(lines)
    print("-----------------------")
    return random.choice(lines)
print(random_line('File Handling\sample.txt'))
