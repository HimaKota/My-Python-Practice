# Write a program for pattern
#  A P Q R
#  A B Q R
#  A B C R
#  A B C D

str1 = 'ABCD'
str2 = 'PQR'
for i in range(0,len(str1)):
     print(str1[ : i+1 ] + str2[ i : ])