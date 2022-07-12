# Write a Python program to abbreviate 'Road' as 'Rd.' in a given string.

import re
street = '21 Ramkrishna Road '
#Road is last word abbreviate to Rd.
print(re.sub('Road$', 'Rd.', street))
