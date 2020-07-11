"""
The ABC company is building a basketball court for its employees to improve company morale.
You are creating a Python program that employees can use to keep track of their average score.
The program must allow users to enter their name and current scores.
The program will output the user name and the user's average score.
The output must meet the following requirements:
-> The user name must be left-aligned.
-> If the user name has fewer than 20 characters, additional space must be added to the right.
-> The average score must have three places to the left of the decimal point and one place to the right of the decimal (XXX.X).
"""

name = input("What is your name? ")
score = 0
count = 0
sum = 0
while(score != -1):
    score = int(input("Enter your scores: (-1 to end): "))
    if score == -1:
        break
    sum += score
    count += 1
average_score = sum / count
print("%-20s, your average score is: %4.1f"%(name, average_score))

#%-20s
#%-20i
#%-20d
#%-20f

#1.4s
#4.1f
#4.1s
#1.4f
