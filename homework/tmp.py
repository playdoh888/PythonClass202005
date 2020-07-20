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
print("%-20s, your average score is: %4.1f" % (name, average_score))