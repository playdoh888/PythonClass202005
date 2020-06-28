# Program to remove all whitespaces
import re

# multiline string
string = 'abc 12\
de 23 \n f45 6'

# matches all whitespace characters
pattern = '\s+'

# empty string
replace = ''

result = re.split(pattern, string)
print(result)

new_string = re.sub(pattern, replace, string)
print(new_string)

# Output: abc12de23f456
