import re

namel = []

# pattern to search for any character other then a-z A-Z
pattern = r'[^\.a-zA-Z]'

# Input email addresses: john@google.com,jojo123@yahoo.com,jake@google.com
# will return john,jake
emailaddrs = [x for x in input("Enter email address separated by comma: ").split(',')]

print(emailaddrs)

for email in emailaddrs:
    name = email.split('@')
    test_str = name[0]
    # re.search returns None if no position in the string matches the pattern

    if re.search(pattern, test_str):
        # Character other then a-z A-Z was found
        # print('Invalid : %r' % (test_str,))
        continue
    else:
        # No character other then a-z A-Z was found
        # print('Valid   : %r' % (test_str,))
        namel.append(test_str)

print(','.join(namel))
