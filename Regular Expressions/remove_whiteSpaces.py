# Write a Python program to remove all whitespaces from a string.

import re
text1 = ' Python    Exercises '
print("Original string:",text1)
print("Without extra spaces:",re.sub(r'\s+', '',text1))
