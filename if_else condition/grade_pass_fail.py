# Write a python script to accept student score as input then check if the score is >=0
# and <35 print failed, elif check score>=35 and score<60 print as passed with B grade,
# elif check score>=60 and score<75 print as passed with A grade, elif check score>=75 
# and score<100 print as passed with A+ or excellent Grade else print invalid score given.

score = int(input("Enter Student Score: "))
if score>=0 and score<35:
    print("You are failed")
elif score>=35 and score<60:
    print("You are passed with B Grade")
elif score>=60 and score<75:
    print("You are passed with A Grade")
elif score>=75 and score<100:
    print("You are passed with A+ Grade")
else :
    print("Invalid score given")