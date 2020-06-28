import re

pattern = '^a...s$'
test_string = 'abyss'
result = re.match(pattern, test_string)

if result:
    print("Search successful.")
else:
    print("Search unsuccessful.")

result = re.match(pattern, "abscdw")

if result:
    print("Search successful.")
else:
    print("Search unsuccessful.")

result = re.match(pattern, "kadase")

if result:
    print("Search successful.")
else:
    print("Search unsuccessful.")

result = re.match(pattern, "abous")

if result:
    print("Search successful.")
else:
    print("Search unsuccessful.")

result = re.match(pattern, "aaass")

if result:
    print("Search successful.")
else:
    print("Search unsuccessful.")

