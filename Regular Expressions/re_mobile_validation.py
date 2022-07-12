#mobile number validation code using regular expression

# m_phones=['9341910328','9341910345','7341910327','934191032X']
my_file = open("File Handling\mobiledata.txt", "r")
# reading the file
data=my_file.read()
data_into_list = data.split("\n")
import re
for i in data_into_list:
    if len(i)==10:  #check for the 10 digits length
        if re.findall('[9,8]{1}[0-9]{9}',i):
            print("It's valid %s number "%i)
        else:
            print("It's Invalid %s number "%i)
