def string_backspace_convert(target_string):
    preserved_string = ''
    for c in list(target_string) :
        if c != '#':
            preserved_string += c
        else:
            if len(preserved_string) >= 1:
                preserved_string = preserved_string[:-1]
    return preserved_string

S = "a#c"
T = "b"
result1 = string_backspace_convert(S)
result2 = string_backspace_convert(T)
if result1 == result2:
    print(True)
else:
    print(False)

print("Start another script that does the same thing!")

S = "a#c"
T = "b"

temp1 = []
for letter in S:
    if letter == '#' and len(temp1) > 0:
        temp1.pop()
    else:
        temp1.append(letter)

temp2 = []
for letter in T:
    if letter == '#' and len(temp2) > 0:
        temp2.pop()
    else:
        temp2.append(letter)

if temp1 == temp2:
    print(True)
else:
    print(False)
