numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
zipped = zip(numbers, letters)
print(zipped)
print(type(zipped))
print(list(zipped))

integers = [1, 2, 3]
letters = ['a', 'b', 'c']
floats = [4.0, 5.0, 6.0]
zipped = zip(integers, letters, floats)  # Three input iterables
print(list(zipped))

print(list(zip(range(5), range(100))))

from itertools import zip_longest

numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
longest = range(5)
zipped = zip_longest(numbers, letters, longest, fillvalue='?')
print(list(zipped))
