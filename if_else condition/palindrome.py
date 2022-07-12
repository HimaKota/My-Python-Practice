#Write a program to check given Number is palindrom or not

string=input(("Enter a string: "))
my_str = string.lower()
if(my_str==my_str[::-1]):
      print("The string is a palindrome")
else:
      print("Not a palindrome")