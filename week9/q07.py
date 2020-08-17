# Regarding HW4 - Q7 below, the correct answer should be A and B.
# Break can only used within a loop.
# Python compiler will complain if break is used with the  “if, if...else” and “if...elif...else” statement.  :-)

y = []
for i in range(1, 10):
    if i % 2 == 0:
        y.append(i)
    else:
        continue

print(y)

z = []
i = 0
while True:
    i += 1
    if i % 2 == 0:
        z.append(i)
    elif i > 10:
        break
    else:
        continue

print(z)

name = input("Please enter your name: ")
if name == "Jack":
    print("Bad name!")
    break
elif name == "John":
    print("Good name!")
    continue
else:
    print(name)
