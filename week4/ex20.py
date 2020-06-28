import re

string = 'Twelve:12 Eighty nine:89.'
pattern = '\d+'

result = re.split(pattern, string)
print(result)

result = re.findall(pattern, string)
print(result)


# Output: ['Twelve:', ' Eighty nine:', '.']
