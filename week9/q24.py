import re

correctpasswords = []
str = input("Enter passwords separated by comma: ")

passwords = str.split(',')

for p in passwords:
    if len(p) < 6 or len(p) > 12:
        continue
    if not re.search("[a-z]", p):
        continue
    if not re.search("[A-Z]", p):
        continue
    if not re.search("[0-9]", p):
        continue
    if not re.search("[\$\#\@]", p):
        continue
    else:
        pass
    correctpasswords.append(p)

print(correctpasswords)
