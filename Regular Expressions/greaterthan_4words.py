# Write a Python program to find all words which are at least 4 characters long in a string.

import re

from numpy import character
text = 'The quick brown fox jumps over the lazy dog.'

#greaterthan 4 character words
print("4 character long word ",re.findall(r"\b\w{4,}\b", text))

#5 character words
print("5 character long word ",re.findall(r"\b\w{5}\b", text))