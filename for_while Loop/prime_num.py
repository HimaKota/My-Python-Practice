# Check given number is prime or not

num = int(input("enter value "))

for i in range(2,num):
    if (num % i) == 0:
        print(num, "is not a prime number")
        break
else:
    print(num, "is a prime number")