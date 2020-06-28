import re

string = "The rain in Spain"
pat = "^The.*Spain$"

x = re.search(pat, string)

if x:
    print("YES! We have a match!")
else:
    print("No match")

